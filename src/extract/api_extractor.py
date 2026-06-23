import requests
from dotenv import load_dotenv
import json
import os

load_dotenv()

API_URL = os.getenv("API_URL")

response = requests.get(API_URL)

datos = response.json()

with open("data/raw/characters_raw.json", "w") as f:
    json.dump(datos, f , indent= 4, ensure_ascii= False)

'''print(response.status_code)
print(len(datos["results"]))
print(datos.keys())
print(type(datos["results"]))
print(datos["results"][0])'''