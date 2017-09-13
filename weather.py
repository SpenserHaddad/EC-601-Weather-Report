"""Wrapper around the open weather API

Uses the API key provided by the environment variable OPEN_WEATHER_API_KEY

Functions:
    get_weather_by_zip(zip)
    get_weather_by_coordinate(long, lat)
"""
from collections import namedtuple
import requests

WEATHER_API_URL = r'http://api.openweathermap.org/data/2.5/forecast'
API_KEY = '902daaa31b338d0d36827a506b7353e3'
GEO_IP_URL = r'http://freegeoip.net/json'

Weather = namedtuple('Weather', ('temperatures', 'weather'))


def get_weather_by_zip(zip_code, country_code='us'):
    params = {'appid': API_KEY,
              'zip': f'{zip_code},{country_code}'}
    r = requests.get(WEATHER_API_URL, params=params)
    weather_data = r.json()
    return unpack_weather_data(weather_data)


def get_weather_by_ip(ip):
    lat, lon = _get_ip_coordinates(ip)
    return get_weather_by_coordinate(lat, lon)


def get_weather_by_coordinate(lat, lon):
    params = {'lat': lat, 'lon': lon, 'appid': API_KEY}
    r = requests.get(WEATHER_API_URL, params=params)
    weather_data = r.json()
    return unpack_weather_data(weather_data)


def get_weather_by_city(city, country):
    pass


def unpack_weather_data(weather_data):
    data = weather_data['list']

    temp = []
    temp.append(data[0]['main']['temp'])
    temp.append(data[1]['main']['temp'])
    temp.append(data[2]['main']['temp'])
    temp.append(data[3]['main']['temp'])
    temp.append(data[4]['main']['temp'])

    for i in range(0,len(temp)):
        temp[i] = round(((temp[i]-273.15)*100)/100,2)

    weathers = [data['weather'][0]['main'] for data in data[0:5]]
    return Weather(temperatures=temp, weather=weathers)


def _get_ip_coordinates(ip):
    params = {'q': ip}
    r = requests.get(GEO_IP_URL, params=params)
    geo_data = r.json()
    return (geo_data['latitude'], geo_data['longitude'])
