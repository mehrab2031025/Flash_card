from tkinter import *
import pandas as pd
from random import *

try:
    data = pd.read_csv("to_learn.csv")
except:
    data = pd.read_csv('french_words.csv')

data_list = data.to_dict(orient="records")

current_card = {}

def next_card():
    global current_card, id
    window.after_cancel(id)
    current_card = choice(data_list)
    canvas.itemconfig(canvas_image, image= front_img)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    id = window.after(3000, flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(canvas_image, image=back_imag)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")

def is_known():
    data_list.remove(current_card)
    new_data = pd.DataFrame(data_list)
    new_data.to_csv("to_learn.csv", index=False)
    next_card()



BGCOLOR = "#B1DDC6"
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BGCOLOR)
id = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BGCOLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

front_img = PhotoImage(file="card_front.png")
back_imag = PhotoImage(file="card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

wrong_img = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)
next_card()

window.mainloop()
