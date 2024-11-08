import requests

key = 'Replace with your API key'
city = input("Enter the city: ")

# URL for the OpenWeatherMap API
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={key}'

# Perform the GET requestLondon
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    city = data['name']
    temperature = data['main']['temp']
    print(f"The temperature in {city} is {temperature}°C")
else:
    print(f"Failed to retrieve data: {response.status_code}")