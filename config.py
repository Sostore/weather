from os import getenv

LANGUAGE = "en"
UNITS = "metric"
USE_ROUNDED_COORDS = True
OPENWEATHER_API = getenv('OPENWEATHER_API')
OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + OPENWEATHER_API + "&lang=" + LANGUAGE + "&"
    "units=" + UNITS
)
