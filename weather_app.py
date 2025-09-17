from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

# Get API key from environment variable
API_KEY = os.getenv('API_KEY', '6cf356ceb2ec0ff941855d4a43144e0e')
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        return {
            'city': city,
            'temperature': main['temp'],
            'description': weather['description'],
            'humidity': main['humidity'],
            'pressure': main['pressure'],
            'wind_speed': data['wind']['speed']
        }
    else:
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form.get('city')
    else:
        city = request.args.get('city')
    
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400
    
    weather_data = get_weather(city)
    if weather_data:
        return jsonify(weather_data)
    else:
        return jsonify({'error': 'City not found or API request failed'}), 404

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
