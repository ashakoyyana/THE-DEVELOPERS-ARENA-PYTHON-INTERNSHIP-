import requests
import json
from datetime import datetime, timedelta
from pathlib import Path
import time
from typing import Optional, Dict

class WeatherAPI:
    def __init__(self, api_key, base_url="http://api.openweathermap.org/data/2.5"):
        self.api_key = api_key
        self.base_url = base_url
        self.cache_dir = Path("data/cache")
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.cache_duration = 600

    def _get_cached_data(self, cache_key):
        cache_file = self.cache_dir / f"{cache_key}.json"
        if cache_file.exists():
            if time.time() - cache_file.stat().st_mtime < self.cache_duration:
                with open(cache_file) as f:
                    return json.load(f)
        return None

    def _save_to_cache(self, cache_key, data):
        with open(self.cache_dir / f"{cache_key}.json", "w") as f:
            json.dump(data, f, indent=2)

    def _make_request(self, endpoint, params):
        params["appid"] = self.api_key
        params["units"] = "metric"
        try:
            r = requests.get(f"{self.base_url}/{endpoint}", params=params, timeout=10)
            if r.status_code == 200:
                return r.json()
        except:
            pass
        return None

    def get_current_weather(self, city, country_code=None):
        key = f"current_{city}_{country_code}" if country_code else f"current_{city}"
        cached = self._get_cached_data(key)
        if cached:
            return cached
        query = f"{city},{country_code}" if country_code else city
        data = self._make_request("weather", {"q": query})
        if data:
            self._save_to_cache(key, data)
        return data

    def get_forecast(self, city):
        return self._make_request("forecast", {"q": city})
