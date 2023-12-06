from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

def notify_azure_function(city, temperature):
    azure_function_url = 'https://your-azure-function-url/api/your-function-name'  # Replace with your Azure Function URL
    payload = {'city': city, 'temperature': temperature}
    response = requests.post(azure_function_url, json=payload)
    
    # Log the response or perform other actions based on your requirements
    print(response.text)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    api_key = '851d7e5e0791f11560c8a8811f33a526'  # Replace with your actual API key
    weather_data = get_weather_data(city, api_key)
    
    # Extract temperature from the weather data
    temperature = weather_data.get('main', {}).get('temp', 0)

    # Trigger the Azure Function when the temperature is greater than 50°F
    if float(temperature) > 50.0:
        notify_azure_function(city, temperature)

    return render_template('weather.html', city=city, weather_data=weather_data)

def get_weather_data(city, api_key):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key, 'units': 'imperial'}
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    return weather_data

if __name__ == '__main__':
    app.run(debug=True)
