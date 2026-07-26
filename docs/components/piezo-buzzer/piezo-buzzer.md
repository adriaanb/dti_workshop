---
layout: default
title: "Piezo Buzzer"
parent: "Components"
nav_order: 8
---

<img src="assets/piezo-buzzer-passive.png" alt="Piezo Buzzer" width="500"/>

# Piezo Buzzer
<a href="../../glossary/glossary"><img src="../../glossary/assets/output.png" alt="Output" width="72"/></a> <a href="../../glossary/glossary"><img src="../../glossary/assets/pwm.png" alt="PWM" width="72"/></a>

Can generate beeping sounds and melodies.

This component is based on [Adafruit's Large Enclosed Piezo Element](https://www.adafruit.com/product/1739).

{:.important}
Make sure your Piezo Element is wired to the **BUZZ** terminals on the Piezo Config Board, as pictured above. If the wires are connected to the **SENSE** terminals, the component is configured as a [Knock Sensor](../knock-sensor/knock-sensor) and cannot be used to generate tones!

{:.highlight}
<img src="assets/piezo-buzzer-passive-old.png" alt="Old Piezo Buzzer"  style="float: right;" width="220"/>An **older version** of the Piezo Buzzer **without** the configuration board is also available. It consists of a piezo element with a resistor in one of its leads, as pictured here. It is functionally identical with the new version and can be used the same way. 

---

## Background

A Piezoelectric Disc is an electronic component commonly used to generate audible signals or alarms in electronic circuits. It converts electrical signals into mechanical vibrations, which we perceive as sound. Conversely, it can also convert mechanical vibrations, knocks, or impacts into electrical signals, allowing it to function as a sensor. Its function is determined by how it is set up electronically.

This article discusses using the Piezoelectric Disc as a buzzer to generate sound.

## Basic Usage

This exampe shows how to create a simple acoustic alarm at a fixed frequency. To use the buzzer, we need to use a technique called **pulse-width modulation** (**`PWM`**) to generate a signal at a certain frequency. To produce `PWM` signals, we use the `pwmio` module, which provides the `pwmio.PWMOut()` method. This method allows us to specify the pin to use and the frequency we want to output.

{:.highlight}
Pins that support **PWM** are denoted by a **`~`** beside their names on the pinout diagram.

`piezo_buzzer = pwmio.PWMOut(board.GP20, frequency=440)` means the buzzer is connected to pin  **GP20** and will be driven at a frequency of 440 Hz, which corresponds to the musical note A4.

In the main loop, we use `piezo_buzzer.duty_cycle` to set the PWM signal's duty cycle. While a 100% duty cycle corresponds to the value `65535`, we use `65535 // 2` to set a duty cycle of 50%. This generates the loudest possible tone, while lower values reduce the volume. To silence the buzzer, we set the duty cycle to `0`.

```python
# --- Imports
import time
import board
import pwmio

# --- Variables
piezo_buzzer = pwmio.PWMOut(board.GP20, frequency=440)

# --- Functions

# --- Setup

# --- Main loop
while True:
    piezo_buzzer.duty_cycle = 65535 // 2
    time.sleep(0.5)
    piezo_buzzer.duty_cycle = 0
    time.sleep(0.5)

```

{:.highlight}

> A PWM signal's duty cycle represents the time the signal is "on" during each repetition. This illustration shows a duty cycle of 10%, meaning the signal is on 10% and off 90% of the time.
>
> <img src="assets/10_pc_duty.gif" alt="10 Percent Duty Cycle Animation" style="mix-blend-mode: darken"/>  



## Playing a Melody

Building on the previous example, let's explore how to create and play back a melody. Instead of defining one fixed tone value, we program a function to play individual tones with a specified frequency, duration, and ensuing pause. We define a melody using an array, where each entry represents a note and its characteristics. In the main loop, we iterate through the melody array, playing each note using the `play_tone` function we have written.

```python
# --- Imports
import time
import board
import pwmio

# --- Variables
piezo_buzzer = pwmio.PWMOut(board.GP20, variable_frequency=True)
duty_cycle_val = 50

# --- Functions
def play_tone(freq, duration, pause):
    piezo_buzzer.frequency = freq
    piezo_buzzer.duty_cycle = duty_cycle_val * 65535 // 100
    time.sleep(duration)           # Duration of note
    piezo_buzzer.duty_cycle = 0    # Off
    time.sleep(pause)              # Pause after note

# --- Setup
melody_ducklings = [
    [262, 0.25, 0], [294, 0.25, 0], [330, 0.25, 0], [349, 0.25, 0], [392, 0.45, 0.05], [392, 0.45, 0.05],
    [440, 0.25, 0], [440, 0.25, 0], [440, 0.25, 0], [440, 0.25, 0], [392, 0.75, 0.25],
    [440, 0.25, 0], [440, 0.25, 0], [440, 0.25, 0], [440, 0.25, 0], [392, 0.75, 0.25],
    [349, 0.25, 0], [349, 0.25, 0], [349, 0.25, 0], [349, 0.25, 0], [330, 0.45, 0.05], [330, 0.45, 0.05],
    [294, 0.25, 0], [294, 0.25, 0], [294, 0.25, 0], [294, 0.25, 0], [262, 0.75, 0.25]
    ]

# --- Main loop
while True:
    for note in melody_ducklings:
        play_tone(note[0], note[1], note[2])

    time.sleep(0.75)
```

The example code above plays back a German nursery rhyme. You can replace the melody array with one of the following ones, representing a French nursery rhyme and a Dutch one, respectively:

```python
melody_jaques = [
    [262, 0.5, 0], [294, 0.5, 0], [330, 0.5, 0], [262, 0.25, 0.25], 
    [262, 0.5, 0], [294, 0.5, 0], [330, 0.5, 0], [262, 0.25, 0.25],
    [330, 0.5, 0], [349, 0.5, 0], [392, 0.75, 0.25], 
    [330, 0.5, 0], [349, 0.5, 0], [392, 0.75, 0.25],
    [392, 0.25, 0], [440, 0.25, 0], [392, 0.25, 0], [349, 0.25, 0], [330, 0.5, 0], [262, 0.25, 0.25],
    [392, 0.25, 0], [440, 0.25, 0], [392, 0.25, 0], [349, 0.25, 0], [330, 0.5, 0], [262, 0.25, 0.25],
    [262, 0.5, 0],[196, 0.5, 0],[262, 0.75, 0.25],
    [262, 0.5, 0],[196, 0.5, 0],[262, 0.75, 0.25]
    ]
```


```python
melody_rijsttafel = [    
    [349, 0.75, 0], [392, 0.75, 0], [262, 0.5, 0],
    [392, 0.75, 0], [440, 0.75, 0], [523, 0.125, 0], [466, 0.125, 0], [440, 0.25, 0],
    [349, 0.75, 0], [392, 0.75, 0], [262, 0.5, 0],
    [262, 0.75, 0.5], [262, 0.125, 0], [262, 0.125, 0], [294, 0.125, 0], [349, 0.25, 0], [349, 0.5, 0]
] 
```

{: .note-title }

> For the musicians amongst you
>
> Both these examples are written to resemble a musical meter called "common time." In this case, the values for duration and pause in each measure (represented as one line in the array formatting) add up to two seconds (where each half second corresponds to a quarter note). You can  consult a [Music Note To Frequency Chart](https://www.google.com/search?q=Music Note to Frequency Chart) to help you use this blueprint to encode your own melody or sheet music into an array.

