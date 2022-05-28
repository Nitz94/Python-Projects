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
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(str(timer))  # changed to str because pycharm expects str
    canvas.itemconfig(timer_text, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    app_label.config(text="Timer", fg=RED, bg=GREEN, font=(FONT_NAME, 35, "bold"))
    check_marks.config(fg=PINK, bg=GREEN, font=(FONT_NAME, 12, "bold"))

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # if its 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        app_label.config(text="BREAK", fg=RED, bg=GREEN, font=(FONT_NAME, 35, "bold"))
    # if its 2nd/4th/6th rep:
    elif reps % 2 == 0:
        app_label.config(text="BREAK", fg=PINK, bg=GREEN, font=(FONT_NAME, 35, "bold"))
        count_down(short_break_sec)
    # if its 1st/3rd/5th/7th rep:
    else:
        app_label.config(text="WORK", fg=YELLOW, bg=GREEN, font=(FONT_NAME, 35, "bold"))
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"  # dynamically changing the data types to fit our requirement
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    # config a particular canvas and particular item in that canvas. here we're changing text to count

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "✔"
            check_marks.config(text=marks, fg=PINK, bg=GREEN, font=(FONT_NAME, 12, "bold"))

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=GREEN)


canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)  # creating a canvas to place image
tomato_img = PhotoImage(file="tomato.png")  # photo image class reads the image location,and it is saved to a variable
canvas.create_image(100, 112, image=tomato_img)  # image is placed at the specified position
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


app_label = Label(text="Timer", fg=RED, bg=GREEN, font=(FONT_NAME, 35, "bold"))
app_label.grid(column=1, row=0)

check_marks = Label(fg=PINK, bg=GREEN, font=(FONT_NAME, 12, "bold"))
check_marks.grid(column=1, row=3)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)














window.mainloop()









