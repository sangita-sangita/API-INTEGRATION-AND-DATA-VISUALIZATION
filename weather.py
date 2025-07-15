import requests
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = '581127197832298e7fd3857ed6bbfefb'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
CITIES = ['New York', 'London', 'Tokyo', 'Delhi', 'Sydney', 'Cape Town', 'Ramgarh', 'Ranchi']

def fetch_temperature(city, api_key):
    """Fetch the current temperature for a given city."""
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Temperature in Celsius
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return data['main']['temp']
    except requests.exceptions.RequestException as e:
        print(f"Network error for {city}: {e}")
    except KeyError:
        print(f"Unexpected response format for {city}: {response.text}")
    return None

def main():
    city_names = []
    temperatures_celsius = []

    for city in CITIES:
        temp = fetch_temperature(cit_
