---
layout: default
title: "Bonus: Reaction Game"
parent: "Tutorials"
nav_order: 5
redirect_from:
  - "/part 1 tutorials/bonus/"
---


# Bonus: Reaction Game

On this page, you can find the code for a simple reaction game. 

This basic game makes use of two digital input components (for instance, a Tactile Switch), and an RGB LED as an output.

Once the LED turns white, both players have to try and touch their sensor as quick as possible. Whoever is faster wins the round, and the LED will  light up in the corresponding color (red or blue).

Try to see if you can understand the code and build a prototype that makes use of it. Feel free to use it as a basis for modification, creating your own game logic and behavior.


```python
##--- Imports
import digitalio
import board
import neopixel
import time
import random

##--- Variables
state_wait = 0
state_start_game = 1
state_wait_button_press = 2
state_red_wins = 3
state_blue_wins = 4
current_state = 0

# Button variables
red_pin = board.GP1
red_button = digitalio.DigitalInOut(red_pin)
red_button.direction = digitalio.Direction.INPUT

blue_pin = board.GP5
blue_button = digitalio.DigitalInOut(blue_pin)
blue_button.direction = digitalio.Direction.INPUT

# For the Chainable LED:
pin_leds = board.GP20
num_leds = 6
leds = neopixel.NeoPixel(pin_leds, num_leds, auto_write=False, pixel_order=neopixel.GRB)

led_off = (0, 0, 0, 0)
led_red = (255, 0, 0, 0)
led_blue = (0, 0, 255, 0)
led_white = (0, 0, 0, 255)

# Timer variables
timer_duration = 0
timer_mark = 0

##--- Functions
def set_led_color(color):
    global leds
    leds.fill(color)
    leds.show()

def set_timer(duration):
    global timer_duration, timer_mark
    timer_duration = duration
    timer_mark = time.monotonic()

def timer_expired():
    global timer_mark, timer_duration
    if time.monotonic() - timer_mark > timer_duration:
        return True
    else:
        return False

##--- Main loop
while True:
    if current_state == state_wait:
        set_led_color(led_off)
        set_timer(random.randint(3, 10))
        print("starting game!")
        current_state = state_start_game

    elif current_state == state_start_game:
        if timer_expired():
            print("timer expired, press your buttons!")
            set_led_color(led_white)
            current_state = state_wait_button_press

    elif current_state == state_wait_button_press:
        if red_button.value:
            print("red won")
            current_state = state_red_wins
        elif blue_button.value:
            print("blue won")
            current_state = state_blue_wins

    elif current_state == state_blue_wins:
        set_led_color(led_blue)
        time.sleep(3)
        current_state = state_wait

    elif current_state == state_red_wins:
        set_led_color(led_red)
        time.sleep(3)
        current_state = state_wait
```

{:.note}
The original source of this reaction game code can be found [here](https://id-studiolab.github.io/Digital-Interfaces/assignments/01-reaction-game-discover/).
