---
layout: default
title: "Machine Learning Introduction"
parent: "2025"
nav_order: 1
has_toc: false
redirect_from:
  - "/part 3 tiny sorter/"
---
# Machine Learning Introduction: "Tiny Sorter"

<div>
  <video autoplay muted loop playsinline style="max-width: 100%; height: auto;">
    <source src="./assets/video0.mp4" type="video/mp4">
  </video>
</div>

Welcome to the “Tiny Sorter” project, an interactive machine learning–enabled sorting machine adapted for the DTI Summer School 2025!

This hands-on module is based on the original [Google Tiny Sorter project](https://experiments.withgoogle.com/tiny-sorter), reworked and documented for your microcontroller workshop using the Raspberry Pi Pico with CircuitPython. The aim of this part is to introduce you to the power of real-time ML-driven decision-making in a physical setup.

**Core idea:**  
A simple, DIY machine will sort objects on a cardboard-based channel, using a webcam and a trained ML model running in your browser. The model recognizes objects and sends commands to control a servo-motor via the Raspberry Pi Pico, directing each object into the correct bin.

## What you will learn

- How simple machine learning models can power tangible hardware projects.
- How to collect and train image data with tools like Google’s Teachable Machine.
- How the browser (ML frontend) and the microcontroller communicate using the Web Serial API.
- Insights into adapting and extending open-source educational projects.

{:.note}
For this workshop, you will receive fully working CircuitPython code for the Raspberry Pi Pico. You do not need to port or rewrite code yourself. If you are interested and have programming experience, you are welcome to explore and modify the provided code as a bonus exercise!

## Materials & Setup

- Raspberry Pi Pico 
- USB cable (Pico ↔ Laptop)
- Servo motor
- Basic DIY materials: cardboard, scissors, tape
- Laptop with a webcam (for the browser ML interface) and with Chrome browser (mandatory)



## Overview

In the upcoming sections we will create the Tiny Sorter Step-by-Step. Here is a quick overview of what we are going to do:

1. [Building](step-1): Build the simple mechanical sorter according to the guide.
2. [Training](step-2): Train  a ML model in your browser to recognize two object classes.
3. [Setup](step-3): Connect your Pico and start the provided Python code, to get everything ready for Sorting.
4. [Testing](step-4): Test and use your Tiny Sorter to sort objects with the power of Machine Learning. There might be some troubleshooting necessary.
5. [Adaption (Bonus)](step-5): Your Tiny Sorter works? Great! Now if you feel up for the task try to modify, adapt or extend the Tiny Sorter.

Happy building and experimenting!


## Next Steps

[Start with Step 1 to build your Tiny Sorter!](step-1){: .btn .btn-blue }.

