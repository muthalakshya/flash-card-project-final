BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


#-------------------------Import------------------------------------------------------
from tkinter import *
import pandas
import random

# ----------------------accesing data file------------------------------------------------------0

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    # print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_text():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text = current_card["French"], fill="black")
    canvas.itemconfig(background, image=card_front_img)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_text()




# ----------------------UI Setup------------------------------------------------------
window = Tk()
window.config(pady=50,padx=50,bg=BACKGROUND_COLOR,highlightthickness=0)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

background = canvas.create_image(400,263,image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR)

title = canvas.create_text(400,150,text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400,263,text="word", font=("Ariel", 60, "bold"))

canvas.grid(row=0, column=0,columnspan=2)


wrong_mark_img = PhotoImage(file="images\wrong.png")
button_1 = Button(image=wrong_mark_img, highlightthickness=0, command=next_text)
button_1.grid(row=1, column=0)

right_mark_img = PhotoImage(file="images/tick.png")
button_2 = Button(image=right_mark_img, highlightthickness=0, command=is_known)
button_2.grid(row=1, column=1)


next_text()



window.mainloop()