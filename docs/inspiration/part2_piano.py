# --- Imports
import time
import board
import busio
import adafruit_mpr121
import audiomp3
import audiopwmio

# --- Declarations
# Initialize I2C for the capacitive touch sensor (adjust pins to your setup, in this case it is the Grove Connector labeled I2C1)
i2c_port = busio.I2C(scl=board.GP7, sda=board.GP6)
mpr121 = adafruit_mpr121.MPR121(i2c_port, address=0x5b) # do not change this

# --- Variables
# Setup mono audio output on GP18 using a proper amplifier/speaker
audio = audiopwmio.PWMAudioOut(board.GP18)
mp3_files = ["C.mp3", "D.mp3", "E.mp3"]  # MP3 filenames for channels 0, 1, 2, these files need to be stored as .mp3 files on your pico
current_index = None  # Needed to track which file is playing

# --- Functions
def play_mp3(index):
    """
    What does this function do? ->
    Play the MP3 file for the given index if not already playing.
    Stops any previous playback, closes old files, prevents duplicates.
    """
    global current_index, decoder

    if current_index == index and audio.playing:
        return
    if audio.playing:
        audio.stop()
    if current_index is not None:
        decoder.file.close()
    current_index = index
    print(f"Playing {mp3_files[index]}")
    decoder = audiomp3.MP3Decoder(open(mp3_files[index], "rb"))
    audio.play(decoder)

# --- Setup
# (Nothing extra needed – all config is above.)

# --- Main loop
while True:
    # Check the first three touch channels and play a note if one is touched
    if mpr121[0].value:
        play_mp3(0)   # Play C.mp3 when channel 0 is touched
    elif mpr121[1].value:
        play_mp3(1)   # Play D.mp3 when channel 1 is touched
    elif mpr121[2].value:
        play_mp3(2)   # Play E.mp3 when channel 2 is touched
    time.sleep(0.1)
