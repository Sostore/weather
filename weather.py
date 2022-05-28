from coordinates import get_coordinates
from weather_api_service import get_weather
from weather_formatter import format_weather
from exceptions import CantGetCoordinates, ApiServiceError, GeocoderServiceError

def main():
    try:
        coordinates = get_coordinates()
    except CantGetCoordinates:
        print("Can't get GPS coordinates")
        exit(1)
    except GeocoderServiceError:
        print("Enter correct location name!")
        exit(1)

    try:
        weather = get_weather(coordinates)
    except ApiServiceError:
        print(f"Can't get weather by coordinates: {coordinates}")
        exit(1)
        
    print(format_weather(weather))

if __name__ == "__main__":
    main()
