---
layout: default
title: "Grove Shield"
parent: "Components"
nav_order: 1
---

<img src="assets/pico-grove-shield.png" alt="Grove Shield" width="400"/>

# Grove Shield for Pi Pico

Expands the capabilities of your microcontroller by providing solderless Grove connectors.

---

### Features

* 10 Grove Headers
  - 3 Digital Headers
  - 2 I2C Headers that also serve as Digital Headers
  - 2 UART Headers that also serve as Digital Headers
  - 3 Analog Headers A0, A1, A2 (A1 and A2 are shingled)
* WiFi Radio

> NOTE: In shingled pin headers, each header's second pin is shared with the first pin in the header above it. Therefore, using one disables the other. For instance, using pins A0 and A1 in the  A1-labeled header disallows the use of A0 in the A0-labeled header.



![Pinout Diagram](assets/pi-pico-w-pinout.jpg)
