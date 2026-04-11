import csv
from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 30, "italic")
WORD_FONT = ("Ariel", 40, "bold")
current_card = {}
to_learn = {}

# --------------------------- CARDS ---------------------------

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/japanese_hiragana.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="hiragana", fill="black")
    canvas.itemconfig(card_word, text=current_card["Japanese"], fill="black")
    canvas.itemconfig(canvas_img, image=card_front_img)
    flip_timer = window.after(5000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(card_title, text="romaji", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def known_card():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

# ------------------------------ UI ------------------------------

window = Tk()
window.title("Flashy")
window.minsize(910, 740)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

card_front_img = PhotoImage(file="./resources/card_front.png")
card_back_img = PhotoImage(file="./resources/card_back.png")
right_img = PhotoImage(file="./resources/right.png")
wrong_img = PhotoImage(file="./resources/wrong.png")

canvas = Canvas(width=800, height=526)
canvas_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=TITLE_FONT)
card_word = canvas.create_text(400, 263, text="", font=WORD_FONT)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

known_btn = Button(image=right_img, highlightthickness=0, command=known_card)
known_btn.grid(column=0, row=1)
unknown_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
unknown_btn.grid(column=1, row=1)

flip_timer = window.after(5000, flip_card)
next_card()

window.mainloop()
