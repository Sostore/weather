from weather_api_service import Weather, Forecast


def format_weather(weather: Weather) -> str:
    """Formats weather data to string"""
    return (f"Date: {weather.date},\n"
            f"{weather.city}, Temperature {weather.temperature}°С, "
            f"{weather.weather_type.value}\n"
            f"Sunrise: {weather.sunrise.strftime('%H:%M')}\n"
            f"Sunset: {weather.sunset.strftime('%H:%M')}\n")


def format_forecast(forecast: Forecast):
    """Formats forecast data to string"""
    # 5 day / 3 hour forecast
    for weather in forecast:
        print(f"{weather.date.strftime('%A')}, {weather.date.time()}\n"
              f"{weather.temperature}°С, "
              f"{weather.weather_type.value}\n")
