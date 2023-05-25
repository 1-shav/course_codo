import tkinter as tk
import math
from playsound import playsound
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#F2C9F0"
PURPLE = "#395D73"
GREEN = "#2D4859"
YELLOW = "#f7f5dd"
BLUE = "#1B1959"
FONT_NAME = "Dogica"
WORK_MIN = 35
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
    #head_chahiye.config(text="pawmodoro", fg=GREEN)
    REPS = 0
    CHECKS = 0
    config_check_marks()
    timed_canvas.itemconfig(timer_txt, text="00:00")
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
        #head_chahiye.config(text="long_break...", fg=PURPLE)
        count_down(long_break_sec)
    elif REPS % 2 == 0:
        #head_chahiye.config(text="short_break...", fg=PINK)
        count_down(short_break_sec)
    else:
        #head_chahiye.config(text="working...", fg=GREEN)
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

    timed_canvas.itemconfig(timer_txt, text=f"{formatted_min}:{formatted_sec}")
    TIMER_RN = count

    if count > 0:
        TIMER = screen.after(1000, count_down, count - 1)
    else:
        playsound("code_py/[28]more__gui/pawmodoro/sound.mp3")
        start_timer()
        if REPS % 2 == 0:
            CHECKS += 1
            config_check_marks()


def config_check_marks():
        check_marks.config(text="-" * CHECKS)


# ---------------------------- UI SETUP ------------------------------- #

screen = tk.Tk()
screen.title("Pawmodoro")
screen.config(padx=100, pady=75, bg=PINK)


logo_canvas = tk.Canvas(width=460, height=300, bg=PINK, highlightthickness=0)
logo = tk.PhotoImage(file="code_py/[28]more__gui/pawmodoro/logooo.png")
logo_canvas.create_image(230, 150, image=logo)
logo_canvas.grid(row=0, column=1)


timed_canvas = tk.Canvas(width=260, height=50, bg=PINK, highlightthickness=0)
timer_txt = timed_canvas.create_text(130, 25, text="00:00", font=(FONT_NAME, 40, "bold"), fill="white")
timed_canvas.grid(row=1, column=1)

start = tk.Button(text="start", command=check_started, font=(FONT_NAME, 10), fg=YELLOW, bg=PURPLE)
start.grid(row=2, column=0)

reset = tk.Button(text="reset", command=reset_timer, font=(FONT_NAME, 10), fg=YELLOW, bg=PURPLE)
reset.grid(row=2, column=2)

check_marks = tk.Label(font=(FONT_NAME, 17),fg=GREEN, bg=PINK)
check_marks.grid(row=3, column=1)









screen.mainloop()