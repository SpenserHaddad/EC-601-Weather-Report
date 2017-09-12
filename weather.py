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

#Weather = namedtuple('Weather', ('temperature', 'weather'))
#temperatures = namedtuple('temperature_1','temperature_2',
#                          'temperature_3','temperature_4','temperature_5')

Weather = namedtuple('Weather', ('temperatures'))

def get_weather_by_zip(zip_code, country_code='us'):
    params = {'appid': API_KEY,
              'zip': f'{zip_code},{country_code}'}
    r = requests.get(WEATHER_API_URL, params=params)
    weather_data = r.json()
    temp=[]
    temp.append(weather_data['list'][0]['main']['temp'])
    temp.append(weather_data['list'][1]['main']['temp'])
    temp.append(weather_data['list'][2]['main']['temp'])
    temp.append(weather_data['list'][3]['main']['temp'])
    temp.append(weather_data['list'][4]['main']['temp'])
    print(temp)
    return Weather(temperatures=temp)

def get_weather_by_zip_1(zip_code, country_code='us'):
    params = {'appid': API_KEY,
              'zip': f'{zip_code},{country_code}'}
    r = requests.get(WEATHER_API_URL, params=params)
    weather_data = r.json()
    temp=[]
    temp.append(weather_data['list'][0]['main']['temp'])
    return Weather(temperatures=temp)
#    return Weather(temperature=temp,
#                   weather=weather_data['weather'][0]['main'])#weather是天气状况：多云....
#
#def get_weather_by_ip(ip):
#    lat, long_ = _get_ip_coordinates(ip)
#    return get_weather_by_coordinate(lat, long_)


#def get_weather_by_coordinate(lat, long_):
#    params = {'lat': lat, 'long': long_}
#    r = requests.get(WEATHER_API_URL, params=params)
#    weather_data = r.json()
#    return Weather(temparature=weather_data['main']['temp'],
#                   weather=weather_data['weather'][0]['main'])


#def _get_ip_coordinates(ip):
#    params = {'q': ip}
 #   r = requests.gt(GEO_IP_URL, params=params)
#    geo_data = r.json()
#    return (geo_data['latitude'], geo_data['longitude'])
