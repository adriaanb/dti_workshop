---
layout: default
title: "Part 2 - Connect to a WiFi Network"
parent: "Connecting To The Internet"
redirect_from:
  - "/part 1 tutorials/connecting-to-the-internet/part-2.html"
---

# Part 2 - Connect to a WiFi Network

To connect your Pi Pico W to a network, you must provide a network name (SSID) and password. However, directly using sensitive data like WiFi passwords in your code is risky. Therefore, creating a separate file to hold your personal keys and passwords outside your `code.py` file is a good idea. This way, you can share your code without revealing sensitive data to others.

1. Begin by clicking the **`+`** icon labeled **New** in the top toolbar of Mu Editor.

2. Copy and paste the following code to the new file, replacing `network-name` with the name of your WiFi network and `network-passwd` with your network's password.

   ```python
   secrets = {
       "ssid": "network-name",
       "password": "network-passwd"
   }
   ```

3. Click the **Save** button in the toolbar and save the file on your `CIRCUITPY` drive using the name `secrets.py`.

4. Enter your `code.py` file and replace the code you wrote in [part one](part-1) with the code below, then hit **Save**.

   ```python
   import time
   import wifi
   import socketpool
   import ipaddress
   
   # Get WiFi details from your secrets.py file
   from secrets import secrets
   
   # Connect to WiFi using credentials from the secrets file
   wifi.radio.connect(secrets["ssid"], secrets["password"])
   
   pool = socketpool.SocketPool(wifi.radio)
   
   print()
   print("WiFi connection established.")
   print("My MAC addres is:", ":".join("{:02X}".format(byte) for byte in wifi.radio.mac_address))
   print("My IP address is", wifi.radio.ipv4_address)
   print()
   print("Pinging google.com at IP address 8.8.4.4")
   
   while True:    
       ipv4 = ipaddress.ip_address("8.8.4.4")
       response = wifi.radio.ping(ipv4)
         
       if response is None:
           print(f"Ping failed. No response.")
       else:
           print(f"Ping successful. Response time: {response} ms")
       
       time.sleep(2)
   ```
   
5. Open Mu's `Serial Monitor` to verify that the microcontroller successfully connects to the chosen network and can get a response from `google.com`.

6. Note the differences from the code you encountered in [part one](part-1) of this tutorial:

      - An `import` statement for your newly created `secrets.py` file has been added. This gives the code access to the network name (SSID) and password.
      - The content of the `while True:` loop has been replaced: It now pings google.com and reports the response time. This confirms internet connectivity for your microcontroller.

[Next Step](part-3){: .btn .btn-blue }
