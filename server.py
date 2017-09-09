from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return "How are you?"

@app.route('/weather')
def weather(arg):
    return render_template('weather.html')


if __name__ == "__main__":
    app.run(debug=True)
