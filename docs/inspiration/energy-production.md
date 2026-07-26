---
layout: default
title: "Energy Production"
parent: "Inspiration"
nav_order: 4
redirect_from:
  - "/part 2 get creative/idea-4.html"
  - "/part 1 tutorials/connecting-to-the-internet/part-4.html"
  - "/tutorials/connecting-to-the-internet/part-4.html"
---

# Energy Production

How much renewable energy is being produced around you right now? While you cannot see directly what is currently coming out of your outlet, information about the weather that drives renewable energy is publicly available.

This project fetches live weather data for your location and turns it into something you can see on your desk. Start with the working example, then explore one of the directions suggested below.

{: .note }
This example needs a working WiFi connection. If you have not set that up yet, work through [Connecting To The Internet](../tutorials/connecting-to-the-internet/) first.

## Basic Example: Fetching Live Weather

We use [open-meteo.com](https://open-meteo.com), which is free and does not need an API key. Its documentation can be found here: [Open Meteo Docs](https://open-meteo.com/en/docs).

This version lights three LEDs to show the weather now, in one hour, and in two hours.

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
    response.close()
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

---

## Idea 1: A Solar Output Indicator

Solar panels produce a lot of electricity when the sky is clear, yet very little when it is cloudy. Cloud cover data is already part of the example above, so the same request can drive a simple indicator.

The LEDs fade from **red** (overcast, little solar energy) through amber to **green** (clear skies, panels producing lots of energy).

```python
# --- Imports
import time
import board
import wifi
import socketpool
import ssl
import adafruit_requests
import neopixel

from secrets import secrets

# --- Variables
latitude = 51.9607
longitude = 7.6261

weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=cloudcover&timezone=Europe/Berlin"

pixel_pin = board.GP18
num_pixels = 3
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False, pixel_order=neopixel.GRB)

# --- Setup
wifi.radio.connect(secrets["ssid"], secrets["password"])

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

# --- Functions
def get_cloudcover():
    response = requests.get(weather_url)
    data = response.json()
    response.close()
    return data["hourly"]["cloudcover"][0]

def solar_output(cloudcover):
    # Clear sky counts as full output, fully overcast as almost none
    return (100 - cloudcover) / 100

def show_output(level):
    red = int(255 * (1 - level))
    green = int(255 * level)
    pixels.fill((red, green, 0))
    pixels.show()

# --- Main loop
while True:
    cloudcover = get_cloudcover()
    level = solar_output(cloudcover)
    print(f"Cloud cover {cloudcover}% -> solar output {int(level * 100)}%")

    show_output(level)

    time.sleep(120)
```

### Take it further

- Use the forecast values to show whether output is about to rise or fall
- Compare two locations and light one strip per city
- Add the [OLED Screen](../components/oled-screen/oled-screen.html) to display more granular information

---

## Idea 2: A Wind Turbine For Your Desk

{: .highlight }
This one is a challenge, not a walkthrough.

We've shown solar energy as a light indicator, now let's show wind energy as movement. The [Mini Fan](../components/mini-fan/mini-fan.html) becomes a turbine that spins at the speed of the wind measured outside.

**What you need to work out:**

1. **Ask for wind data.** Add `windspeed_10m` to the `hourly=` list in the request URL. Reading the value back works exactly like `cloudcover` does above.

2. **Map wind speed to fan speed.** The API returns kilometres per hour, usually somewhere between 0 and 40. The `pwmio` module wants a duty cycle between `0` and `65535`. You need a rule that converts one into the other.

3. **Calibrate your behavior.** A DC motor will not start turning at a very low duty cycle, it will just sit there and buzz. Find the lowest value that reliably gets your fan spinning and treat that as your starting point.

**Questions worth answering while you build:**

- Should a calm day mean a stopped fan, or one that moves slowly?
- What happens above 40 km/h? Program a maximum speed cap or let it run at maximum and see what happens?
- Can you think of a clever way to indicate wind *direction* using `winddirection_10m`?

{: .note }
Wind and sun complement each other. It is often windiest when it is cloudiest. Combine both scenarios and you have a small model of why energy grids rely on a mix of renewable sources.

---

[Back to Overview](./){: .btn }
