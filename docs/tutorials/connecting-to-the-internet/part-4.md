---
layout: default
title: "Part 4 - Trigger AR Interactions"
parent: "Connecting To The Internet"
nav_order: 4
---

# Part 4 - Trigger AR Interactions

{: .highlight-yellow }
This page is a draft. The AR integration is still being set up and the details below will change before the workshop.

So far you have used the internet to *get* data onto your Pico. In this part, you turn it around: your Pico uses an API to send data out, in this case *to* an Augmented Reality (AR) stage you will explore more in the following days, and something happens in the shared AR scene.

The AR side runs on [xrwise](https://creator.xrwise.tech/). There, you will find a **Room ID** and an **Interaction ID**, **(TODO)**. Using these, your microcontroller can trigger changes by using these values to send a so-called `POST` request.

1. **TODO** (Find relevant Room ID and Interaction ID).

2. Connect a [tactile switch](../../components/tactile-switch/tactile-switch.html) to GPIO pin **GP1**.

3. Copy the code below into your `code.py`, then fill in the `ACCESS-KEY` in the URL along with your own `ROOM_ID` and `INTERACTION_ID`. 

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
   SIGNAL_URL = "https://nakama.xrwise.tech:7350/v2/rpc/signal_match?http_key=ACCESS-KEY&unwrap="
   ROOM_ID = "paste-your-room-id-here"
   INTERACTION_ID = 1

   button = digitalio.DigitalInOut(board.GP1)
   button.direction = digitalio.Direction.INPUT

   last_state = False

   # --- Setup
   wifi.radio.connect(secrets["ssid"], secrets["password"])

   pool = socketpool.SocketPool(wifi.radio)
   requests = adafruit_requests.Session(pool, ssl.create_default_context())

   # --- Functions
   def send_signal(interaction_id, payload=None):
       body = {"interactionId": interaction_id, "roomId": ROOM_ID}
       if payload is not None:
           body["payload"] = str(payload)
       response = requests.post(SIGNAL_URL, json=body)
       print("Signal sent:", response.status_code)
       response.close()

   # --- Main loop
   while True:
       pressed = button.value
       if pressed and not last_state:
           print("Button pressed, triggering interaction")
           send_signal(INTERACTION_ID)
       last_state = pressed
       time.sleep(0.05)
   ```

4. Save and press the button: the interaction fires in the AR scene.

{: .note }
If your interaction has **value mode** enabled, it expects a value with every signal, e.g.,`send_signal(INTERACTION_ID, payload=123)`.
