---
layout: default
title: "Step 4 - Test your Tiny Sorter"
parent: "Machine Learning Introduction"
redirect_from:
  - "/part 3 tiny sorter/step-4.html"
---

# Step 4 - Test your Tiny Sorter

It is time to test your Tiny Sorter! After completing the setup in Step 3, you should be ready to go.

The video below shows the Tiny Sorter in action:

<div>
  <video autoplay muted loop playsinline title="Testing Video" style="max-width: 100%; height: auto;">
    <source src="./assets/testing.mp4" type="video/mp4">
  </video>
</div>

Using the [Web Serial API](https://developer.chrome.com/docs/capabilities/serial/), the machine learning model running in your web app sends class predictions to the Pico, which moves the servo to sort objects accordingly.

---

## ❌ Your Tiny Sorter doesn't work?

**Try these troubleshooting steps:**

- **Check connections:**  
  - Is the Pico firmly attached to the laptop via USB?
  - Is the servo plugged into the correct pin (e.g., GP5 or GP27 for Grove A1)?
  - Are all jumper wires or Grove connectors seated properly?
- **Is `code.py` on your Pico?**  
  - Make sure the MicroPython/CircuitPython script is saved as `code.py`.  
  - Also ensure `boot.py` exists and enables the serial data channel as shown in Step 3.
- **Serial port blocked?**  
  - Close the Mu Editor, Thonny, or any other program that might be using the Pico’s serial port.
- **Browser issues:**  
  - Are you using Google Chrome? Other browsers might not support the Web Serial API.
  - Did you grant camera permissions and select the correct device in the connection dialog (choose the higher-numbered device for the Data Channel)?
- **Model not loading?**  
  - Double-check the Teachable Machine model link. Paste it again, and ensure you see your trained class names in the app.
- **No movement at all?**  
  - Check the servo’s power–some servos require more current than USB provides.
  - Make sure the servo hasn’t been physically blocked and can move freely.
- **Still not working?**  
  - Reload the web app; unplug and replug the Pico and try again.

If you are stuck, ask your workshop instructors.

---

## ✅ Your Tiny Sorter works?

Excellent!  
You have successfully built and tested your Tiny Sorter. 🚀

---

[Continue with Step 5 (optional) to modify, adapt or extend your Tiny Sorter!](step-5){: .btn .btn-blue }
