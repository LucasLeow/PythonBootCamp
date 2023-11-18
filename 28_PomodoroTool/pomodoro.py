from tkinter import *

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
sets = 0
timer = None  # must be global var so can pass to reset fn

reps_chk_mark = "✔"
sets_chk_mark = "✨"

chk_marks = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    # clear checkmarks, stop & reset timer, change title
    global reps, sets, timer, chk_marks
    reps = 0
    sets = 0
    chk_marks = ""

    window.after_cancel(timer)  # Stop Timer
    canvas.itemconfig(timer_text, text="00:00")  # Reset timer text
    timer_label.config(text='Timer', fg=GREEN)  # Reset timer title
    chk_mark_label.config(text=chk_marks)  # Clear check marks


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, sets
    reps += 1

    # work_time = WORK_MIN * 60
    # short_break_time = SHORT_BREAK_MIN * 60
    # long_break_time = LONG_BREAK_MIN * 60

    work_time = 1
    short_break_time = 1
    long_break_time = 1

    if reps % 8 == 0:
        timer_label.config(text='Long Break', fg=RED)
        sets += 1
        count_down(seconds=long_break_time)
    elif reps % 2 == 0:
        timer_label.config(text='Short Break', fg=PINK)
        count_down(seconds=short_break_time)
    else:
        timer_label.config(text='Work', fg=GREEN)
        count_down(seconds=work_time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(seconds):  # recursive call to countdown
    global reps, sets, chk_marks, timer
    mins, secs = divmod(seconds, 60)  # returns quotient (mins) & remainder (secs)
    text = '{:02d}:{:02d}'.format(mins, secs)
    canvas.itemconfig(timer_text, text=text)  # Update timer_text
    if seconds > 0:
        timer = window.after(1000, count_down, seconds - 1)  # .after() calls function after some time
        # cannot use while loop because interferes with canvas mainloop()
    else:
        if reps % 2 == 0:
            if sets == 1:
                chk_marks += sets_chk_mark
                sets = 0
                chk_mark_label.config(text=chk_marks)
            else:
                chk_marks += reps_chk_mark
                chk_mark_label.config(text=chk_marks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)  # padding for img

#  == Canvas setup (Tomato Image) ==
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # set close to actual img resolution

tomato_bg = PhotoImage(file='tomato.png')
canvas.create_image((100, 112), image=tomato_bg)  # ~ half of img resolution
timer_text = canvas.create_text((100, 130), text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# == Timer Text ==
timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, 'bold'))
timer_label.grid(column=1, row=0)

# == Buttons ==
start_btn = Button(text='Start', command=start_timer)
reset_btn = Button(text='Reset', command=reset_timer)

start_btn.grid(column=0, row=2)
reset_btn.grid(column=2, row=2)

# == checkmark ==
chk_mark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, 'normal'))
chk_mark_label.grid(column=1, row=3)
window.mainloop()
