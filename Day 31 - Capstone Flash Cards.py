from tkinter import *
import pandas as pd
import random
from time import sleep

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


def correct():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    random_french_word()


def random_french_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_language, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=translation)


def translation():
    canvas.itemconfig(card_background, image=card_back)
    canvas.itemconfig(card_language, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


try:
    file = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original = pd.read_csv("french_words.csv")
    to_learn = original.to_dict(orient="records")
else:
    to_learn = file.to_dict(orient="records")
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=translation)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="card_front.png")
card_back = PhotoImage(file="card_back.png")
right_img = PhotoImage(file="right.png")
wrong_img = PhotoImage(file="wrong.png")
card_background = canvas.create_image(400, 263, image=card_front)
card_language = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"), fill="black")
canvas.grid(column=0, row=0, columnspan=2)
check = Button(image=right_img, highlightthickness=0, bg="grey", borderwidth=0, command=correct)
check.grid(column=0, row=1)
ex = Button(image=wrong_img, highlightthickness=0, bg="grey", borderwidth=0, command=random_french_word)
ex.grid(column=1, row=1)
random_french_word()
window.mainloop()