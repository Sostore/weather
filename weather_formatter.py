from weather_api_service import Weather


def format_weather(weather: Weather) -> str:
    """Formats weather data to string"""
    return (f"{weather.city}, Temperature {weather.temperature}°С, "
            f"{weather.weather_type.value}\n"
            f"Sunrise: {weather.sunrise.strftime('%H:%M')}\n"
            f"Sunset: {weather.sunset.strftime('%H:%M')}\n")
