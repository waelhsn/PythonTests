# GetWeather Application

[![Docker Image CI](https://github.com/waelhsn/PythonTests/actions/workflows/docker-image.yml/badge.svg)](https://github.com/waelhsn/PythonTests/actions/workflows/docker-image.yml)

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
- A valid OpenWeatherMap API key. Link to get one: [OpenWeatherMap API Keys](https://openweathermap.org/appid)
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

### 3. Set the Environment Variable for the API Key
```bash
export OPENWEATHER_API_KEY=<your_api_key>
```

### 4. Run the Script
```bash
 python GetWeather.py
```

## Using Docker

### 1. Build the Docker image:

bash
Copy code

```bash
docker build -t <image-name> .
```
### 2. Run the Docker Container with an Environment Variable:

```bash
docker run -it --env API_KEY=your_api_key getweather
```
### 3. Verify the Environment Variable Inside the Container
  
```bash
echo $API_KEY
```