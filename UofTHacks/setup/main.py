
# from scripts.fetch_fire import fetch_fire_data



# def main():
#     # Fetch fire data as CSV
#     fire_api_key = "bb9be6f693d302f51c29fdf7667724b4"  # Replace with your actual API key
#     date_of_interest = "2025-01-18"

#     try:
#         fire_csv_data = fetch_fire_data(fire_api_key, date=date_of_interest)

#         # Save to a CSV file
#         with open("fire_data.csv", "w") as file:
#             file.write(fire_csv_data)
#             print("Fire data CSV saved successfully as 'fire_data.csv'.")
    
#     except Exception as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     main()





# from scripts.fetch_fire import fetch_fire_data
# from scripts.preprocess import preprocess_fire

# # from scripts.preprocess import preprocess_fire, preprocess_weather
# from models.spread_model.spread_simulation import spread_fire
# from visualizations.map_visualizer import visualize_fire

# def main():
#     # Fetch fire data and weather parameters
#     fire_api_key = "bb9be6f693d302f51c29fdf7667724b4"  # Replace with your actual API key
#     date_of_interest = "2025-01-18"

#     try:
#         # Fetch the fire data (CSV format)
#         fire_csv_data = fetch_fire_data(fire_api_key, date=date_of_interest)
        
#         # Process the fire data into GeoDataFrame
#         fire_data = preprocess_fire(fire_csv_data)
        
#         # Extract environmental parameters (e.g., wind speed, temperature) for simulation
#         weather_data = {"main": {"temp": 300, "humidity": 40}, "wind": {"speed": 5, "deg": 180}}  # Replace with actual weather data
#         weather_params = preprocess_weather(weather_data)
        
#         # Set up a grid representing fire areas (this would depend on the fire data)
#         grid = np.zeros((10, 10))  # Example grid, replace with real data
#         grid[5, 5] = 1  # Initial fire point
        
#         # Simulate the fire spread based on weather parameters (e.g., wind speed)
#         fire_spread = spread_fire(grid, wind_speed=weather_params['wind_speed'], wind_direction=weather_params['wind_direction'], iterations=10)
        
#         # Visualize the fire spread on a map
#         for lat, lon in zip(fire_data['latitude'], fire_data['longitude']):  # Assume fire_data has latitude/longitude columns
#             visualize_fire(lat, lon, radius=10)
        
#         # Optionally, save the fire spread data for later use
#         print(f"Fire spread simulation complete. Data visualized on map.")
        
#     except Exception as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     main()


# import pandas as pd
# from scripts.fetch_fire import fetch_fire_data
# from scripts.preprocess import preprocess_fire

# def main():
#     # Fetch fire data as CSV
#     fire_api_key = "bb9be6f693d302f51c29fdf7667724b4"  # Replace with your actual API key
#     date_of_interest = "2025-01-18"

#     try:
#         fire_csv_data = fetch_fire_data(fire_api_key, date=date_of_interest)

#         # Parse the CSV string into a DataFrame
#         from io import StringIO
#         fire_data_df = pd.read_csv(StringIO(fire_csv_data))

#         # Preprocess the fire data
#         fire_df = preprocess_fire(fire_data_df)

#         # Save to a CSV file
#         fire_df.to_csv("fire_data.csv", index=False)
#         print("Fire data CSV saved successfully as 'fire_data.csv'.")

#     except Exception as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
# #     main()
# from scripts.fetch_weather import fetch_weather_data
# from scripts import fetch_fire
# from scripts.preprocess import preprocess_fire

# from models.spread_model.spread_simulation import spread_fire
# from visualizations.map_visualizer import visualize_fire
# from scripts.fetch_fire import process_fire_csv  # Import the new processing function.

# def main():
#     # Step 1: Fetch data
#     weather = fetch_weather_data("5c670df8ecb6f18953c4ad8e630e1b02", 34.0522, -118.2437)
#     fire_csv = process_fire_csv("bb9be6f693d302f51c29fdf7667724b4", date="2024-01-18")

#     # Step 2: Process data
#     weather_data = preprocess_fire(weather)
#     fire_data = process_fire_csv(fire_csv)

#     # Step 3: Visualize
#     visualize_fire(fire_data, 34.0522, -118.2437)

# if __name__ == "__main__":
#     main()

# ----------------------------

# import requests

# from scripts.fetch_weather import fetch_weather_data
# from scripts.fetch_fire import process_fire_csv  # Assuming it processes raw CSV data into a DataFrame.
# from scripts.preprocess import preprocess_fire
# from visualizations.map_visualizer import visualize_fire

# def fetch_fire_csv(api_key, date):
#     """
#     Fetch fire data CSV from an API or external source.
    
