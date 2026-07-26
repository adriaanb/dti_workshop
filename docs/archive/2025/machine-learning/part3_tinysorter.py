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
