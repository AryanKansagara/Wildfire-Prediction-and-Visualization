import geopandas as gpd
from shapely.geometry import Point
import numpy as np

def spread_fire(fire_data, wind_speed=0, wind_direction=0, spread_factor=1.0):
    """
    Simulate the spread of fire based on intensity and optional weather parameters.
    
    :param fire_data: GeoDataFrame with columns ['latitude', 'longitude', 'intensity'].
    :param wind_speed: Wind speed influencing the fire spread (default: 0).
    :param wind_direction: Wind direction in degrees (0 = North, 90 = East, etc.).
    :param spread_factor: Factor determining how far fires can spread (default: 1.0).
    :return: GeoDataFrame with updated fire locations and intensities.
    """
    updated_fire_data = fire_data.copy()

    for idx, row in updated_fire_data.iterrows():
        # Modify intensity based on spread factor
        updated_fire_data.at[idx, "intensity"] = row["intensity"] * spread_factor

        # Spread fire based on wind and intensity
        # Convert wind direction to radians
        wind_rad = np.radians(wind_direction)

        # Calculate displacement using wind and spread factor
        displacement = spread_factor * wind_speed * row["intensity"] / 10.0
        delta_lat = displacement * np.cos(wind_rad) / 111.0  # Approx conversion to lat degrees
        delta_lon = displacement * np.sin(wind_rad) / (111.0 * np.cos(np.radians(row["latitude"])))

        updated_fire_data.at[idx, "latitude"] += delta_lat
        updated_fire_data.at[idx, "longitude"] += delta_lon
        updated_fire_data.at[idx, "geometry"] = Point(row["longitude"] + delta_lon, row["latitude"] + delta_lat)

    return updated_fire_data
