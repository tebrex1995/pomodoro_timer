from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#6B9362"
YELLOW = "#f7f5dd"
TIMER_COLOR = "#889375"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=TIMER_COLOR)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 != 0:
        countdown(work_sec)
        timer_label.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break", fg=RED)

    else:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif int(count_sec) < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = time = window.after(1000, countdown, count - 1)
        return str(time)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
            checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Shikamaru's Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


def start():
    print("Start")


def reset():
    print("Reset")


#### LABELS #####

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=TIMER_COLOR, bg=YELLOW)
timer_label.grid(column=1, row=0)
checkmark = Label(font=(FONT_NAME, 25, "bold"), fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

##### CANVAS #####

canvas = Canvas(width=476, height=800, bg=YELLOW, highlightthickness=0)
shikamaru_img = PhotoImage(file="shikamaru.png")
timer_text = canvas.create_text(238, 50, text="25:00", fill=TIMER_COLOR, font=(FONT_NAME, 45, "bold"))
canvas.create_image(225, 380, image=shikamaru_img)
canvas.grid(column=1, row=1)

#####BUTTONS#####

start_button = Button(text="Start", font=("Arial", 16, "bold"), foreground=RED, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", font=("Arial", 16, "bold"), foreground=RED, command=reset_timer)
reset_button.grid(column=4, row=2)
window.mainloop()
