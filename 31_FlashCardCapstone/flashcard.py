from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- CONSTANTS ------------------------------- #
CARD_WIDTH = 800
CARD_HEIGHT = 526

LG_FONT = ('Ariel', 40, 'italic')
WORD_FONT = ('Ariel', 60, 'bold')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('French FlashCard')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# == Canvas setup (Card bg) ==
canvas = Canvas(width=CARD_WIDTH, height=CARD_HEIGHT, highlightthickness=0)

card_bg = PhotoImage(file='images/card_front.png')
canvas.create_image((CARD_WIDTH/2, CARD_HEIGHT/2), image=card_bg)

# Canvas text
canvas.create_text((CARD_WIDTH/2, 150), text='French', fill='black', font=LG_FONT)
canvas.create_text((CARD_WIDTH/2, 263), text='trouve', fill='black', font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
cross_img = PhotoImage(file='images/wrong.png') # 100 x 99
right_img = PhotoImage(file='images/right.png') # 100 x 100

cross_btn = Button(image=cross_img, highlightthickness=0)
right_btn = Button(image=right_img, highlightthickness=0)

cross_btn.grid(column=0, row=1)
right_btn.grid(column=1, row=1)

window.mainloop()
