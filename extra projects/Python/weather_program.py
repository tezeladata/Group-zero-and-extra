import requests
from pprint import pprint

api_key = "238daee9e898e1e4618031c00ce980e4"

city = input("Enter city name: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + api_key + "&q=" + city

weather_data = requests.get(base_url).json()

pprint(weather_data)