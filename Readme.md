# GetWeather Application

## Overview
`GetWeather.py` is a simple Python script that retrieves the current temperature for a specified city using the OpenWeatherMap API. The project also includes a `Dockerfile` for containerizing the application.

## Features
- Fetches real-time weather data for any city.
- Uses the OpenWeatherMap API.
- Dockerized for easy deployment.

## Files
- **`GetWeather.py`**  
  Main Python script that interacts with the OpenWeatherMap API.
- **`Dockerfile`**  
  Configuration file for building a Docker image of the application.

## Requirements
- Python 3.9 or higher
- A valid OpenWeatherMap API key
- `requests` library for Python

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-folder>
```




### 2. Install Dependencies
```bash
 pip install -r requirements.txt
```


### 3. Run the Script
```bash
 python GetWeather.py
```

### Using Docker


docker build -t getweather .

docker run -it getweather
