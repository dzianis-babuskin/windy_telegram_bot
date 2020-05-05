import requests

from src.const import API_KEY, UNITS
from src.geo import get_location_by_city_name


def get_current_weather_by_name(city_name:str):
    api_call = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units={UNITS}'
    return requests.get(api_call).json()

def get_hourly_weather_by_name(city_name:str, hours=5):
    lat, lon = get_location_by_city_name(city_name)
    api_call = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=daily&appid={API_KEY}&units={UNITS}'
    return requests.get(api_call).json()['hourly'][:hours]