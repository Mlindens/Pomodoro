# Pomodoro Timer

This is a simple implementation of a Pomodoro Timer. The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s. The technique uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks. 

![Capture](https://github.com/Mlindens/Pomodoro/assets/83295029/396fc8fd-5e2e-4014-9a1f-b5a5e3fea381)

## Features


- Graphical User Interface using tkinter
- Customizable work, short break, and long break durations
- Automatic switching between work and break sessions
- Displays the number of work sessions completed with checkmarks

## Usage

- Click the "Start" button to begin the timer.
- The timer will automatically switch between work sessions and breaks.
- After every 4 work sessions, a long break will be started.
- Click the "Reset" button at any time to stop the current timer and clear the checkmarks.

## Customization

You can customize the duration of the work sessions, short breaks, and long breaks by modifying the `WORK_MIN`, `SHORT_BREAK_MIN`, and `LONG_BREAK_MIN` variables in the code, respectively. 

## Installation

1. Clone the repository or download the files.
2. Make sure you have Python 3 installed.
3. Run the `pomodoro.py` file to start the program.
