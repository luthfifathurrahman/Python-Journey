from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
checkmark_count = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global reps, checkmark_count
    checkmark_count = 0 # reset checkmark_count
    reps = 0 # reset reps count
    window.after_cancel(timer) # reset countdown
    window.config(bg=YELLOW) # reset window
    canvas.config(bg=YELLOW) # reset canvas
    checkmark_label.config(text="", bg=YELLOW) # reset checkmark label
    pomodoro_label.config(text="POMODORO", bg=YELLOW, fg=GREEN) # reset pomodoro label
    canvas.itemconfig(timer_text, text="00:00") # reset timer label


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, checkmark_count
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 9:
        timer_reset()
    elif reps == 8:
        countdown(long_break_sec)
        window.config(bg=YELLOW)
        canvas.config(bg=YELLOW)
        checkmark_label.config(bg=YELLOW)
        pomodoro_label.config(text="LONG BREAK",
                              font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
        checkmark_count = 4
        checkmark_text = checkmark_count * "✔"
        checkmark_label.config(text=f"{checkmark_text}")
    elif reps % 2 == 0:
        countdown(short_break_sec)
        window.config(bg=YELLOW)
        canvas.config(bg=YELLOW)
        checkmark_label.config(bg=YELLOW)
        pomodoro_label.config(text="SHORT BREAK",
                              font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
        checkmark_count += 1
        checkmark_text = checkmark_count * "✔"
        checkmark_label.config(text=f"{checkmark_text}")
    else:
        countdown(work_sec)
        window.config(bg=PINK)
        canvas.config(bg=PINK)
        checkmark_label.config(bg=PINK)
        pomodoro_label.config(text="WORK",
                              font=(FONT_NAME, 40, "bold"), bg=PINK, fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window =Tk()
window.title("Pomodoro") # title name
window.config(padx=100, pady=50, bg=YELLOW)

# POMODORO LABEL
pomodoro_label = Label(text="POMODORO",
                       font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
pomodoro_label.grid(column=1, row=0)

# TOMATO
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# START BUTTON
start_button = Button(text="Start", width=10, font=(FONT_NAME, 10), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# RESET BUTTON
reset_button = Button(text="Reset", width=10, font=(FONT_NAME, 10), highlightthickness=0, command=timer_reset)
reset_button.grid(column=2, row=2)

# CHECKMARK
checkmark_label = Label(text="", font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)



window.mainloop()