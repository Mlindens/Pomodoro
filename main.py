"""
Simple Pomodoro timer using tkinter
"""

from tkinter import *

# Global vars
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


window = Tk()
# Set window title
window.title("Pomodoro")
# Set window padding
window.config(padx=100, pady=50, bg=YELLOW)
# Set canvas for the tomato image
canvas = Canvas(width=360, height=360, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./img/tomato1.png")
canvas.create_image(180, 180, image=tomato_img)
canvas.create_text(180, 220, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.pack()

window.mainloop()
