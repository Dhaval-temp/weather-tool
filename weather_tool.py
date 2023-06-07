import requests
import json
import argparse

def get_weather(city, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for 4xx or 5xx errors
        data = response.json()
        return data
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection Error: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Something went wrong: {err}")

def parse_weather(data):
    if data['cod'] == 200:
        # Parsing required weather data from the response
        city_name = data['name']
        weather_desc = data['weather'][0]['description'].capitalize()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Displaying the weather forecast
        print(f"Weather forecast for {city_name}:")
        print(f"Description: {weather_desc}")
        print(f"Temperature: {temperature} K")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print(f"Error: {data['message']}")

def main():
    parser = argparse.ArgumentParser(description='Get weather forecast for a city')
    parser.add_argument('city', type=str, help='Name of the city')
    parser.add_argument('--api-key', type=str, help='OpenWeatherMap API key')
    args = parser.parse_args()

    if args.api_key:
        weather_data = get_weather(args.city, args.api_key)
    else:
        print("Error: Please provide an OpenWeatherMap API key using the '--api-key' argument.")
        return

    if weather_data:
        parse_weather(weather_data)

if __name__ == '__main__':
    main()
