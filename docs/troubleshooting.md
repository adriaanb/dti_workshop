---
layout: default
title: "Troubleshooting"
nav_order: 7
---

# Troubleshooting

Something is not working as expected? Not to worry, that is a normal part of building things. Here are some of the most common problems and things you can try to address them:

## I saved my code but nothing happens

**Check the file name.** Your program has to be saved as `code.py` on the `CIRCUITPY` drive. CircuitPython also accepts `main.py`, but everything in this workshop uses `code.py`. A file with any other name is simply stored on the drive and never runs.

**Restart the program.** In the serial monitor, press:

- **Ctrl + C** to stop the running program
- **Ctrl + D** to restart it

**Unplug and plug the board back in.** Restarting with Ctrl + D re-runs your code, but it does not reset the hardware. If a sensor was left in use by the previous run, it stays that way until the board loses power. This is the fix when a sensor worked once and then stopped being found.

## ImportError: no module named ...

Your code is asking for a library that is not on the board. Open the `lib` folder on your `CIRCUITPY` drive and check whether the file or folder named in the error is there.

If it is missing, download the [Adafruit CircuitPython Library Bundle](https://circuitpython.org/libraries) for version 10.x, find the file in it, and copy it into `lib`.

{: .note }
Not everything lives in `lib`. Modules like `board`, `time`, `digitalio`, `busio` and `analogio` are built into CircuitPython itself, so they are always available and never need copying.

## How do I read an error message?

When something goes wrong, the serial monitor prints a few lines that look intimidating but are mostly helpful. Read them from the **bottom up**:

```text
Traceback (most recent call last):
  File "code.py", line 14, in <module>
NameError: name 'buton' is not defined
```

- The **last line** says what went wrong: `buton` is not a name the program knows, so it is probably a typo for `button`.
- The **line above** says where: line 14 of `code.py`.

Two of the most common ones:

- `NameError` - a name is misspelled, or used before it was created
- `IndentationError` - the spaces at the start of a line do not line up

## Still stuck?

Ask the [AI Assistant](ai-assistant.html) and paste the exact error message, or ask your workshop instructors.
