from geopy.geocoders import Nominatim


def get_location_by_city_name(city_name):
    try:
        geolocator = Nominatim(user_agent='app')
        location = geolocator.geocode(city_name)
        lat = location.latitude
        lon = location.longitude
        return lat, lon
    except:
        pass