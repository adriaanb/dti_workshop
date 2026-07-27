---
layout: default
title: "Time of Flight Sensor"
parent: "Components"
nav_order: 15
---

<img src="assets/ToF_v1_VL53L0X.png" alt="Time of Flight Sensor Version 1"  width="250"/>

# Time of Flight Distance Sensor
<a href="../../glossary/glossary"><img src="../../glossary/assets/input.png" alt="Input" width="72"/></a> <a href="../../glossary/glossary"><img src="../../glossary/assets/iic.png" alt="I²C" width="72"/></a>

Detects the distance of objects directly in front of the sensor. Works best with white surfaces, for a range from 30 to 1200 mm. Works most reliably between 50 and 950 mm.

Additional information is available on [this page](https://learn.adafruit.com/adafruit-vl53l0x-micro-lidar-distance-sensor-breakout), discussing a similar component based on the same sensor.

Additional code examples are available [here](https://github.com/adafruit/Adafruit_CircuitPython_VL53L0X/tree/main/examples).

---

## Preparation

This Distance Sensor communicates with your microcontroller using a protocol called [I²C](../../glossary/glossary). To work, it must be connected to a port labeled **I²C** on the BitsyExpander Board. You will need to include the `adafruit_bus_device` [library](../../glossary/glossary) in your code to read data via I²C and the `adafruit_vl53l0x` library to control the [VL53L0X](https://www.adafruit.com/product/3317) sensor itself.

These libraries should already be installed on the ItsyBitsy Microcontroller included in your kit, so you don't need to worry about installing them yourself.

{: .highlight }
You can verify that these libraries are installed by ensuring a folder named `adafruit_bus_device` and a file called `adafruit_vl53l0x.mpy` are present in the `lib` folder of your `CIRCUITPY` drive. If not, download Adafruit's Library Bundle for Version 10.x [here](https://circuitpython.org/libraries). Extract the needed file and folder from the bundle and place them in the `lib` folder on your microcontroller. You can learn more about libraries and their use in the [Glossary](../../glossary/glossary) or the [Tutorials](../../tutorials).

## Basic Usage

Make sure to include `busio` and `adafruit_vl53l0x` in the imports section of your code to use the required libraries.  

The first step to using the sensor is setting up the connection by creating an `I2C` [object](../../glossary/glossary) named `i2c_port`. Then, `dist_sensor = adafruit_vl53l0x.VL53L0X(i2c_port)` is used to create an [instance](../../glossary/glossary) of the sensor named `dist_sensor` and connected to `i2c_port`. In the example code below, this is done in the _Variables_ section.

In the main loop, the `print()` function outputs distance readings retrieved from the sensor using `dist_sensor.range`, along with explanatory labels.

{: .highlight }
Two `I2C` ports are available via the Grove Shield. This code example uses **GP6** for the data line (SDA), and **GP7** for the clock (SCL). Another is available on GP8 and GP9.

```python
# --- Imports
import time
import board
import busio
import adafruit_vl53l0x

# --- Declarations
i2c_port = busio.I2C(scl=board.GP7, sda=board.GP6)

# --- Functions

# --- Setup
dist_sensor = adafruit_vl53l0x.VL53L0X(i2c_port)

# --- Main loop
while True:
    print("Range:", dist_sensor.range, "mm")
    time.sleep(0.1)
```

## Additional Resources

### [Working with I²C Devices](https://learn.adafruit.com/working-with-i2c-devices)

Adafruit's extensive learning resource on the I²C standard

### [Resolving I²C Address Conflicts](https://learn.adafruit.com/working-with-multiple-i2c-devices)

Adafruit's guide exploring methods to resolve I²C address conflicts
