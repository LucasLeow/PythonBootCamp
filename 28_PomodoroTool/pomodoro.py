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

chk_mark = "✔"

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    count_down(seconds=(WORK_MIN * 60))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(seconds):  # recursive call to countdown
    mins, secs = divmod(seconds, 60)  # returns quotient (mins) & remainder (secs)
    text = '{:02d}:{:02d}'.format(mins, secs)
    canvas.itemconfig(timer_text, text=text)  # Update timer_text
    if seconds > 0:
        window.after(1000, count_down, seconds - 1)  # .after() calls function after some time
        # cannot use while loop because interferes with canvas mainloop()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW) # padding for img

#  == Canvas setup (Tomato Image) ==
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) # set close to actual img resolution

tomato_bg = PhotoImage(file='tomato.png')
canvas.create_image((100, 112), image=tomato_bg) # ~ half of img resolution
timer_text = canvas.create_text((100, 130), text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


# == Timer Text ==
timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, 'bold'))
timer_label.grid(column=1, row=0)

# == Buttons ==
def reset_timer():
    print('stop clicked')

start_btn = Button(text='Start', command=start_timer)
reset_btn = Button(text='Reset', command=reset_timer)

start_btn.grid(column=0, row=2)
reset_btn.grid(column=2, row=2)

# == checkmark ==
chk_mark_label = Label(text=chk_mark, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, 'normal'))
chk_mark_label.grid(column=1, row=3)
window.mainloop()