from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return "How are you?"


@app.route('/weather/<arg>')
def weather(arg):
    return render_template('weather.html', arg=arg)


if __name__ == "__main__":
    app.run(debug=True)
