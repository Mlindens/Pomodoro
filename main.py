"""
This program implements a simple Pomodoro timer.

This program uses the tkinter library for the GUI. The user interface consists of a timer display,
a start button, a reset button, a display showing whether it's a work session or a break, and
a checkmark display showing the number of work sessions completed.

The program operates in the following sequence:

- Work for 30 minutes
- Short break for 5 minutes
- Repeat the above two steps three times
- After the fourth work session, take a long break of 15 minutes

The user can start the timer, and it will automatically switch between work and break times.
The user can also reset the timer at any point, which will clear the current timer and the checkmarks.

Global Variables:
-----------------
WORK_MIN : int
    Duration of the work session in minutes. Default is 30.
SHORT_BREAK_MIN : int
    Duration of the short break in minutes. Default is 5.
LONG_BREAK_MIN : int
    Duration of the long break in minutes. Default is 15.
REPS : int
    Count of total work and break sessions. Used to determine whether the upcoming session is work, short break,
    or long break.
TIMER : tkinter object
    The timer object used to count down the time. It is controlled by the start_timer() and reset_timer() functions.

Functions:
----------
start_timer():
    Starts the timer for work or break based on the current count of REPS.
count_down(count):
    Recursively counts down from a given number (count) and updates the timer display.
    When the countdown reaches zero, it automatically starts the next timer.
reset_timer():
    Stops the current timer and resets the timer display and the checkmarks.
"""


from tkinter import *
import math

# Global vars
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
REPS = 0
TIMER = None


# Timer function
def start_timer():
    """Starts the timer for work or break based on the current count of REPS."""
    global REPS
    REPS += 1
    # Check for long break
    if REPS % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        top_text.config(text="Long Break", fg=RED)
    # Check for short break
    elif REPS % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        top_text.config(text="Short Break", fg=PINK)
    # Check for work session
    else:
        count_down(WORK_MIN * 60)
        top_text.config(text="Work", fg=GREEN)


# Countdown function
def count_down(count):
    """
    Recursively counts down from a given number (count) and updates the timer display.
    When the countdown reaches zero, it automatically starts the next timer.
    """
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # Adds 0 in front of single digit numbers
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # Update canvas text with minutes and seconds
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    # Count down timer when timer is above 0
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    # Repeat timer and add checkmarks for each work session completed
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            mark += "✓"
        checkmark.config(text=mark)


def reset_timer():
    """Stops the current timer and resets the timer display and the checkmarks."""
    window.after_cancel(TIMER)
    # Reset top text
    top_text.config(text="Timer", fg=GREEN)
    # Reset timer
    canvas.itemconfig(timer_text, text="00:00")
    # Reset checkmarks
    checkmark.config(text="")
    # Reset REPS
    global REPS
    REPS = 0


# Initialize window
window = Tk()
# Set window title
window.title("Pomodoro")
# Set icon
window.iconbitmap("./img/tomato.ico")
# Set window padding
window.config(padx=100, pady=50, bg=YELLOW)

# Set top text format and location
top_text = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
top_text.grid(column=1, row=0)

# Start button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)
# Reset button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

# Checkmark denoting each successful pomodoro session
checkmark = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=2)

# Set canvas for the tomato image
canvas = Canvas(width=360, height=360, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./img/tomato.png")
canvas.create_image(180, 180, image=tomato_img)
# Set timer text format and location
timer_text = canvas.create_text(180, 220, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
