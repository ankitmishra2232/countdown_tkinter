import tkinter as tk
from tkinter import font
import time

def start_timer():
    global timer_running
    timer_running = True
    countdown()

def stop_timer():
    global timer_running
    timer_running = False

def reset_timer():
    global time_left
    time_left = 60
    timer_label.config(text="60")

def countdown():
    global time_left
    if timer_running:
        if time_left > 0:
            timer_label.config(text=str(time_left))
            time_left -= 1
            timer_label.after(1000, countdown)
        else:
            timer_label.config(text="Time's up!")
            # play sound or vibration
            # sound.play()
            # vibration.start()

root = tk.Tk()
root.title("Countdown Timer")

# set color scheme
root.config(bg="white")

# set font
customFont = font.Font(family="Helvetica", size=32, weight="bold")

time_left = 60
timer_running = False

# create timer label
timer_label = tk.Label(root, font=customFont, bg="white", fg="black")
timer_label.pack(pady=30)

# create start button
start_button = tk.Button(root, text="Start", font=customFont, bg="green", fg="white", command=start_timer)
start_button.pack(side=tk.LEFT,padx=30)

# create stop button
stop_button = tk.Button(root, text="Stop", font=customFont, bg="red", fg="white", command=stop_timer)
stop_button.pack(side=tk.LEFT,padx=30)

# create reset button
reset_button = tk.Button(root, text="bittuaa", font=customFont, bg="blue", fg="white", command=reset_timer)
reset_button.pack(side=tk.LEFT,padx=30)


root.mainloop()