#     :param api_key: API key for authentication.
#     :param date: Date for which to fetch fire data.
#     :return: Raw CSV string.
#     """
#     # Example API URL, replace with the actual endpoint.
#     url = f"https://api.firedata.com/fetch?date={date}&key={api_key}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.text
#     else:
#         raise ValueError(f"Error fetching fire data: {response.status_code} - {response.text}")

# def main():
#     try:
#         # Step 1: Fetch Weather Data
#         weather_api_key = "5c670df8ecb6f18953c4ad8e630e1b02"
#         weather = fetch_weather_data(weather_api_key, 34.0522, -118.2437)

#         # Step 2: Fetch Fire Data
#         fire_api_key = "2485c48f8604576dfddbade3ebb7a033"
#         fire_csv = fetch_fire_csv(fire_api_key, date="2024-01-18")
#         fire_data = process_fire_csv(fire_csv)  # Process raw CSV into a DataFrame

#         # Step 3: Process Fire Data
#         processed_fire_data = preprocess_fire(fire_data)

#         # Step 4: Visualize Fire Data
#         visualize_fire(processed_fire_data, base_lat=34.0522, base_lon=-118.2437)

#         print("Visualization complete. Check the 'visualizations' folder for the output.")

#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     main()


# from scripts.fetch_weather import fetch_weather_data
# from scripts.fetch_fire import process_fire_csv  # Assuming it processes raw CSV data into a DataFrame.
# from scripts.preprocess import preprocess_fire
# from visualizations.map_visualizer import visualize_fire
# import requests

# def fetch_fire_csv(api_key, date):
#     """
#     Fetch fire data CSV from an API or external source.
    
#     :param api_key: API key for authentication.
#     :param date: Date for which to fetch fire data.
#     :return: Raw CSV string.
#     """
#     url = f"https://api.firedata.com/fetch?date={date}&key={api_key}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.text
#     else:
#         raise ValueError(f"Error fetching fire data: {response.status_code} - {response.text}")

# def main():
#     try:
#         # Step 1: Fetch Weather Data
#         weather_api_key = "5c670df8ecb6f18953c4ad8e630e1b02"
#         weather = fetch_weather_data(weather_api_key, 34.0522, -118.2437)

#         # Step 2: Fetch Fire Data
#         fire_api_key = "2485c48f8604576dfddbade3ebb7a033"  # Updated API Key
#         fire_csv = fetch_fire_csv(fire_api_key, date="2024-01-18")
#         fire_data = process_fire_csv(fire_csv)  # Process raw CSV into a DataFrame

#         # Step 3: Process Fire Data
#         processed_fire_data = preprocess_fire(fire_data)

#         # Step 4: Visualize Fire Data
#         visualize_fire(processed_fire_data, base_lat=34.0522, base_lon=-118.2437)

#         print("Visualization complete. Check the 'visualizations' folder for the output.")

#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     main()

from scripts.fetch_weather import fetch_weather_data
from scripts.fetch_fire import fetch_fire_csv  # Correct function name
from scripts.preprocess import preprocess_fire
from visualizations.map_visualizer import visualize_fire
import requests
import pandas as pd
from io import StringIO

def main():
    try:
        # Step 1: Fetch Weather Data
        weather_api_key = "5c670df8ecb6f18953c4ad8e630e1b02"
        weather = fetch_weather_data(weather_api_key, 34.0522, -118.2437)

        # Step 2: Fetch Fire Data
        fire_api_key = "2485c48f8604576dfddbade3ebb7a033"  # Updated API Key for FIRMS
        fire_csv = fetch_fire_csv(fire_api_key, date="2025-01-10")
        
        # Step 3: Print the raw CSV to inspect its structure
        print("Raw CSV data:\n", fire_csv)
        
        # Convert the raw CSV data to a pandas DataFrame
        fire_data = pd.read_csv(StringIO(fire_csv))
        
        # Step 4: Inspect the columns in the fire data to confirm
        print("Columns in the fire data:", fire_data.columns)

        # Step 5: Check if the expected columns are present
        if not {"latitude", "longitude", "brightness"}.issubset(fire_data.columns):
            print("Fire data doesn't contain the expected columns.")
            print("Column names in the fire data:", fire_data.columns)
            return
        
        # Step 6: Process Fire Data (assuming the correct columns are found)
        fire_data = fire_data.rename(columns={"brightness": "intensity"})  # If the column name is 'brightness'
        processed_fire_data = preprocess_fire(fire_data)

        # Step 7: Visualize Fire Data
        visualize_fire(processed_fire_data, base_lat=34.0522, base_lon=-118.2437)

        print("Visualization complete. Check the 'visualizations' folder for the output.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
