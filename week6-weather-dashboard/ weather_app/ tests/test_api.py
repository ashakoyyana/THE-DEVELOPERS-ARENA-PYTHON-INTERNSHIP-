from weather_app.weather_api import WeatherAPI

def test_api_object():
    api = WeatherAPI("dummy")
    assert api is not None
