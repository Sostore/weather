from os import getenv

LANGUAGE = "en"
UNITS = "metric"
SHOW_COORDS = False
USE_ROUNDED_COORDS = True
SHOW_FORECAST = True
OPENWEATHER_API = getenv('OPENWEATHER_API')
OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/{type}?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + OPENWEATHER_API + "&lang=" + LANGUAGE + "&"
    "units=" + UNITS
)