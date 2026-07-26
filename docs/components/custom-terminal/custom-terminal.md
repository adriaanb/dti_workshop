---
layout: default
title: "Custom Screw Terminal"
parent: "Components"
nav_order: 18
---

<img src="assets/custom-terminal.png" alt="Custom Terminal" width="250"/>

# Custom Screw Terminal
<a href="../../glossary/glossary"><img src="../../glossary/assets/input.png" alt="Input" width="72"/></a> 

This component allows you to connect your own sensors to it. 

You can use it as an  <a href="../../glossary/glossary"><img src="../../glossary/assets/analog.png" alt="Analog" width="72"/></a>  component by connecting a variable resistor between the terminals: A thermistor will turn it into a temperature sensor, a photoresistor into a light sensor. But you can also connect something like [conductive rubber band](https://www.adafruit.com/product/519) to turn it onto a stretch sensor.

You can also use it as a  <a href="../../glossary/glossary"><img src="../../glossary/assets/digital.png" alt="Digital" width="72"/></a>  component by building a custom switch: Use any two conductive objects and connect one to either screw terminal. As soon as they touch each other or are bridged by a third conductive object, you can read that like a closed switch!

---

## Basic photo resistor example
```python
# --- Imports
import time
import board
import analogio

# --- Variables
# Initialize analog input connected to photo resistor
photo_resistor = analogio.AnalogIn(board.A1)

# --- Functions

# --- Setup

# --- Main loop
while True:
    val = photo_resistor.value # Read the photo resistor value
    print(val) # Output the value in the serial monitor
    time.sleep(0.05)  # Make the loop run a little bit slower
```
