from flask import Flask, jsonify, request
from twikit import Client, TooManyRequests
import time
from datetime import datetime
from configparser import ConfigParser
from random import randint

app = Flask(__name__)

# japanese
DEFAULT_QUERY = '(from:elonmusk) lang: en'
DEFAULT_LIMIT = 10

# Leer configuraciones de usuario desde config.ini
config = ConfigParser()
config.read('config.ini')
username = config['X']['username']
email = config['X']['email']
password = config['X']['password']

# Autenticar con X.com
client = Client(language='en-US')
client.load_cookies('cookies.json')

def get_tweets(query, tweets=None):
    if tweets is None:
        print(f'{datetime.now()} - Getting tweets for query: {query}')
        tweets = client.search_tweet(query, product='Top')
    else:
        wait_time = randint(5, 10)
        print(f'{datetime.now()} - Getting next tweets after {wait_time} seconds...')
        time.sleep(wait_time)
        tweets = tweets.next()
    return tweets

@app.route('/tweets', methods=['GET'])
def fetch_tweets():
    # Obtener los parámetros 'username' y 'limit' desde la URL
    user = request.args.get('username')
    limit = request.args.get('limit', DEFAULT_LIMIT)
    
    try:
        limit = int(limit)
    except ValueError:
        return jsonify({"error": "Invalid limit value, it must be a number"}), 400

    # Si no se proporciona un nombre de usuario, usar la consulta predeterminada
    if not user:
        query = DEFAULT_QUERY
    else:
        # Crear consulta con el usuario proporcionado
        query = f'(from:{user}) lang:en'

    tweet_count = 0
    tweets = None
    all_tweets = []

    while tweet_count < limit:
        try:
            tweets = get_tweets(query, tweets)
        except TooManyRequests as e:
            rate_limit_reset = datetime.fromtimestamp(e.rate_limit_reset)
            print(f'{datetime.now()} - Rate limit reached. Waiting until {rate_limit_reset}')
            wait_time = rate_limit_reset - datetime.now()
            time.sleep(wait_time.total_seconds())
            continue

        if not tweets:
            print(f'{datetime.now()} - No more tweets found')
            break

        for tweet in tweets:
            tweet_count += 1
            tweet_data = {
                "Tweet_count": tweet_count,
                "Username": tweet.user.name,
                "Text": tweet.text,
                "Created_At": tweet.created_at,
                "Retweets": tweet.retweet_count,
                "Likes": tweet.favorite_count
            }
            print(f'{datetime.now()} - Tweet {tweet_count}: {tweet_data["Text"]}')
            all_tweets.append(tweet_data)

            if tweet_count >= limit:
                break

    return jsonify(all_tweets), 200

if __name__ == '__main__':
    app.run(debug=True)
