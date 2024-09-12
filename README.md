# Twitter Data Scraping API

Este proyecto proporciona una API en Python para extraer datos de Twitter mediante técnicas de web scrapping. La API permite obtener tweets en tiempo real a partir de un nombre de usuario y un límite de tweets, y devuelve la información en formato JSON.

## Características

- Extracción de tweets basados en un nombre de usuario y un número límite de tweets.
- La información devuelta incluye:
  - Fecha de creación del tweet
  - Número de likes
  - Número de retweets
  - Texto del tweet
  - Número de tweet en la consulta
  - Nombre del usuario de Twitter

## Requisitos

- Python 3.8 o superior
- Entorno virtual (venv)

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/DivorcedLance/twitter-connector-backend
   cd twitter-connector-backend
   ```

2. Crea y activa un entorno virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Corre la API con el siguiente comando:

   ```bash
   python app.py
   ```

2. La API estará disponible en `http://localhost:5000/tweets`. Para obtener tweets, puedes hacer una petición GET con los parámetros `username` y `limit`:

   ```http
   http://localhost:5000/tweets?username=elonmusk&limit=5
   ```

3. El resultado será un JSON con la información de los tweets extraídos.

## Ejemplo de respuesta

```json
[
  {
    "Created_At": "Fri Sep 06 23:08:32 +0000 2024",
    "Likes": 464906,
    "Retweets": 31297,
    "Text": "Impressive AAA game from China!\n\nSeems oddly familiar 😂 https://t.co/LkrmoFhVou",
    "Tweet_count": 1,
    "Username": "Elon Musk"
  },
  ...
]
```

## Contribuciones

Las contribuciones son bienvenidas. Si tienes sugerencias o mejoras, no dudes en abrir un issue o enviar un pull request.