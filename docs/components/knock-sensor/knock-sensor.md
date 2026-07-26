---
layout: default
title: "Knock Sensor"
parent: "Components"
nav_order: 9

---

<img src="assets/knock-sensor.png" alt="Knock Sensor" width="500"/>

# Knock Sensor

<a href="../../glossary/glossary"><img src="../../glossary/assets/input.png" alt="Input" width="72"/></a> <a href="../../glossary/glossary"><img src="../../glossary/assets/analog.png" alt="Analog" width="72"/></a>

Can detect knocks and impacts.

This component is based on [Adafruit's Large Enclosed Piezo Element](https://www.adafruit.com/product/1739).

{:.important}
Make sure your Piezo Element is wired to the **SENSE** terminals on the Piezo Config Board, as pictured above. If the wires are connected to the **BUZZ** terminals, the component is configured as a [Piezo Buzzer](../piezo-buzzer/piezo-buzzer) and cannot be used as a sensor!

{:.highlight-yellow}
<img src="assets/knock-sensor-old.png" alt="Old Knock Sensor"  style="float: right; margin: 10px 0px;" width="220"/>An **older version** of the Knock Sensor **without** the configuration board is also available. It consists of a piezo element with a resistor across its leads, as pictured here. If handled carelessly it can cause damage to the microcontroller. Whenever possible, favor the **newer version**, especially for long-term projects.




---

## Background

A Piezoelectric Disc is an electronic component commonly used to generate audible signals or alarms in electronic circuits. It converts electrical signals into mechanical vibrations, which we perceive as sound. Conversely, it can also convert mechanical vibrations, knocks, or impacts into electrical signals, allowing it to function as a sensor. Its function is determined by how it is set up electronically.

This article discusses using the Piezoelectric Disc as a sensor to detect knocks and impacts.

## Basic Usage

The code example below reads the value from a piezoelectric sensor connected to pin **A1** on each run through the main loop. If the sensor detects an impact with a value greater than the defined threshold of 1000, it prints a message along with the sensor's reading to the Serial Monitor. The loop pauses briefly after each check to prevent overwhelming the output.

```python
# --- Imports
import time
import board
import analogio

# --- Variables
detect_threshold = 1000
knock_sensor = analogio.AnalogIn(board.A1)

# --- Functions

# --- Setup

# --- Main loop
while True:
    if knock_sensor.value > detect_threshold:
        print(f"Knock! ({knock_sensor.value})")
    time.sleep(0.1)

```



## Using Debounce to Filter Out Unwanted Knocks

In this code example, debouncing is used to prevent multiple detections of the same knock. Debouncing works by introducing a short delay between valid knock detections, filtering out any triggers that happen too quickly to be intentional.

To achieve this, we use `time.monotonic()` to get the number of seconds (as a floating-point number) that have elapsed since the microcontroller was powered on. On each run through the main loop, the conditions `sensor_value >= detect_threshold` and `(current_time - last_knock_time) > debounce_time` are checked to ensure the sensor value exceeds the threshold and that enough time has passed since the last knock before registering a new one.

```python
# --- Imports
import time
import board
import analogio

# --- Variables
detect_threshold = 1000
debounce_time = 0.4  # 400 ms debounce time
knock_sensor = analogio.AnalogIn(board.A1)
last_knock_time = 0

# --- Functions

# --- Setup

# --- Main loop
while True:
    current_time = time.monotonic()
    sensor_value = knock_sensor.value

    if sensor_value >= detect_threshold and (current_time - last_knock_time) > debounce_time:
        print(f"Knock! ({sensor_value})")
        last_knock_time = current_time  # Update the time of the last valid knock

    time.sleep(0.01)
```
