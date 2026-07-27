---
layout: default
title: "Part 1 - Scan for Available Networks"
parent: "Connecting To The Internet"
nav_order: 1
redirect_from:
  - "/part 1 tutorials/connecting-to-the-internet/part-1.html"
---

# Part 1 - Scan for Available Networks

The code below shows you how to scan for available networks using your Pi Pico W's inbuilt WiFi module.

1. Connect your Pi Pico W to your computer.

2. Copy the example code below and use `Mu Editor` to save it to your `code.py` file. Remember to back up your old code elsewhere.

3. Open the `Serial Monitor` to verify that your microcontroller can find a network to connect to in the next step.

   ```python
   import wifi
   import time
   
   while True:
       print("\nAvailable Networks:")
       print([network.ssid for network in wifi.radio.start_scanning_networks()])
       wifi.radio.stop_scanning_networks()
       
       time.sleep(10)
   ```

{:.note}
Starting with this tutorial, code examples will include so-called [comments](../../glossary/glossary). Comments exist to document the code and are ignored by the program. They are meant to help you and others understand the code better. In CircuitPython, comments begin with the **`#`** character.

[Next Step](part-2){: .btn .btn-blue }

