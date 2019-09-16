from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/currentstats', methods=['POST'])
def temperature():
    zipcode = request.form['zip']   # prompts a zip code from the user
    url = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=b3726d1c22de02e3dbf12fd1393f94a8')    # api url with id
    obj = url.json()
    kelvin = float(obj['main']['temp']) # fetches temperature from main
    fahrenheit = (kelvin - 273.15) * 9 / 5 + 32     # converts Kelvin to Farenheit
    hum = obj['main']['humidity']   # fetches humidity from main
    return render_template('stats.html', temp=fahrenheit, humidity=hum) # returns template to stats.html

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
