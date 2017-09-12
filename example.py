import requests

WEATHER_API_URL = r'http://api.openweathermap.org/data/2.5/weather'
API_KEY = '902daaa31b338d0d36827a506b7353e3'

bu_zip = '02215'

params = {'appid': API_KEY, 'zip': f'{bu_zip},us'}
r = requests.get(WEATHER_API_URL, params=params)

if r.status_code != 200:
    print('The call to the weather api failed. Probably a bad API key')
else:
    print('The call to the weather api succeeded, printing the temperature')
    temperature = r.json()['main']['temp']
    print(temperature)