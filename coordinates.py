from typing import NamedTuple

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

import config
from exceptions import CantGetCoordinates, GeocoderServiceError


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_coordinates() -> Coordinates:
    """Returns coordinates"""
    city_name = input("Enter your location (City, address, etc...): ")
    coordinates = _get_coords_by_city_name(city_name)
    return _round_coordinates(coordinates)


def _get_coords_by_city_name(city_name: str) -> Coordinates:
    """Returns coordinates by city name using geopy"""

    geolocator = Nominatim(user_agent="GetLoc")
    try:
        location = geolocator.geocode(city_name)
    except GeocoderTimedOut:
        raise GeocoderServiceError

    if location == None:
        raise CantGetCoordinates

    if config.SHOW_COORDS:
        print(location.latitude, location.longitude)
        
    return Coordinates(latitude=location.latitude, longitude=location.longitude)


def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    if not config.USE_ROUNDED_COORDS:
        return coordinates
    return Coordinates(*map(
        lambda c: round(c, 4),
        [coordinates.latitude, coordinates.longitude]
    )) 


if __name__ == "__main__":
    coords = get_coordinates()
    print(f"Latitude: {coords.latitude}\
            \nLongitude: {coords.longitude}")
