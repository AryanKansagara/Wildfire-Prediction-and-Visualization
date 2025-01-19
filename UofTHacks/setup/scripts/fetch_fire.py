
# scripts/fetch_fire.py
import pandas as pd
from io import StringIO
import requests
def fetch_fire_csv(api_key, date, bbox=None):
    """
    Fetch fire data CSV from the NASA FIRMS API.
    
    :param api_key: API key for authentication.
    :param date: Date for which to fetch fire data (in YYYY-MM-DD format).
    :param bbox: Optional bounding box for the area of interest (lat_min, lon_min, lat_max, lon_max).
    :return: Raw CSV string containing fire data.
    """
    # Updated URL for fetching fire data from FIRMS API
    url = "https://firms.modaps.eosdis.nasa.gov/api/activefire/csv"
    
    # Prepare parameters for the API request
    params = {
        "MAP_KEY": api_key,
        "date": date,
    }
    if bbox:
        params["bbox"] = bbox  # Optional bounding box parameter if provided
    
    # Make the API request to fetch fire data
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for any HTTP error (e.g., 400, 500)

        if response.status_code == 200:
            return response.text
        else:
            raise ValueError(f"Error fetching fire data: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching fire data: {e}")
        raise  # Re-raise the exception to be caught by the main function
