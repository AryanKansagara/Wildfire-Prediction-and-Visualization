import requests

def fetch_weather_data(api_key, lat, lon):
    """
    Fetch weather data using OpenWeatherMap API.

    :param api_key: API key for OpenWeatherMap.
    :param lat: Latitude of the location.
    :param lon: Longitude of the location.
    :return: Parsed weather data (wind speed and direction).
    """
    if not (-90 <= lat <= 90) or not (-180 <= lon <= 180):
        raise ValueError("Invalid latitude or longitude.")
    
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "wind_speed": data["wind"]["speed"],
            "wind_direction": data["wind"]["deg"]
        }
    else:
        raise ValueError(f"Error fetching weather data: {response.status_code} - {response.text}")

if __name__ == "__main__":
    # Example: Replace with actual API key and coordinates
    api_key = "2debbc894782e4e49b390cbab1a275c1"
    lat, lon = 34.0522, -118.2437
    weather = fetch_weather_data(api_key, lat, lon)
    print(weather)
