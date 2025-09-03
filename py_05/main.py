from tkinter import *
import pandas as pd
import random
import time

BG_COLOR = "#B1DDC6"
FIlE_NAME = "french_words.csv"

df = pd.read_csv(FIlE_NAME)
new_dict = df.to_dict(orient="records")


def front_card():
    global set_timer
    window.after_cancel(set_timer)
    random_fr = random.choice(new_dict)
    canvas.itemconfig(cnv_img, image=card_front_img)
    canvas.itemconfig(text_title, text="French", fill="black")
    canvas.itemconfig(text_word, text=random_fr["French"], fill="black")
    set_timer = window.after(3000, back_card)

def back_card():
    canvas.itemconfig(cnv_img, image=card_back_img)
    random_en = random.choice(new_dict)
    canvas.itemconfig(text_title, text="English", fill="white")
    canvas.itemconfig(text_word, text=random_en["English"], fill="white")

window = Tk()
window.title("Project")
window.config(padx=50, pady=50, background=BG_COLOR)
set_timer = window.after(3000, back_card)
canvas = Canvas(width=800, height=526, highlightthickness=0., background=BG_COLOR)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
cnv_img = canvas.create_image(400, 253, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

#/-- label canvas --/
text_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"), fill="black")
text_word = canvas.create_text(400, 253, text="", font=("Arial", 60, "bold"), fill="black")


Ture_img = PhotoImage(file="./images/right.png")
btn_True = Button(window, image=Ture_img, highlightthickness=0,command=front_card)
btn_True.grid(row=1, column=1)
False_img = PhotoImage(file="./images/wrong.png")
btn_False = Button(window, image=False_img, highlightthickness=0,command=front_card)
btn_False.grid(row=1, column=0)

front_card()
window.mainloop()