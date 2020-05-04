import requests


UNITS = 'metric'
API_KEY = 'OPENWEATHER API KEY'


def get_current_weather_by_name(city_name:str):
    api_call = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units={UNITS}'
    return requests.get(api_call).json()

def get_current_weather_by_geo(lat:int, lon:int):
    api_call = f'https://api.openweathermap.org/data/2.5/forecast/weather?lat={lat}&lon={lon}&appid={API_KEY}&units={UNITS}'
    return requests.get(api_call).json()