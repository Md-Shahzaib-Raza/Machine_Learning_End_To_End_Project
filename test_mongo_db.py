from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Read URL from .env
url = os.getenv("MONGO_DB_URL")

# Create client
client = MongoClient(url)

# Test connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

except Exception as e:
    print(e)