class CantGetCoordinates(Exception):
    """Program can't get current gps coordinates"""

class ApiServiceError(Exception):
    """Program can't get current weather"""

class GeocoderServiceError(Exception):
    """Geocoder can't get coordinates"""