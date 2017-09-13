"""Wrapper around the open weather API

Uses the API key provided by the environment variable OPEN_WEATHER_API_KEY

Functions:
    get_weather_by_zip(zip)
    get_weather_by_coordinate(long, lat)
"""
from collections import namedtuple
#import os
import requests

#WEATHER_API_URL = r'http://api.openweathermap.org/data/2.5/weather'
WEATHER_API_URL = r'http://api.openweathermap.org/data/2.5/forecast'
API_KEY = '902daaa31b338d0d36827a506b7353e3'
GEO_IP_URL = r'http://freegeoip.net/json'


Weather = namedtuple('Weather', ('temperatures'))

def get_weather_by_zip(zip_code, country_code='us'):
    params = {'appid': API_KEY,
              'zip': f'{zip_code},{country_code}'}
    r = requests.get(WEATHER_API_URL, params=params)
    weather_data = r.json()
    temp=[]
    for i in range(5) :
        temp.append(weather_data['list'][i]['main']['temp'])
    return Weather(temperatures=temp)

def get_weather_by_zip_1(zip_code, country_code='us'):
    params = {'appid': API_KEY,
              'zip': f'{zip_code},{country_code}'}
    r = requests.get(WEATHER_API_URL, params=params)
    weather_data = r.json()
    temp=[]
    temp.append(weather_data['list'][0]['main']['temp'])
    return Weather(temperatures=temp)


def get_weather_by_ip(ip):
    lat, long_ = _get_ip_coordinates(ip)
    return get_weather_by_coordinate(lat, long_)


def get_weather_by_coordinate(lat, long_):
    params = {'lat': lat, 'long': long_}
    r = requests.get(WEATHER_API_URL, params=params)
    weather_data = r.json()
    temp=[]
    for i in range(5) :
        temp.append(weather_data['list'][i]['main']['temp'])
    return Weather(temperatures=temp)
#    return Weather(temparature=weather_data['main']['temp'])


def _get_ip_coordinates(ip):
    params = {'q': ip}
    r = requests.gt(GEO_IP_URL, params=params)
    geo_data = r.json()
    return (geo_data['latitude'], geo_data['longitude'])
