import requests
import os
from dotenv import load_dotenv

load_dotenv() 
api_key=os.getenv("API_KEY")


api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York"

def fetch_data():
      try:
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an error for bad responses
            print("Data fetched successfully!")
            print(response.json())
            return response.json()
      except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            raise

# fetch_data()

# def mock_fetch_data():
#     return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-07-13 03:43', 'localtime_epoch': 1752378180, 'utc_offset': '-4.0'}, 'current': {'observation_time': '07:43 AM', 'temperature': 23, 'weather_code': 122, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png'], 'weather_descriptions': ['Overcast'], 'astro': {'sunrise': '05:37 AM', 'sunset': '08:27 PM', 'moonrise': '10:28 PM', 'moonset': '08:19 AM', 'moon_phase': 'Waning Gibbous', 'moon_illumination': 95}, 'air_quality': {'co': '338.55', 'no2': '44.77', 'o3': '34', 'so2': '11.655', 'pm2_5': '20.905', 'pm10': '25.715', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 10, 'wind_degree': 134, 'wind_dir': 'SE', 'pressure': 1020, 'precip': 0, 'humidity': 81, 'cloudcover': 100, 'feelslike': 25, 'uv_index': 0, 'visibility': 14, 'is_day': 'no'}}