import json
import ssl
import urllib
from datetime import datetime
from enum import Enum
from typing import Literal, NamedTuple
from urllib.error import URLError

import config
from coordinates import Coordinates
from exceptions import ApiServiceError

Celsius = int

class WeatherType(Enum):
    THUNDERSTORM = "Thunderstorm"
    DRIZZLE = "Drizzle"
    RAIN = "Rain"
    SNOW = "Snow"
    CLEAR = "Clear"
    FOG = "Fog"
    CLOUDS = "Clouds"


class Weather(NamedTuple):
    date: datetime
    temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str


Forecast = list[Weather]


def get_weather(coordinates: Coordinates) -> Weather:
    """Requests weather in OpenWeather API and returns it"""
    response = _get_openweather_response(
        "weather",
        latitude=coordinates.latitude,
        longitude=coordinates.longitude
    )
    return _parse_weather_response(response)


def get_forecast(coordinates: Coordinates) -> Forecast:
    """Requests forecast"""
    response = _get_openweather_response(
        "forecast",
        latitude=coordinates.latitude, 
        longitude=coordinates.longitude
    )
    return _parse_forecast_response(response)
    


def _get_openweather_response(call_type: Literal["weather"] | Literal["forecast"],
                              latitude: float, longitude: float) -> str:

    ssl._create_default_https_context = ssl._create_unverified_context
    url = config.OPENWEATHER_URL.format(
        type=call_type,
        latitude=latitude,
        longitude=longitude
    )
    try:
        return urllib.request.urlopen(url).read()
    except URLError:
        raise ApiServiceError


def _load_json(response: str):
    try:
        openweather_dict = json.loads(response)
    except json.JSONDecodeError:
        raise ApiServiceError
    return openweather_dict


def _parse_forecast_response(response: str) -> Forecast:
    openweather_dict = _load_json(response)
    return [_parse_weather(weather) for weather in openweather_dict["list"]]


def _parse_weather_response(response: str) -> Weather:
    openweather_dict = _load_json(response)
    return _parse_weather(openweather_dict)


def _parse_weather(openweather_dict: dict) -> Weather:
    return Weather(
        date=_parse_date(openweather_dict) if "dt" in openweather_dict else datetime.today,
        temperature=_parse_temperature(openweather_dict),
        weather_type=_parse_weather_type(openweather_dict),
        sunrise=_parse_sun_time(openweather_dict, "sunrise"),
        sunset=_parse_sun_time(openweather_dict, "sunset"),
        city=openweather_dict["name"] if "name" in openweather_dict else None
    )


def _parse_date(openweather_dict: dict):
    return datetime.fromtimestamp(openweather_dict["dt"])


def _parse_temperature(openweather_dict: dict) -> Celsius:
    return round(openweather_dict["main"]["temp"])


def _parse_weather_type(openweather_dict: dict) -> WeatherType:
    try:
        weather_type_id = str(openweather_dict["weather"][0]["id"])
    except (IndexError, KeyError):
        ApiServiceError

    weather_types = {
        "1": WeatherType.THUNDERSTORM,
        "3": WeatherType.DRIZZLE,
        "5": WeatherType.RAIN,
        "6": WeatherType.SNOW,
        "7": WeatherType.FOG,
        "800": WeatherType.CLEAR,
        "80": WeatherType.CLOUDS
    }

    for _id, _weather_type in weather_types.items():
        if weather_type_id.startswith(_id):
            return _weather_type
    raise ApiServiceError


def _parse_sun_time(
        openweather_dict: dict,
        time: Literal["sunrise"] | Literal["sunset"]) -> datetime:
    if "sunset" in openweather_dict['sys'] or "sunrise" in openweather_dict['sys']:
        return datetime.fromtimestamp(openweather_dict["sys"][time])
    else:
        return None


if __name__ == "__main__":
    print(get_weather(Coordinates(latitude=51.5073219, longitude=-0.1276474)))
