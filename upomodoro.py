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
reps =0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    works_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 6
    if reps % 8 == 0 :
        count_down(long_break_sec)
        Title_text.config(text='Break',fg = RED)

    elif reps %2 == 0:
        count_down(works_sec)
        Title_text.config(text='Break', fg=RED)
    else:
        count_down(short_break_sec)
        Title_text.config(text='Work', fg=PINK)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_second = count % 60
    if count_second < 10:
        count_second = f'0{count_second}'

    canvas.itemconfig(timer_text, text=f"{(count_min)}:{count_second}")

    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ''
        for i in range(reps/2):
            option_check.config(text='')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_png)
timer_text = canvas.create_text(100, 130, text='00:00', fill='black', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

Title_text = Label(text='TIMER', bg=YELLOW, font=(FONT_NAME, '50'), fg=GREEN)
Title_text.grid(row=0, column=1)

option_check = Label(fg=GREEN, bg=YELLOW)
option_check.grid(row=3, column=1)

start_button = Button(text='Start', highlightthickness=0, bg=GREEN, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', highlightthickness=0, bg=GREEN)
reset_button.grid(row=2, column=3)

window.mainloop()
