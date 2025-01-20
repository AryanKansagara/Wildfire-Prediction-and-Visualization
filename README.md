# Wildfire Prediction and Visualization

**A Python-based project to predict wildfire spread using real-time weather and fire data, paired with geospatial visualizations to aid decision-making and risk assessment.**

## Features
- 🔥 Predict wildfire spread based on weather and location data.
- 🌎 Visualize fire locations and affected areas on an interactive map.
- 🚀 Easy-to-use modular design for integration and scaling.

### Project Structure

```plaintext
📂 setup/  
├── data/                    # Directory for storing raw and processed data  
├── env/                     # Environment-related files  
├── models/spread_model/     # Fire spread simulation model  
├── scripts/                 # Scripts for fetching and preprocessing data  
│   ├── fetch_fire.py        # Fetches wildfire data from NASA FIRMS  
│   ├── fetch_weather.py     # Fetches weather data from OpenWeatherMap  
│   ├── preprocess.py        # Preprocessing for fire and weather data  
├── visualizations/          # Visualization tools and output maps  
│   ├── map_visualizer.py    # Visualizes fire locations on an interactive map  
├── main.py                  # Main execution file  
├── requirements.txt         # Python dependencies  
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/wildfire-prediction.git
   ```
2. Set Up Virtual Environment
   ```bash
   python -m venv env  
   source env/bin/activate  # On Windows, use 'env\Scripts\activate'  
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
## Usage
1. Fetch weather and fire data using the provided scripts:
   ```bash
   python main.py
   ```
2. API keys in the .env
   Replace placeholders in fetch_fire.py and fetch_weather.py with your NASA FIRMS and OpenWeatherMap API keys.

3. View the visualization: Open visualizations/fire_map.html in your browser.

## Acknowledgements 
* NASA FIRMS for wildfire data
* OpenWeatherMap for weather data
* Folium for interactive maps


