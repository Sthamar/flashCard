from tkinter import *
import pandas
import random


words = {}
learn_word = {}
BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("data/to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    learn_word = original_data.to_dict(orient="records")
else:
    learn_word = data.to_dict(orient="records")


def next_card():
    global words, timer
    window.after_cancel(timer)
    words = random.choice(learn_word)
    canvas.itemconfig(text_title, text="French", fill = "black")
    canvas.itemconfig(word_text, text= words["French"], fill = "black")
    canvas.itemconfig(card_background, image=card_front_img)
    timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(text_title, text="English", fill = "white")
    canvas.itemconfig(word_text, text= words["English"], fill = "white")


def known_words():
    learn_word.remove(words)
    print(len(learn_word))
    data = pandas.DataFrame(learn_word)
    data.to_csv("data/to_learn.csv", index=False)

    next_card()



window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, func=flip_card)

#canvas

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image= card_front_img)
text_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_text =canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#buttons
right_img = PhotoImage(file="images/right.png")
wrong_img =PhotoImage(file="images/wrong.png")
right_btn = Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=known_words)
right_btn.grid(column=1, row=1)
wrong_btn = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_btn.grid(column=0, row=1)

next_card()

window.mainloop()
