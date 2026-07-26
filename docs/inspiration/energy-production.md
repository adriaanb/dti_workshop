---
layout: default
title: "Energy Production"
parent: "Inspiration"
nav_order: 4
redirect_from:
  - "/part 2 get creative/idea-4.html"
---

# Idea 4 – Energy Production with Water/Wind (Simulation)

This project is a thought-starter, not a fully guided tutorial. The goal is to get creative with a new component: the **Mini Fan (DC Motor)** and explore how we can simulate concepts like renewable energy.

While we won't actually generate electricity, we can build a model that represents a wind or water turbine. This is a great way to practice connecting inputs to outputs in a meaningful and creative way!

---

## The Concept

The core of this idea is to use the **Mini Fan** to represent a turbine.
- When the fan spins, it simulates the production of energy.
- The faster the fan spins, the more "energy" is being generated.

The challenge is to decide *what* controls the fan's speed. You can connect other sensors to your Pico to create a simple, interactive simulation.

---

## Main Component

The key component for this project is the **Mini Fan (DC Motor)**. It's a simple motor that can be controlled using a PWM (Pulse-Width Modulation) signal from the Raspberry Pi Pico, which allows you to precisely set its rotation speed.

- You can find all the details on how to connect and control it on the [**Mini Fan component page**](https://adriaanb.github.io/dti_workshop/components/mini-fan/mini-fan).

---

## How to Get Started: Some Ideas

This is an open-ended challenge! Here are a few starting points to spark your imagination:

- **Build a Wind Turbine:** Create a simple cardboard structure for your fan. How can you control its speed? Maybe a **Rotary Angle Sensor** acts as a dial to control the "wind speed."
- **Simulate a Hydro Dam:** Use a **Button** to "open the floodgates," making the fan spin at full speed for a few seconds.
- **Create an "intelligent" System:** Connect a **Light Sensor**. The turbine could automatically spin faster during the "day" (when there's more light) and slower at "night."
- **Visualize the Output:** Use the **NeoPixel LED strip** to show how much "energy" is being produced. The more LEDs that light up, the faster the fan is spinning.

---

## Example Code Snippet

This project has no final code, but here is a simple snippet to get you started. This code will make the fan spin at 50% speed for 5 seconds. You can find more details on the [component page](https://adriaanb.github.io/dti_workshop/components/mini-fan/mini-fan).

Remember to save your final script as `code.py`!

```python
# --- Imports
import time
import board
import pwmio

# --- Variables
# Set up a PWM output on a pin (e.g., GP13 - check your Grove shield!)
# The frequency can be between 1000-20000 Hz for this motor
fan_pwm = pwmio.PWMOut(board.GP13, frequency=5000, duty_cycle=0)

# --- Functions
# (You can add your own functions here!)

# --- Setup
print("Starting fan simulation...")
# Set the fan speed to 50%. Duty cycle is a value from 0 (off) to 65535 (full speed)
speed = 0.5
fan_pwm.duty_cycle = int(speed * 65535)

# --- Main loop
# Let it run for 5 seconds, then stop
time.sleep(5)
fan_pwm.duty_cycle = 0 # Stop the fan
print("Simulation finished.")

while True:
    # This is where you could add your own logic, e.g., reading a sensor
    # to control the fan speed in real-time.
    pass
```

---

Have fun bringing your ideas to life and simulating your own power plant!

---

### Need help?


There are several ways for you to get some help with your prototypes:

1. We have trained a custom AI-Agent for you that will help you with any questions. This is especially helpful regarding your python-code:

    [DTI Workshop Helper](https://www.perplexity.ai/search/dti-workshop-helper-T0eH2gNyRM2elfBJcprRJw){: .btn}

2. For references on using specific components, jump to the Components section: 

    [Component Overview](../components/){: .btn}

3. Your workshop instructors are of course happy to help. Don't worry: Go ahead and ask your question.

