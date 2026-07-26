# --- Imports
import digitalio  # Digital input/output control
import board      # Board pin definitions
import neopixel   # Chainable RGB LED control
import time       # Time-related functions (delay, timers)
import random     # Generate random numbers for delay

# --- Variables

# Initialize buttons as digital inputs
red_button = digitalio.DigitalInOut(board.GP1)
red_button.direction = digitalio.Direction.INPUT
blue_button = digitalio.DigitalInOut(board.GP5)
blue_button.direction = digitalio.Direction.INPUT

# Initialize NeoPixel RGB LED strip on GP16 with 6 LEDs
led_pin = board.GP16
num_leds = 6
leds = neopixel.NeoPixel(led_pin, num_leds, auto_write=False, pixel_order=neopixel.GRB)

# Define RGB colors for LED indications
LED_OFF = (0, 0, 0)          # LEDs off
LED_WHITE = (255, 255, 255)  # White light to signal "Go!"
LED_RED = (255, 0, 0)        # Red light for Red player's win
LED_BLUE = (0, 0, 255)       # Blue light for Blue player's win

# Initialize timer variables
countdown_time = 0
countdown_start = 0

# Define game states
STATE_COUNTDOWN = "countdown"
STATE_WAIT_FOR_PRESS = "waiting_for_press"
STATE_WIN = "win"
current_state = STATE_COUNTDOWN

# --- Functions

def set_led_color(color):
    """Set all LEDs to the given RGB color."""
    leds.fill(color)
    leds.show()

def start_countdown():
    """Start random countdown between 3 and 7 seconds."""
    global countdown_time, countdown_start
    countdown_time = random.randint(3, 7)
    countdown_start = time.monotonic()
    print("Get ready...")

def countdown_finished():
    """Check if countdown timer has finished."""
    return time.monotonic() - countdown_start >= countdown_time

# --- Setup

# Turn off LEDs initially
set_led_color(LED_OFF)

# Start the countdown timer
start_countdown()

current_state = STATE_COUNTDOWN

# --- Main Loop

while True:
    if current_state == STATE_COUNTDOWN:
        # Wait until random delay ends
        if countdown_finished():
            set_led_color(LED_WHITE)  # Signal "Go!" with white LEDs
            print("Go! Press your button now!")
            current_state = STATE_WAIT_FOR_PRESS

    elif current_state == STATE_WAIT_FOR_PRESS:
        # Wait for either player's button press
        if red_button.value:
            print("Red wins!")
            set_led_color(LED_RED)
            win_time = time.monotonic()
            current_state = STATE_WIN
        elif blue_button.value:
            print("Blue wins!")
            set_led_color(LED_BLUE)
            win_time = time.monotonic()
            current_state = STATE_WIN

    elif current_state == STATE_WIN:
        # Keep state for 3 seconds, then restart game
        if time.monotonic() - win_time > 3:
            set_led_color(LED_OFF)
            start_countdown()
            current_state = STATE_COUNTDOWN

    time.sleep(0.01)  # Small delay to reduce CPU usage
