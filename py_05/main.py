from tkinter import *

BG_COLOR = "#B1DDC6"

window = Tk()
window.title("Project")
window.config(padx=50, pady=50, background=BG_COLOR)
canvas = Canvas(width=800, height=526, highlightthickness=0., background=BG_COLOR)
card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 253, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

#/-- label canvas --/
canvas.create_text(400, 150, text="English", font=("Arial", 40, "italic"), fill="black")
canvas.create_text(400, 253, text="English", font=("Arial", 60, "italic"), fill="black")


Ture_img = PhotoImage(file="./images/right.png")
btn_True = Button(window, image=Ture_img, highlightthickness=0,)
btn_True.grid(row=1, column=1)
False_img = PhotoImage(file="./images/wrong.png")
btn_False = Button(window, image=False_img, highlightthickness=0)
btn_False.grid(row=1, column=0)

window.mainloop()