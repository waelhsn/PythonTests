import os
import requests

key = os.getenv('API_KEY')
if not key:
    raise ValueError("No API key found. Please set the API_KEY environment variable.")

city = input("Enter the city: ")

# URL for the OpenWeatherMap API
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={key}'

# Perform the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    city = data['name']
    temperature = data['main']['temp']
    print(f"The temperature in {city} is {temperature}°C")
else:
    print(f"Failed to retrieve data: {response.status_code}")
