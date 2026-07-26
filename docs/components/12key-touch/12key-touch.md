---
layout: default
title: "Capacitive Touch (12 Key)"
parent: "Components"
nav_order: 16
---

<img src="assets/12key-touch.png" alt="MPR121 Touch Sensor" width="500"/>

# Capacitive Touch Sensor (MPR121)
<a href="../../glossary/glossary"><img src="../../glossary/assets/input.png" alt="Input" width="72"/></a> <a href="../../glossary/glossary"><img src="../../glossary/assets/iic.png" alt="Digital" width="72"/></a>

This Capacitive Touch Sensor allows you to transform everyday objects into touch interfaces. When you touch any sufficiently conductive material (such as fruit, foil, or even your own body) connected to its pins, the sensor detects a change in capacitance, which you can use to trigger a response in your code. Below is a short example that prints "Touched" to the Serial Monitor whenever any of the sensor's channels detects a change.

Note that the sensor establishes a "baseline" for capacitance when the microcontroller is powered on. If you make any changes to the connected objects' "neutral" state, you will need to restart the microcontroller for the sensor to recalibrate and function correctly.

---

## Basic Usage
```python
# --- Imports
import time
import board
import busio
import adafruit_mpr121

# --- Declarations
i2c_port = busio.I2C(scl=board.GP9, sda=board.GP8)

# --- Functions

# --- Setup
mpr121 = adafruit_mpr121.MPR121(i2c_port, address=0x5b)

# --- Main loop
while True:
    for i in range(12):
        if mpr121[i].value:
            print('Input {} touched!'.format(i))
```

## Advanced Usage with Audio Playback

In this example, we will use the sensor to detect touches to connected produce. Whenever a touch is detected, we will play back an MP3 file with a custom message for each item. This example also relies on the [Mono Speaker & Amplifier Board](../audio-amp-speaker/audio-amp-speaker).

```python
# --- Imports
import time
import board
import busio
import adafruit_mpr121
import audiomp3
import audiopwmio

# --- Declarations
i2c_port = busio.I2C(scl=board.GP7, sda=board.GP6)
mpr121 = adafruit_mpr121.MPR121(i2c_port, address=0x5b)

# --- Variables
audio = audiopwmio.PWMAudioOut(board.GP18)  # Pin GP8 for audio output
mp3_files = ["banana.mp3", "tomato.mp3", "apple.mp3"]  # MP3 files for channels 9, 10, 11
current_file_index = None  # Track the currently playing file

# --- Functions
def play_mp3(file_index):
    global current_file_index, decoder

    if current_file_index == file_index:
        # If the file is already playing, do nothing
        return

    # Stop the current audio if playing
    if audio.playing:
        audio.stop()

    # Close the previous decoder if one exists
    if current_file_index is not None:
        decoder.file.close()

    # Update the current file index
    current_file_index = file_index

    # Print the name of the file being played
    print(f"Now playing: {mp3_files[file_index]}")

    # Open the new MP3 file, create a new decoder, and play it
    decoder = audiomp3.MP3Decoder(open(mp3_files[file_index], "rb"))
    audio.play(decoder)

# --- Main loop
while True:
    # Check touch inputs on channels 9, 10, and 11
    if mpr121[9].value:
        play_mp3(0)  # Play mp3_1.mp3 when channel 9 is touched
    elif mpr121[10].value:
        play_mp3(1)  # Play mp3_2.mp3 when channel 10 is touched
    elif mpr121[11].value:
        play_mp3(2)  # Play mp3_3.mp3 when channel 11 is touched

    # Small delay to avoid rapid cycling
    time.sleep(0.1)
```

