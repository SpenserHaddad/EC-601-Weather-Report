import re
import ipaddress
import os
from flask import Flask, render_template, request, redirect, url_for
import weather

app = Flask(__name__)

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


@app.route('/')
def index():
    return render_template('input.html')


@app.route('/weather', methods=['POST', 'GET'])
def weather_report():
    if request.method == 'POST':
        return redirect(url_for('weather_report',
                                location=request.form['location']))
    else:
        location = request.args['location'].strip()

        # Determine the type of location used
        if not location:
            return render_template('weather.html', failed=True)
        elif _location_is_zip(location):
            report = weather.get_weather_by_zip(location)
        elif _location_is_ip_addr(location):
            report = weather.get_weather_by_ip(location)
        else:  # Assume it's a city
            city, country = location.split(',')
            report = weather.get_weather_by_city(city.strip(), country.strip())
        return render_template('weather.html',
                               temp=report.temperatures, failed=False)
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

def _location_is_zip(location):
    # Match pattern of 5 numbers (assume we would only get valid zip codes)
    return bool(re.match(r'\d{5}', location))


def _location_is_ip_addr(location):
    try:
        # If this runs without problems then it's a valid ip
        ipaddress.ip_address(location)
        return True
    except ValueError:
        return False



if __name__ == "__main__":
    app.run(debug=True)
