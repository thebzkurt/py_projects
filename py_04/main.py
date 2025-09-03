from random import shuffle, randint
from tkinter import *
from tkinter import messagebox
import pandas as pd
from PIL import ImageTk, Image
import os
from numpy.random import choice

save_files = "data.csv"

window = Tk()
window.title("My Password Saver")
window.geometry("750x600")
window.configure(padx=10, pady=10)

def info():
    df = pd.read_csv("data.csv")
    user_website = ent_website.get()
    if user_website == "":
        messagebox.showerror("Error", "Please enter a valid website")
        return
    for index, row in df.iterrows():
        if user_website.lower().strip() == row[" --Name-- "]:
            web = df.iloc[index, 0]
            email = df.iloc[index, 1]
            pwd = df.iloc[index, 2]
            messagebox.showinfo(web, f"Email: {email}\nPassword: {pwd}")
            return
    messagebox.showerror("Error", f"this website {ent_website.get()} doesn't exist")

def random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pwd_letter = [choice(letters) for _ in range(randint(8, 10))]
    pwd_number = [choice(numbers) for _ in range(randint(2,4))]
    pwd_symbol = [choice(symbols) for _ in range(randint(2,4))]

    password_list = pwd_letter + pwd_number + pwd_symbol
    shuffle(password_list)

    ent_password.delete(0, END)
    password = "".join(password_list)
    ent_password.insert(0, password)

#/-- save --/
def save_data():
    if os.path.exists(save_files):
        df = pd.read_csv(save_files)
    else:
        df = pd.DataFrame(columns=[" --Name-- "," --User-- "," --Password-- "])

    web_data = ent_website.get()
    user_data = ent_user.get()
    pwd_data = ent_password.get()

    if web_data.strip() == "" or user_data.strip() == "" or pwd_data.strip() == "":
        messagebox.showerror("Error", "Please fill all fields")
    else:
        check = messagebox.askyesno(web_data, f"These are the details entered:\nEmail: {user_data}"
                                              f"\nPassword: {pwd_data}\n is it ok to save?")
        if check:
            df.loc[len(df)] = [web_data, user_data, pwd_data]
            df.to_csv(save_files, index=False)
            messagebox.showinfo("Success", "Data saved")
        else:
            messagebox.showinfo("Success", "Data not saved")


    ent_website.delete(0, END)
    ent_user.delete(0, END)
    ent_password.delete(0, END)
    ent_website.focus()
    ent_user.insert(0, "@hotmail.com")


#/-- UI --/
canvas = Canvas(window, width = 300, height = 350, background="gray")
img = Image.open("lock.jpg")
lock_img = ImageTk.PhotoImage(img)
canvas.create_image(150,150, image = lock_img)
canvas.grid(row = 0, column = 0, columnspan = 3)

# /-- label --/
lbl_website = Label(window, text="Website Name:", font=("Arial", 16))
lbl_website.grid(row=1, column=0, padx = 10, pady = 5)

lbl_user = Label(window, text="Email or Username:", font=("Arial", 16))
lbl_user.grid(row=2, column=0,padx = 10, pady = 5)

lbl_password = Label(window, text="Password:", font=("Arial", 16))
lbl_password.grid(row=3, column=0,padx = 10, pady = 5,)

#/-- enter --/
ent_website = Entry(window, width=40, font=("Arial", 12))
ent_website.grid(row=1, column=1, pady = 5)
ent_website.focus()

ent_user = Entry(window, width=53, font=("Arial", 12))
ent_user.grid(row=2, column=1, columnspan=2, pady = 5)
ent_user.insert(0, "@gmail.com")

ent_password = Entry(window,width=40, font=("Arial", 12))
ent_password.grid(row=3, column=1 , pady = 5)

#/-- button --/
btn_search = Button(window, text="Search",width=14, bg='grey', command=info)
btn_search.grid(row=1, column=2, pady = 5)

btn_generate_password = Button(window, text="Generate Password", command=random_password, bg='grey')
btn_generate_password.grid(row=3, column=2, pady = 5)

btn_add = Button(window, text="Add", width=68, command=save_data,bg='grey')
btn_add.grid(row=4, column=2, pady = 5)
btn_add.grid(row=4, column=1, columnspan=2, pady = 5)

window.mainloop()


