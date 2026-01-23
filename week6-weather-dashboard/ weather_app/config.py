import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5"

if not API_KEY:
    raise ValueError("API key not found. Set OPENWEATHER_API_KEY in .env file.")
