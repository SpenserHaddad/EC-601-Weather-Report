from flask import Flask, render_template, request
import weather

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('input.html')


@app.route('/weather', methods=['POST'])
def weather_report():
    zipcode = request.form['zip']
    tempk = weather.get_weather_by_zip(zipcode).temperature
    return render_template('weather.html', temp=tempk)


if __name__ == "__main__":
    app.run(debug=True)
