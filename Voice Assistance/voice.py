import requests
import json

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        print(f"Response text: {response.text}")
        return None

def display_weather(weather_data):
    if weather_data:
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']
        wind_spd = weather_data['wind']['speed']

        print(f"\nCurrent Weather:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {description}")
        print ("Current wind speed: ",wind_spd ,'kmph')
    else:
        print("Unable to fetch weather data.")

def main():
    api_key = '671879501264c51d4720c83d22ea0f46'

    location = input("Enter city or ZIP code: ")

    weather_data = get_weather(api_key, location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
