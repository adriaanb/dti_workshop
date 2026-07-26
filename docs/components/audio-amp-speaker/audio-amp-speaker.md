---
layout: default
title: "Mono Speaker"
parent: "Components"
nav_order: 10

---

<img src="assets/audio-amp-speaker.png" alt="Speaker Module" width="500"/>

# Audio Amp & Mono Speaker

<a href="../../glossary/glossary"><img src="../../glossary/assets/output.png" alt="Output" width="72"/></a> <a href="../../glossary/glossary"><img src="../../glossary/assets/digital.png" alt="Digital" width="72"/></a>



---

## Background

The [Adafruit STEMMA Speaker](https://www.adafruit.com/product/3885) board is an easy solution for adding sound to your project. As the name suggests, it features a built-in class D audio amplifier, paired with a compact 1 Watt 8 ohm speaker. This setup provides clear audio output for various applications, whether you're adding sound effects, voice prompts, or simple tunes to your project. 

The examples below show how to use PWM pin **GP9** to play an MP3 file stored on your `CIRCUITPY` drive. You can use services such as [TTSMP3](https://ttsmp3.com/ai) to create short MP3 files with speech prompts.

## Basic Usage



```python
# --- Imports
import board
import audiomp3
import audiopwmio

# --- Variables
audio = audiopwmio.PWMAudioOut(board.GP9)
decoder = audiomp3.MP3Decoder(open("picohello.mp3", "rb"))

# --- Functions

# --- Setup

# --- Main loop
while True:
    audio.play(decoder)
    while audio.playing:
        pass
        
    print("Done playing!")
    
    time.sleep(10)
```



## Advanced Usage

Here, we'll use a button connected to **GP16** to cycle through three MP3 files.

```python
# --- Imports
import board
import audiomp3
import audiopwmio
import digitalio
import time

# --- Variables
audio = audiopwmio.PWMAudioOut(board.GP9)

mp3_files = ["first.mp3", "second.mp3", "third.mp3"]  # List of MP3 files
file_index = 0  # Index to track the current MP3 file

decoder = audiomp3.MP3Decoder(open(mp3_files[file_index], "rb"))

button = digitalio.DigitalInOut(board.GP16)
button.direction = digitalio.Direction.INPUT

# --- Functions
def play_next_mp3():
    global file_index, decoder

    audio.stop()
    decoder.file.close()
    file_index = (file_index + 1) % len(mp3_files)
    
    # Print the name of the file being played
    print(f"Now playing: {mp3_files[file_index]}")

    # Open the next MP3 file and create a new decoder, and play it
    decoder = audiomp3.MP3Decoder(open(mp3_files[file_index], "rb"))
    audio.play(decoder)

# --- Main loop
while True:
    if button.value:
        play_next_mp3()

    # Wait until the current audio file finishes playing
    while audio.playing:
        pass
    
    time.sleep(0.1)  # Small delay to avoid rapid cycling
```
