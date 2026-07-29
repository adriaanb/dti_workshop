---
layout: default
title: "Part 4 - Send Data to the Internet"
parent: "Connecting To The Internet"
nav_order: 4
---

# Part 4 - Send Data to the Internet

So far you have used an [API](../../glossary/glossary) to *get* data over the internet onto your Pico. In this part, you turn it around. Your Pi Pico will use a different API to send data *out*. In this example, you will change the color of a virtual object within an Extended Reality (XR) environment using input coming from the physical world.

{:.note}
The XR side runs on [XRwise Creator](https://creator.xrwise.tech/), which you will learn more about in the next workshop. It offers the possibility to use external data sources via a `REST API` to influence objects within a virtual scene. Your Pi Pico becomes such a **source** by sending so-called `POST` requests that trigger an **effect** inside the virtual scene.

## Set Up the Interaction

In this example, we connect a [tactile switch](../../components/tactile-switch/tactile-switch.html) to **GP16**. The code below expects you to provide the **POST URL** and **Room ID** from **XRwise Creator** (ask the instructors if you are uncertain about where to find these), which you will define using the `SIGNAL_URL` and `ROOM_ID` variables respectively.

The code here also allows you to set a hexadecimal color value (`#ff0000` for red, for example), which will be posted to the API whenever you push the button. If the "Change Color" effect is configured in the creator's block coding module, you will then see the color of the linked object change inside the virtual environment.

{: .highlight-yellow }
XRwise is still under active development and may exhibit unexpected behavior. In this tutorial, we set the color of a primitive object (cube, sphere, cylinder, cone, and so on), which works reliably. Feel free to explore the other effects, but be aware that results may vary at this time.

```python
# --- Imports
import time
import board
import digitalio
import wifi
import socketpool
import ssl
import adafruit_requests

# Get WiFi details from your secrets.py file
from secrets import secrets

# --- Variables
# Paste the POST URL and Room ID from the Creator
SIGNAL_URL = "paste-the-post-url-here"
ROOM_ID = "paste-your-room-id-here"
INTERACTION_ID = 1

# The color that gets sent, as a hex value
COLOR = "#ff0000"

button = digitalio.DigitalInOut(board.GP16)
button.direction = digitalio.Direction.INPUT

was_pressed = False

# --- Setup

# Connect to WiFi using credentials from the secrets file
wifi.radio.connect(secrets["ssid"], secrets["password"])

# Set up socket pool and requests
pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

# --- Functions
def send_value(value):
    body = {
        "interactionId": INTERACTION_ID,
        "roomId": ROOM_ID,
        "payload": str(value),
    }
    response = requests.post(SIGNAL_URL, json=body)
    print("Sent", value, "- server replied", response.status_code)
    response.close()

# --- Main loop
while True:
    # Only act on the moment the button goes down, not while it is held
    if button.value and not was_pressed:
        send_value(COLOR)

    was_pressed = button.value
    time.sleep(0.05)
```

Save the file and press the button. The serial monitor prints every value it sends, and the object should change color.

{: .highlight }
The `was_pressed` variable works just like `last_state` in the [tactile switch](../../components/tactile-switch/tactile-switch.html) example: it remembers whether the button was already down on the previous run through the loop, so that one press sends exactly one signal. Without it, your Pico would send a request on every pass through the loop for as long as your finger rests on the button, which is dozens of requests per second.

## Sending a trigger instead of a value

Some interactions do not need a value at all. If you set the Source to **serves a trigger** inside XRwise Creator, it fires as soon as it receives anything. The effect it produces is fully defined inside the Creator instead of coming from the payload of your POST request:

```python
body = {"interactionId": INTERACTION_ID, "roomId": ROOM_ID}
```
