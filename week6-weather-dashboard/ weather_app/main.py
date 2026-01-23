from weather_app.config import API_KEY
from weather_app.weather_api import WeatherAPI
from weather_app.weather_parser import WeatherParser
from weather_app.weather_display import WeatherDisplay

api = WeatherAPI(API_KEY)

city = input("Enter city name: ")

current = api.get_current_weather(city)
forecast = api.get_forecast(city)

if current and forecast:
    parsed_current = WeatherParser.parse_current(current)
    parsed_forecast = WeatherParser.parse_forecast(forecast)

    WeatherDisplay.show_current(parsed_current)
    WeatherDisplay.show_forecast(parsed_forecast)
else:
    print("Unable to fetch weather data.")
