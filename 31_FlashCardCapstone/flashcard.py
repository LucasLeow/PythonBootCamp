import random
from tkinter import *

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- CONSTANTS ------------------------------- #
CARD_WIDTH = 800
CARD_HEIGHT = 526

LG_FONT = ('Ariel', 40, 'italic')
WORD_FONT = ('Ariel', 60, 'bold')

WORDS_PATH = 'data/french_words.csv'


# ---------------------------- GENERATE NEW FLASHCARD ------------------------------- #
def generate_new_word():
    global flip_timer, random_pair
    window.after_cancel(flip_timer)  # Cancels flip timer for every new card requested upon button press
    random_pair = random.choice(words_list)
    french_word = random_pair['French']

    canvas.itemconfig(card_canvas, image=card_bg)
    canvas.itemconfig(title_text, text='French', fill='black')
    canvas.itemconfig(word_text, text=french_word, fill='black')

    flip_timer = window.after(3000, flip_card, random_pair)


def correct_btn():
    words_list.remove(random_pair)
    new_df = pd.DataFrame.from_records(words_list)
    new_df.to_csv('words_to_learn.csv')
    generate_new_word()


# # ---------------------------- FLIP FLASHCARD ------------------------------- #
def flip_card(word_pair):
    english_word = word_pair['English']
    canvas.itemconfig(card_canvas, image=card_after_bg)
    canvas.itemconfig(title_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=english_word, fill='white')


# ---------------------------- WORDS SETUP ------------------------------- #
try:
    df = pd.read_csv('words_to_learn.csv')
except FileNotFoundError:
    df = pd.read_csv(WORDS_PATH)

words_list = df.to_dict(orient='records')
random_pair = random.choice(words_list)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('French FlashCard')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# == Canvas setup (Card bg) ==
canvas = Canvas(width=CARD_WIDTH, height=CARD_HEIGHT)

card_bg = PhotoImage(file='images/card_front.png')
card_after_bg = PhotoImage(file='images/card_back.png')
card_canvas = canvas.create_image((CARD_WIDTH / 2, CARD_HEIGHT / 2), image=card_bg)

# Canvas text
title_text = canvas.create_text((CARD_WIDTH / 2, 150), text='French', fill='black', font=LG_FONT)
word_text = canvas.create_text((CARD_WIDTH / 2, 263), text=f'{random_pair["French"]}', fill='black', font=WORD_FONT)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
cross_img = PhotoImage(file='images/wrong.png')  # 100 x 99
right_img = PhotoImage(file='images/right.png')  # 100 x 100

cross_btn = Button(image=cross_img, highlightthickness=0, command=generate_new_word)
right_btn = Button(image=right_img, highlightthickness=0, command=correct_btn)

cross_btn.grid(column=0, row=1)
right_btn.grid(column=1, row=1)

flip_timer = window.after(3000, flip_card, random_pair)

window.mainloop()


