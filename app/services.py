import os
from dotenv import load_dotenv
from mistralai.client import Mistral
from pymongo import MongoClient

load_dotenv()

# Mistral
api_key = os.getenv("MISTRAL_API_KEY")
mistral_client = Mistral(api_key)
MODEL = "mistral-large-latest"

# MongoDB
mongo_uri = os.getenv("MONGO_URI")
mongo_client = MongoClient(mongo_uri)
db = mongo_client["chatbot_db"]
conversations = db["conversations"]
