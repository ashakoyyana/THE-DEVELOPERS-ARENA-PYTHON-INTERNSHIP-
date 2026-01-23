class WeatherDisplay:
    @staticmethod
    def show_current(weather):
        print("\n🌤️  WEATHER DASHBOARD")
        print("=" * 22)
        print(f"\n📍 {weather['city']}, {weather['country']}")
        print(f"🕐 Last Updated: {weather['time']}\n")
        print(f"Temperature: {weather['temp']}°C (Feels like {weather['feels']}°C)")
        print(f"Conditions:  {weather['condition']}")
        print(f"Humidity:    {weather['humidity']}%")
        print(f"Wind Speed:  {weather['wind']} m/s")
        print(f"Pressure:    {weather['pressure']} hPa")

    @staticmethod
    def show_forecast(forecast):
        print("\n5-Day Forecast:")
        print("───────────────")
        for day in forecast:
            print(f"{day['date']}: {day['icon']}  {day['max']}°C / {day['min']}°C  (Humidity {day['humidity']}%)")
