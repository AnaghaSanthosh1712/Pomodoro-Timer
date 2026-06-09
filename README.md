## POMODORO-TIMER

A simple, custom-built tool created to increase the focus time. It helps us to concentrate more and is provided with many other features, running straight from the terminal to keep tasks trackable and distraction-free.

## What It Does 

* **Custom Time:** You just type in how many minutes you want to focus, and the timer starts counting down.
* **Short & Long Breaks:** When your focus time is up, the app asks if you want a **Short Break (5 minutes)** or a **Long Break (15 minutes)** to relax.
* **Keep Going:** If you are in the zone and want to keep working, you can start another round right away without restarting the program.
* **Streak Counter:** It tracks your streak! Every time you finish a focus block, your streak goes up by 1. At the end of the day, you can see exactly how many times you stayed concentrated.
* **Alarm Sound:** It plays an buzzer sound when the timer hits zero so you know your time is up.
  
## Python Concepts Used 

This project was built from scratch to practice core programming logic. Here are the specific features used to make it work:
* **Functions & Recursion:** Uses a main `count()` function that calls itself recursively to handle transitions between focus blocks and breaks smoothly.
* **While Loops:** Uses a `while (x > 0)` loop to handle the live countdown ticking second by second.
* **Basic Math Operators:** Uses Integer Division (`//`) to extract the minutes and the Modulo Operator (`%`) to calculate the remaining seconds.
* **Global Variables:** Uses the `global` keyword to ensure the streak counter updates and persists correctly across different function calls.
* **Terminal Formatting:** Uses the `end="\r"` print parameter to keep the timer refreshing cleanly on a single line instead of scrolling down the screen.
* **Standard Modules:** Imports `time` for the 1-second delays and `winsound` to handle system audio alerts.

## Future Updates 

Here are a few features planned for this project to level up its capabilities:
* **Pause & Stop Keys:** Add a way to safely pause or stop the live ticking clock mid-session without breaking the script execution.
* **Custom Alarm Tones:** Allow users to choose different sound files directly from the terminal menu interface.
* **Visual Progress Bars:** Add a simple loading bar or text graphics that fill up visually as the time passes.
* **Daily History Log:** Save daily streak scores into a simple text file (`.txt`) to track productivity history over a whole week.

## How to Run It 💻

1. Download the script file to your computer.
2. Put any alarm sound clip you like in the same folder and name it `alarm.wav`.
3. Open your terminal or VS Code terminal and run:
   ```bash
   python pomodoro.py
