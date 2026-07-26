---
layout: default
title: "Motion Sensor"
parent: "Components"
nav_order: 14
---

<img src="assets/grove-pir.png" alt="Grove Motion Sensor" width="250"/>

# Motion Sensor
<a href="../../glossary/glossary"><img src="../../glossary/assets/input.png" alt="Input" width="72"/></a> <a href="../../glossary/glossary"><img src="../../glossary/assets/digital.png" alt="Digital" width="72"/></a>

This PIR Motion Sensor is designed to detect human motion by measuring infrared radiation emitted by objects in its field of view. It operates as a digital component, making it simple to use in code. If the sensor value you read is `True`, a motion is being detected. `False` means no motion is detected.   

The sensor has a detecting angle of 100 degrees and can sense motion at distances ranging from 3.2 meters to 12 meters.

---

## Basic Usage
```python
# --- Imports
import digitalio
import time
import board

# --- Variables
motion_sensor = digitalio.DigitalInOut(board.GP16)
motion_sensor.direction = digitalio.Direction.INPUT

# --- Functions

# --- Setup

# --- Main loop
while True:
    if motion_sensor.value == True:
        print("A Motion has occured")
    else:
        print("Nothing...")
        
    time.sleep(0.1)
```

