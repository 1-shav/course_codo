import tkinter as tk
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
REPS = 0
CHECKS = 0
TIMER = None
STARTED = False
STOPPED = False
TIMER_RN = 0
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():

    global REPS
    global CHECKS
    global STARTED
    global STOPPED

    screen.after_cancel(TIMER)
    head_chahiye.config(text="pawmodoro", fg=GREEN)
    REPS = 0
    CHECKS = 0
    config_check_marks()
    canvas.itemconfig(timer_txt, text="00:00")
    STARTED = False
    start.config(text="start", command=check_started)
    STOPPED = False

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def check_started():
    global STARTED
    global STOPPED

    if STOPPED == True:
        STOPPED = False
        restart_timer()
        start.config(text="stop", command=stop_timer)

    if STARTED == False:
        STARTED = True
        start_timer()
        start.config(text="stop", command=stop_timer)


def start_timer():

    global REPS
    
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        head_chahiye.config(text="long_break...", fg=RED)
        count_down(long_break_sec)
    elif REPS % 2 == 0:
        head_chahiye.config(text="short_break...", fg=PINK)
        count_down(short_break_sec)
    else:
        head_chahiye.config(text="working...", fg=GREEN)
        count_down(work_sec)


def restart_timer():
    count_down(TIMER_RN)

def stop_timer():
    global STOPPED

    STOPPED = True
    start.config(text="start", command=check_started)
    screen.after_cancel(TIMER)



    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    global CHECKS
    global TIMER
    global TIMER_RN

    count_min = math.floor(count / 60)
    formatted_min = "{:02d}".format(count_min)
    count_sec = int(count % 60)
    formatted_sec = "{:02d}".format(count_sec)

    canvas.itemconfig(timer_txt, text=f"{formatted_min}:{formatted_sec}")
    TIMER_RN = count

    if count > 0:
        TIMER = screen.after(1000, count_down, count - 1)
    else:
        start_timer()
        if REPS % 2 == 0:
            CHECKS += 1
            config_check_marks()
# ---------------------------- UI SETUP ------------------------------- #
screen = tk.Tk()
screen.title("Pawmodoro")
screen.config(padx=100, pady=75, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = tk.PhotoImage(file="code_py/[28]more__gui/tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_txt = canvas.create_text(100, 132, text="00:00", font=(FONT_NAME, 25, "bold"), fill="white")
canvas.grid(row=1, column=1)


head_chahiye = tk.Label(text="pawmodoro", font=("Amatic SC", 30, "bold"), fg=GREEN, bg=YELLOW)
head_chahiye.grid(row=0, column=1)

start = tk.Button(text="start", command=check_started, font=(FONT_NAME, 10), fg=YELLOW, bg=RED)
start.grid(row=2, column=0)

reset = tk.Button(text="reset", command=reset_timer, font=(FONT_NAME, 10), fg=YELLOW, bg=RED)
reset.grid(row=2, column=2)

check_marks = tk.Label(font=("Amatic SC", 17),fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)

def config_check_marks():
        check_marks.config(text="✔" * CHECKS)



screen.mainloop()