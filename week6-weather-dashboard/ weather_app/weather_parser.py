from datetime import datetime

class WeatherParser:
    @staticmethod
    def parse_current(data):
        return {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temp": data["main"]["temp"],
            "feels": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "condition": data["weather"][0]["description"].title(),
            "wind": data["wind"]["speed"],
            "time": datetime.fromtimestamp(data["dt"]).strftime("%Y-%m-%d %H:%M:%S")
        }

    @staticmethod
    def parse_forecast(data):
        forecast = []
        for item in data["list"][::8]:
            forecast.append({
                "date": item["dt_txt"].split()[0],
                "min": item["main"]["temp_min"],
                "max": item["main"]["temp_max"],
                "humidity": item["main"]["humidity"],
                "icon": item["weather"][0]["main"]
            })
        return forecast
