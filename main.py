"""
Simple Pomodoro timer using tkinter
"""

from tkinter import *
import math

# Global vars
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# Timer function
def start_timer():
    count_down(5 * 60)


# Countdown function
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# Initialize window
window = Tk()
# Set window title
window.title("Pomodoro")
# Set window padding
window.config(padx=100, pady=50, bg=YELLOW)

# Timer text
top_text = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
top_text.grid(column=1, row=0)

# Start button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)
# Reset button
reset_button = Button(text="Reset")
reset_button.grid(column=2, row=2)

# Checkmark denoting each successful pomodoro session
checkmark = Label(text="✓", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=2)

# Set canvas for the tomato image
canvas = Canvas(width=360, height=360, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./img/tomato1.png")
canvas.create_image(180, 180, image=tomato_img)
timer_text = canvas.create_text(180, 220, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
