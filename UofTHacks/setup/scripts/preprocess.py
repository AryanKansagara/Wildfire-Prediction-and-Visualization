import geopandas as gpd
import pandas as pd  # Ensure pandas is imported
from shapely.geometry import Point

def preprocess_fire(fire_data):
    """
    Process fire data into a GeoDataFrame.

    :param fire_data: DataFrame with 'latitude', 'longitude', and 'intensity' columns.
    :return: GeoDataFrame with spatial information.
    """
    if not {"latitude", "longitude", "intensity"}.issubset(fire_data.columns):
        raise ValueError("Fire data missing required columns: latitude, longitude, intensity.")
    
    fire_gdf = gpd.GeoDataFrame(
        fire_data, geometry=gpd.points_from_xy(fire_data['longitude'], fire_data['latitude'])
    )
    return fire_gdf

if __name__ == "__main__":
    # Example fire data
    fire_sample = {
        'latitude': [34.0522, 35.0522],
        'longitude': [-118.2437, -119.2437],
        'intensity': [300, 400]
    }
    fire_gdf = preprocess_fire(pd.DataFrame(fire_sample))  # Use pandas DataFrame here
    print(fire_gdf)

