---
layout: default
title: "Step 3 - Setup"
parent: "Machine Learning Introduction"
redirect_from:
  - "/part 3 tiny sorter/step-3.html"
---

# Step 3 - Setup

{:.highlight}
Follow these steps to set up your Tiny Sorter. The process is also shown in the video below.

<div>
  <video autoplay muted loop playsinline title="Setup Video" style="max-width: 100%; height: auto;">
    <source src="./assets/setup.mp4" type="video/mp4">
  </video>
</div>

- **Mount the Tiny Sorter in front of the webcam**  
 Place your Tiny Sorter so that the objects and the sorter arm are clearly visible to the camera.

- **Connect the servo motor to GP5 on the Pico**  
  Plug the signal wire of your servo motor into GPIO pin GP5 on the Raspberry Pi Pico. (For Grove A1, use GP27 instead – see the glossary.)

- **Connect the Raspberry Pi Pico to your laptop via USB**  
  - Check that your Pico is physically connected to your computer.
  - Make sure the CircuitPython code for the sorter is saved as `code.py` on your Pico drive.
  - Also confirm that a `boot.py` file is present on the Pico with these contents:
    ```
    import usb_cdc
    usb_cdc.enable(console=True, data=True)
    ```
    *(Edit this only if needed—this file should **not** be part of `code.py`.)*

- **Open the Tiny Sorter web app**  
  Use Google Chrome and go to:  
  [https://editor.p5js.org/heinrichkortsch/full/FG6GUcCSO](https://editor.p5js.org/heinrichkortsch/full/FG6GUcCSO)

- **Paste your Teachable Machine model link in the web app**  
  - Export your model from Teachable Machine and copy the provided URL.
  - Paste the link into the input field in the web app.  
  - If the model loads successfully, you’ll see the names of your two trained classes appear in the interface.

- **Close the Mu Editor (or any other serial/REPL application)**  
  - Be sure the Mu Editor (and any other serial or REPL programs) are fully closed.
  - If Mu or Thonny is open, they block the serial port and prevent the web app from connecting to the Pico.

- **Connect the Pico using the web app**  
  - Click the “CONNECT PICO” button in the app.
  - In the device dialog, choose **the device with the higher number at the end** (e.g. `usbmodem12303`) – this is the Data Channel.
  - If unsure, just select the higher-numbered option for data communication.

- **Align everything**  
  - Make sure the Tiny Sorter and your sorting objects are lined up correctly with the webcam so the machine learning model gets a clear, unobstructed view.

- **All done!**  
  - You are now set: present objects for sorting and watch how the web interface responds with live feedback from your model and Pico.

{:.highlight}
**Tip:**  
If something doesn’t work, check all connections, use Chrome(!), close Mu-Editor, and make sure both `code.py` and `boot.py` exist on the Pico.

The Setup is all done? Let's test your Tiny Sorter.



[Continue with step 4 to test and use  your Tiny Sorter!](step-4){: .btn .btn-blue }.