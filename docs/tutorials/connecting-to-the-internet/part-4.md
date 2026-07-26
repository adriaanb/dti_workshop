---
layout: default
title: "Part 4 - Advanced Example"
parent: "Connecting To The Internet"
redirect_from:
  - "/part 1 tutorials/connecting-to-the-internet/part-4.html"
---

# Advanced Example: Get Weather Data

This example gives you a basic view of how do use a different ` API` to get current weather data. We will be using [open-meteo.com](https://open-meteo.com), as it is easy to use and does not need an API Key. Its documentation can be found here: [Open Meteo Docs](https://open-meteo.com/en/docs)

```python
# --- Imports
import time
import board
import wifi
import socketpool
import ssl
import adafruit_requests
import neopixel
   
# Get WiFi details from your secrets.py file
from secrets import secrets

# --- Variables
latitude = 51.9607  # Latitude for Münster
longitude = 7.6261  # Longitude for Münster

# Open-Meteo API URL to fetch hourly forecasts for temperature, precipitation, and cloud cover
weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,precipitation,cloudcover&timezone=Europe/Berlin"

pixel_pin = board.GP18
num_pixels = 3
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False, pixel_order=neopixel.GRB)

# --- Setup

# Connect to WiFi using credentials from the secrets file
wifi.radio.connect(secrets["ssid"], secrets["password"])

# Set up socket pool and requests
pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

# --- Functions
def get_weather():
    response = requests.get(weather_url)
    weather_data = response.json()
    return weather_data

def update_leds(weather_conditions):
    # Turn off all LEDs first
    pixels.fill((0, 0, 0))

    # Define the colors
    colors = {
        "clear": (255, 255, 0),  # Sun - Yellow
        "rain": (0, 0, 255),  # Rain - Blue
        "cloud": (255, 255, 255),  # Clouds - White
    }

    # Update LEDs based on weather conditions
    for i, condition in enumerate(weather_conditions):
        if condition["cloudcover"] < 20 and condition["precipitation"] == 0:
            pixels[i] = colors["clear"]
            print(f"LED {i} on: Sun detected")
        elif condition["precipitation"] > 0:
            pixels[i] = colors["rain"]
            print(f"LED {i} on: Rain detected")
        elif condition["cloudcover"] >= 20:
            pixels[i] = colors["cloud"]
            print(f"LED {i} on: Clouds detected")
            
    # Ensure the changes are sent to the NeoPixel strip
    pixels.show()

# --- Main loop
while True:
    weather_data = get_weather()

    # Current weather condition and temperature
    current_temp = weather_data['hourly']['temperature_2m'][0]
    current_condition = {
        "cloudcover": weather_data['hourly']['cloudcover'][0],
        "precipitation": weather_data['hourly']['precipitation'][0],
    }
    print(f"Current temperature: {current_temp}°C")

    # Forecast for 1 hour ahead
    weather_1hr = {
        "cloudcover": weather_data['hourly']['cloudcover'][1],
        "precipitation": weather_data['hourly']['precipitation'][1],
    }

    # Forecast for 2 hours ahead
    weather_2hr = {
        "cloudcover": weather_data['hourly']['cloudcover'][2],
        "precipitation": weather_data['hourly']['precipitation'][2],
    }

    # Update LEDs with current weather and forecasts
    update_leds([current_condition, weather_1hr, weather_2hr])
    
    time.sleep(120)  # Wait for 2 minutes before fetching the weather again
```
