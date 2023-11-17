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

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW) # padding for img


#  == Canvas setup ==
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) # set close to actual img resolution

tomato_bg = PhotoImage(file='tomato.png')
canvas.create_image((100, 112), image=tomato_bg) # ~ half of img resolution
canvas.create_text((98, 130), text="00:00", fill='white', font=(FONT_NAME, 20, 'bold'))
canvas.grid(column=1, row=1)

# == Timer Text ==
timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, 'bold'))
timer_label.grid(column=1, row=0)

# == Buttons ==
def start_timer():
    pass

def reset_timer():
    pass

start_btn = Button(text='Start', command=start_timer)
reset_btn = Button(text='Reset', command=reset_timer)

start_btn.grid(column=0, row=2)
reset_btn.grid(column=2, row=2)

# == checkmark ==

window.mainloop()