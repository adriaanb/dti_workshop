---
layout: default
title: "Part 3 - Get Data from the Internet"
parent: "Connecting To The Internet"
redirect_from:
  - "/part 1 tutorials/connecting-to-the-internet/part-3.html"
---

# Part 3 - Get Data from the Internet

So far, this tutorial has taught you how to configure and connect your Pi Pico W to a WiFi network with internet connectivity. Now, you will learn how to receive data (in this case, corny jokes) over the internet using an [API](../../glossary/glossary). The code example below uses a so-called `REST API`, a common way to exchange data over the internet.

{:.highlight-yellow}
Don't worry if you don't fully understand every step in this tutorial.  By following along and completing the code, you'll begin to recognize  how things like APIs work and how they are used. Even if things remain  unclear for now, what you do here will help you to tackle future  projects and gain a better understanding over time.

Before beginning, ensure your `code.py` file is open in **Mu Editor** and contains the code from [part two](part-2) of the tutorial alongside a valid `sectres.py` file. Only a few changes are needed to enable your code to request data from an online resource:

1. You must import two more modules to establish socket connections and make `HTTP requests`:
   ```python
   # Import modules for establishing socket connections and making HTTP requests
   import ssl
   import adafruit_requests
   ```

2. Below the import statements, provide the address for the API you want request data from:
   ```python
   # URL for the API that will return a random joke
   joke_url = "https://sv443.net/jokeapi/v2/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
   ```

3. To enable the `requests` module to send HTTP requests, you need to set up a socket pool and pass it to the `requests` session. Here’s how to do it:
   ```python
   # Create a socket pool and set up requests
   pool = socketpool.SocketPool(wifi.radio)
   requests = adafruit_requests.Session(pool, ssl.create_default_context())
   ```

4. Replace the existing `while True:` loop with the following one. During each repetition, the code will open an HTTP connection and send a request to the URL specified in step 2. After receiving a response, the joke contained within is formatted and printed to the Serial Monitor before the HTTP connection is closed again. 

   ```python
   while True:
       try:
           print("\nFetching random joke from https://v2.jokeapi.dev/")
           r = requests.get(joke_url)
           joke = r.json()
           print("-" * 40)
   
           # Checking for different types of jokes: either one-liner or setup and delivery
           if "joke" in joke:
               print(joke['joke'])
           else:
               print(joke['setup'])
               time.sleep(3)
               print(joke['delivery'])
   
           print("-" * 40)
           r.close()
       except Exception as e:
           print("Failed to fetch joke. Error:", e)
   
       time.sleep(5)
   ```

   {:.highlight}
   The `try` and `except` structure prevents your program from crashing if something goes wrong when fetching the joke from the API. The program will continue running and attempt to fetch a joke again after a short delay.

5. Save your changes and open Mu Editor's Serial Monitor. If everything went well, your microcontroller will deliver a new, random joke every 5 seconds. Your finished code should look something like this:

   ```python
   import time
   import wifi
   import socketpool
   import ipaddress
   import ssl
   import adafruit_requests
   
   # URL for the API that will return a random joke
   joke_url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
   
   # Get WiFi details from your secrets.py file
   from secrets import secrets
   
   # Connect to WiFi using credentials from the secrets file
   wifi.radio.connect(secrets["ssid"], secrets["password"])
   
   # Create a socket pool and set up requests
   pool = socketpool.SocketPool(wifi.radio)
   requests = adafruit_requests.Session(pool, ssl.create_default_context())
   
   
   while True:
       try:
           print("\nFetching random joke from https://v2.jokeapi.dev/")
           r = requests.get(joke_url)
           joke = r.json()
           print("-" * 40)
   
           # Checking for different types of jokes: either one-liner or setup and delivery
           if "joke" in joke:
               print(joke['joke'])
           else:
               print(joke['setup'])
               time.sleep(3)
               print(joke['delivery'])
   
           print("-" * 40)
           r.close()
       except Exception as e:
           print("Failed to fetch joke. Error:", e)
   
       time.sleep(5)
   ```
