import requests

API_KEY = '6cf356ceb2ec0ff941855d4a43144e0e'  # Replace with your OpenWeatherMap API key
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

def print_weather(weather):
    if weather:
        print(f"Weather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description']}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Pressure: {weather['pressure']} hPa")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("City not found or API request failed.")

if __name__ == '__main__':
    city = input("Enter city name: ")
    weather = get_weather(city)
    print_weather(weather)
