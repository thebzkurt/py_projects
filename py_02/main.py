from tkinter import *

window = Tk()
window.geometry("320x120")
window.title("Converters")
window.config(padx=20, pady=20)
state = 0
# /--/ functions
def convert():
    global state
    if state == 0:
        miles_label.config(text="Kilogram")
        kg_label.config(text="Pound")
        convert_button.config(text="Pound to Kilogram")
        state = 1
    elif state == 1:
        miles_label.config(text="Pound")
        kg_label.config(text="Kilogram")
        convert_button.config(text="Kilogram to Pound")
        state = 0

def caculate(input):
    global state
    if state == 0:
        result = int(input) * 45/100
        info_label.config(text=f"{result:.2f}")
    elif state == 1:
        result = int(input) * 100 / 45
        info_label.config(text=f"{result:.2f}")

# /--/ labels
info_label = Label(window, text="0")
info_label.grid(row=1, column=1)

miles_label = Label(window, text="Pound")
miles_label.grid(row=0, column=2)

kg_label = Label(window, text="Kilogram")
kg_label.grid(row=1, column=2)

convert_label = Label(window, text="is equal to")
convert_label.grid(row=1, column=0)

# /--/ enters
input_enter = Entry(window)
input_enter.grid(row=0, column=1)

# /--/ buttons
calculate_button = Button(window, text="Calculate", command=lambda: caculate(input_enter.get()))
calculate_button.grid(row=2, column=1)

convert_button = Button(window, text="Kilogram to Pound", command=lambda: convert())
convert_button.grid(row=2, column=0)


window.mainloop()