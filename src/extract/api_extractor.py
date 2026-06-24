import requests
from dotenv import load_dotenv
import json
import os

load_dotenv()

API_URL = os.getenv("API_URL")

current_url = API_URL

todos_los_personajes = []

while current_url:

    response = requests.get(current_url)

    datos = response.json()

    todos_los_personajes.extend(datos['results'])

    current_url = datos["info"]["next"]

with open("data/raw/characters_raw.json", "w", encoding="utf-8")as f:
    json.dump(todos_los_personajes, f, indent=4, ensure_ascii=False) 

print(f"Personajes descargados: {len(todos_los_personajes)}")       