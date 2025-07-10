from dotenv import load_dotenv
import os

def load_keys():
    load_dotenv()
    return os.getenv("API_KEY"), os.getenv("API_SECRET")
