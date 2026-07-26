---
layout: default
title: "Step 1 - Build the Tiny Sorter"
parent: "Machine Learning Introduction"
redirect_from:
  - "/part 3 tiny sorter/step-1.html"
---

# Step 1 – Build the Tiny Sorter

Welcome to the first step of your Tiny Sorter project! Here, you’ll build the physical sorting machine that forms the heart of our hands-on ML experience.

The tiny sorter that we are going to build  consists of a chute and a basket, as you can see in this video:

<div>
  <video autoplay muted loop playsinline title="Isometric Shot" style="max-width: 100%; height: auto;">
    <source src="./assets/video_isometric.mp4" type="video/mp4">
  </video>
</div>


## What You’ll Need

Make sure you have these materials ready before you start:

- Raspberry Pi Pico
- Servo motor
- Pre-printed [Tiny Sorter blueprint](assets/blueprint.pdf) (provided by us—no printing required!)
- Scissors
- Tape
- Googly Eyes (mandatory)



---

## Assembly Overview


Start by watching the videos below, which walks you through every step of the assembly process. You will have to:

1. **Cut out all blueprint pieces** and arrange them as instructed.
2. **Score and fold** along the marked lines for neat, crisp edges.
3. **Tape and reinforce** key joints and walls as shown.
4. **Assemble the chute and basket**, ensuring correct orientation (see video).
5. **Attach the servo motor** in the pre-scored bracket (matches the provided servo shape).

{:.highlight}
**Tip:**  
Take your time on the cutting and folding steps. Accurate and clean work makes a big difference for a smooth-running Tiny Sorter!



## 1. Cut it out
<div>
  <video autoplay muted loop playsinline title="Cut Out" style="max-width: 100%; height: auto;">
    <source src="./assets/video1.mp4" type="video/mp4">
  </video>
</div>

## 2. Fold it up
<div>
  <video autoplay muted loop playsinline title="Fold it up" style="max-width: 100%; height: auto;">
    <source src="./assets/video2.mp4" type="video/mp4">
  </video>
</div>

{:.note}
In this shot, they are using a pencil to crease the paper and make it easier to fold. This is highly recommended.

## 3. Tape it together
<div>
  <video autoplay muted loop playsinline title="Tape it together" style="max-width: 100%; height: auto;">
    <source src="./assets/video3.mp4" type="video/mp4">
  </video>
</div>

{:.note}
The video shows how to build the sorter using an Arduino (a different microcontroller similar to our Raspberry Pi Pico ). Focus now on building the physical parts — connection differences are explained in a later step.

## 4. Connect it
<div>
  <video autoplay muted loop playsinline title="Connect it" style="max-width: 100%; height: auto;">
    <source src="./assets/video4.mp4" type="video/mp4">
  </video>
</div>

{:.note}
Plug the servo motor into GP5.

## 5. Upload the Code
You need two files on your Pi PicO:
1. The first one that needs to be created is `boot.py`:

```python
import usb_cdc
    usb_cdc.enable(console=True, data=True)
```

2. The main file is `code.py`:

```python
import time
import board
import pwmio
from adafruit_motor import servo
import usb_cdc

# === CONFIGURATION (You CAN change these settings) ===
SERVO_PIN = board.GP5  # <--- Change to your correct pin
IDLE_START = 60        # Idle movement: start angle (degrees)
IDLE_END = 90          # Idle movement: end angle (degrees)
IDLE_SPEED = 0.025     # Delay time for idle movement (seconds) - lower is faseter


# === SETUP (leave unchanged unless you know what you're doing) ===
servo_pwm = pwmio.PWMOut(SERVO_PIN, frequency=50)
sorter_servo = servo.Servo(servo_pwm, min_pulse=500, max_pulse=2500)
sorter_servo.angle = (IDLE_START + IDLE_END) // 2  # start in the middle position

serial = usb_cdc.data  # USB Serial 'Data channel' for Web Serial API

def write_status(msg):
    """Send status message to the browser console (Web Serial)."""
    serial.write(bytes(msg + '\r\n', 'utf-8'))

def reset_serial_buffer(serial):
    """Clear all pending bytes from the serial buffer."""
    while serial.in_waiting > 0:
        serial.read(1)


# === MAIN LOOP ===
while True:
    if serial.in_waiting > 0:
        cmd = serial.read(1)
        if not cmd:
            continue
        command = cmd[0]
        print("Received command:", command)  # For debugging via Mu/Thonny Serial

        if command == 1:
            # --- SORT: Class 1 detected ---
            sorter_servo.angle = 0
            write_status('class 1 detected')
            time.sleep(2)
            for angle in range(0, 76, 1):
                sorter_servo.angle = angle
                time.sleep(0.05)
            time.sleep(1)
            reset_serial_buffer(serial)  # Discard any extra repeated signals

            # --- WORKSHOP EXTENSION ---
            # Place any code here that should run EACH TIME the sorter detects class 1.
            # e.g. increment a counter, update a display, etc.

        elif command == 2:
            # --- SORT: Class 2 detected ---
            sorter_servo.angle = 180
            write_status('class 2 detected')
            time.sleep(2)
            for angle in range(180, 74, -1):
                sorter_servo.angle = angle
                time.sleep(0.02)
            time.sleep(1)
            reset_serial_buffer(serial)

            # --- WORKSHOP EXTENSION ---
            # Place any code here that should run EACH TIME the sorter detects class 2.

        # If command == 0 or any other value, do nothing special
        # The idle movement continues below

    else:
        # --- IDLE ANIMATION: gently move sorter arm back and forth when no sort is active ---
        for angle in range(IDLE_START, IDLE_END + 1, 1):
            sorter_servo.angle = angle
            time.sleep(IDLE_SPEED)
        for angle in range(IDLE_END, IDLE_START - 1, -1):
            sorter_servo.angle = angle
            time.sleep(IDLE_SPEED)
        # Idle animation: lets everyone see the actuator is ready and responsive

# === END OF FILE ===

```

---

## When You're Done

When your sorter has been assembled, set it aside for Step 3, where we will connect the electronics and run the code. But before, we will train the ML Model in Step 2.


[Continue with Step 2 to train the ML Model!](step-2){: .btn .btn-blue }.


---

*This page and materials are adapted for the Summer School DTI 2025 based on the original assembly guides and resources by Google’s Tiny Sorter project. Videos embedded here remain the property of Google Experiments.*



