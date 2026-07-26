# Schreibe hier Deinen Code :-)

# --- Imports
import digitalio
import board
import time

# --- Variables

# Set up the PIR motion sensor as INPUT (detects movement)
pir_pin = board.A2
pir_sensor = digitalio.DigitalInOut(pir_pin)
pir_sensor.direction = digitalio.Direction.INPUT

# Set up the buzzer as OUTPUT (makes sound)
buzzer_pin = board.A0
buzzer = digitalio.DigitalInOut(buzzer_pin)
buzzer.direction = digitalio.Direction.OUTPUT

# --- Functions
# (No functions needed for this simple version.)

# --- Setup
# (All setup is already done in the Variables section.)

# --- Main loop
while True:
    # Check if motion sensor detects movement (INPUT)
    if pir_sensor.value:
        print("Motion detected! Alarm sounding!")
        # Beep the buzzer quickly for about 5 seconds
        for i in range(50):
            buzzer.value = True     # OUTPUT: Turn buzzer ON
            time.sleep(0.05)        # Wait 0.05 seconds
            buzzer.value = False    # OUTPUT: Turn buzzer OFF
            time.sleep(0.05)
        print("Alarm reset. Monitoring resumed.")
        time.sleep(1)              # Wait before next check (prevents immediate retrigger)
    else:
        buzzer.value = False        # Make sure buzzer stays OFF
        time.sleep(0.1)             # Short delay before checking again

