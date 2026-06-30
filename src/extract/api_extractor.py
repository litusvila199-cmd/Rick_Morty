import json
import logging
import os

import requests
from dotenv import load_dotenv


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_characters():

    try:

        load_dotenv()

        api_url = os.getenv("API_URL")

        current_url = api_url

        todos_los_personajes = []

        while current_url:

            response = requests.get(current_url, timeout=10)
            response.raise_for_status()

            datos = response.json()

            todos_los_personajes.extend(datos["results"])

            current_url = datos["info"]["next"]

        with open("data/raw/characters_raw.json", "w", encoding="utf-8") as f:
            json.dump(todos_los_personajes, f, indent=4, ensure_ascii=False)

        logger.info(f"Personajes descargados: {len(todos_los_personajes)}")

        return todos_los_personajes

    except Exception as e:
        logger.error(f"Error during extraction: {e}")
        raise

if __name__ == "__main__":
    extract_characters()
