import requests
import argparse


# get_weather function where api call is maade to openweathermap.org and the json response is returned also exception handling is done.
def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=bd5e378503939ddaee76f12ad7a97608'
    
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

# parse_weather function where the json response is parsed and required data is displayed.
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


# main function where argparse is used to get the city name from the user and call get_weather function to get weather_data which is later parsed by parse_weather
def main():
    parser = argparse.ArgumentParser(description='Get weather forecast for a city')
    parser.add_argument('city', type=str, help='Name of the city')
    args = parser.parse_args()
    weather_data = get_weather(args.city)

    if weather_data:
        parse_weather(weather_data)

if __name__ == '__main__':
    main()