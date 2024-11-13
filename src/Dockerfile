# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements.txt first (this helps Docker cache layers)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the remaining files
COPY . .

# Expose a port if needed
EXPOSE 80

# Run the script when the container launches
CMD ["python", "./GetWeather.py"]
