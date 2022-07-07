import config
from coordinates import get_coordinates
from weather_api_service import get_weather, get_forecast
from weather_formatter import format_weather, format_forecast
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

    try:
        forecast = get_forecast(coordinates)
    except ApiServiceError:
        print(f"Can't get forecast by coordinates: {coordinates}")
        
    print(format_weather(weather))
    if config.SHOW_FORECAST:
        format_forecast(forecast)


if __name__ == "__main__":
    main()
