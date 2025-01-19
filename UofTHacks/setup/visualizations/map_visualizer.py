
# import os
import folium

# def visualize_fire(latitude, longitude, radius=10):
#     # Create a map centered around the fire location
#     m = folium.Map(location=[latitude, longitude], zoom_start=12)

#     # Add a circle to represent the fire spread
#     folium.Circle(
#         location=[latitude, longitude],
#         radius=radius * 1000,  # Convert to meters
#         color='red',
#         fill=True,
#         fill_opacity=0.5
#     ).add_to(m)

#     # Get the current directory of this script
#     current_dir = os.path.dirname(os.path.realpath(__file__))

#     # Save the map to an HTML file in the same folder
#     m.save(os.path.join(current_dir, "fire_map.html"))

# if __name__ == "__main__":
#     visualize_fire(34.0522, -118.2437, radius=10)  # Fire at Los Angeles with a 10 km radius


# def visualize_fire(fire_data, base_lat, base_lon):
#     """
#     Visualize fire locations on a map.
    
#     :param fire_data: DataFrame with 'latitude', 'longitude', and 'intensity'.
#     :param base_lat: Central latitude for the map.
#     :param base_lon: Central longitude for the map.
#     """
#     m = folium.Map(location=[base_lat, base_lon], zoom_start=6)
    
#     for _, row in fire_data.iterrows():
#         folium.Circle(
#             location=[row["latitude"], row["longitude"]],
#             radius=row["intensity"] * 100,
#             color="red",
#             fill=True,
#             fill_opacity=0.5
#         ).add_to(m)
    
#     m.save("visualizations/fire_map.html")


import folium
import pandas as pd
import os
from datetime import datetime

def visualize_fire(fire_data, base_lat, base_lon, output_file=None, map_zoom=6, circle_color="red"):
    """
    Visualize fire locations on a map.
    
    :param fire_data: DataFrame with 'latitude', 'longitude', and 'intensity'.
    :param base_lat: Central latitude for the map.
    :param base_lon: Central longitude for the map.
    :param output_file: Optional output file path for the map. Defaults to timestamped file.
    :param map_zoom: Initial zoom level for the map.
    :param circle_color: Color of the fire intensity circles.
    """
    # Validate fire_data
    if not {"latitude", "longitude", "intensity"}.issubset(fire_data.columns):
        raise ValueError("Fire data must contain 'latitude', 'longitude', and 'intensity' columns.")

    # Create a folium map centered on the base location
    m = folium.Map(location=[base_lat, base_lon], zoom_start=map_zoom)

    # Add fire circles to the map
    for _, row in fire_data.iterrows():
        folium.Circle(
            location=[row["latitude"], row["longitude"]],
            radius=row["intensity"] * 100,  # Adjust scaling as needed
            color=circle_color,
            fill=True,
            fill_opacity=0.5
        ).add_to(m)

    # Determine output file name
    if output_file is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"visualizations/fire_map.html"

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Save the map
    m.save(output_file)
    print(f"Map saved to: {output_file}")

if __name__ == "__main__":
    # Example fire data
    fire_sample = {
        "latitude": [34.0522, 35.0522, 36.0522],
        "longitude": [-118.2437, -119.2437, -120.2437],
        "intensity": [5, 3, 8]
    }
    fire_data = pd.DataFrame(fire_sample)

    # Visualize fire data
    visualize_fire(fire_data, base_lat=34.0522, base_lon=-118.2437)
