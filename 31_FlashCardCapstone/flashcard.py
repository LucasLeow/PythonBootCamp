from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- CONSTANTS ------------------------------- #
CARD_WIDTH = 800
CARD_HEIGHT = 526

LG_FONT = ('Ariel', 40, 'italic')
WORD_FONT = ('Ariel', 60, 'bold')

WORDS_PATH = 'data/french_words.csv'

# ---------------------------- GENERATE NEW FLASHCARD ------------------------------- #
def generate_new_word():
    df = pd.read_csv(WORDS_PATH)
    random_row = df.sample()

    french_word = random_row['French'].values[0]
    canvas.itemconfig(word_text, text=french_word)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('French FlashCard')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# == Canvas setup (Card bg) ==
canvas = Canvas(width=CARD_WIDTH, height=CARD_HEIGHT)

card_bg = PhotoImage(file='images/card_front.png')
canvas.create_image((CARD_WIDTH/2, CARD_HEIGHT/2), image=card_bg)

# Canvas text
title_text = canvas.create_text((CARD_WIDTH/2, 150), text='French', fill='black', font=LG_FONT)
word_text = canvas.create_text((CARD_WIDTH/2, 263), text='trouve', fill='black', font=WORD_FONT)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
cross_img = PhotoImage(file='images/wrong.png') # 100 x 99
right_img = PhotoImage(file='images/right.png') # 100 x 100

cross_btn = Button(image=cross_img, highlightthickness=0, command=generate_new_word)
right_btn = Button(image=right_img, highlightthickness=0, command=generate_new_word)

cross_btn.grid(column=0, row=1)
right_btn.grid(column=1, row=1)

window.mainloop()
