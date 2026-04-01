import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("MONGO_URI")
client = MongoClient(uri)

try:
    # On envoie une requête toute simple à Atlas
    client.admin.command('ping')
    print(" Connexion Atlas : OK ! Ton code parle enfin à ta base de données.")
except Exception as e:
    print(f" Erreur de connexion : {e}")
    print("Vérifie ton mot de passe dans le .env ou ton accès IP sur Atlas.")