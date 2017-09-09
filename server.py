from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('input.html')


@app.route('/weather', methods=['POST'])
def weather():
    zipcode = request.form['zip']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=902daaa31b338d0d36827a506b7353e3')
    tempk = float(r.json()['main']['temp'])
    return render_template('weather.html', temp=tempk)

if __name__ == "__main__":
    app.run(debug=True)
