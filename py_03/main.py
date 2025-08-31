from time import process_time
from tkinter import *
import math

window = Tk()
window.title("Pomodoro")
window.geometry("230x210")
window.config(background = "#FEFADC", padx = 10, pady = 10)

rest_time = 5
long_rest_time = 20
work_time = 1
second_time = 60
reps = 0
timer = None

def rest():
    global reps
    window.after_cancel(timer)
    start_btn.config(state=NORMAL)
    main_label.config(text="Pomodoro", background = "#FEFADC", font=("Arial", 16))
    time_label.config(text="00:00", background = "#FEFADC", font=("Arial", 16))
    count_label.config(text="0", background = "#FEFADC",  font=("Arial", 16))
    reps = 0


def start_time():
    global reps
    start_btn.config(state=DISABLED)
    reps += 1
    print(reps)
    work_sec = work_time * 60
    rest_sec = rest_time * 60
    long_rest_sec = long_rest_time * 60


    if reps % 2 == 1:
        count_down(work_sec)
        main_label.config(text = "Work", background = "#FEFADC", font=("Arial", 16))
    elif reps % 8 == 0:
        count_down(long_rest_sec)
        main_label.config(text="Rest", background="#FEFADC", font=("Arial", 16))
    elif reps % 2 == 0:
        count_down(rest_sec)
        main_label.config(text="Rest", background="#FEFADC", font=("Arial", 16))

def count_down(seconds):
    global reps, timer
    count_min = math.floor(seconds / 60)
    count_sec = seconds % 60
    if count_sec <10:
        time_label.config(text=f"{count_min}:0{count_sec}")
    else :
        time_label.config(text=f"{count_min}:{count_sec}")
    if seconds > 0:
        timer =window.after(50, count_down, seconds - 1)
    else:
        start_time()
        count = ""
        work_s = math.floor(reps/2)
        for _ in range(work_s):
            count += "✅"
        count_label.config(text=count, padx = 10,)


# /-- labels --/
main_label = Label(window, text="Pomodoro", background = "#FEFADC", font=("Arial", 16))
main_label.grid(row=0, column=0, columnspan=2, padx=60, pady=10)

time_label = Label(window, text="00:00", background = "#FEFADC", font=("Arial", 16))
time_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

count_label = Label(window, text="0", background = "#FEFADC",  font=("Arial", 16))
count_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# /-- buttons --/
start_btn = Button(window, text="Start", width=10, command=start_time)
start_btn.grid(row=2, column=0, padx=10, pady=10)

reset_btn = Button(window, text="Reset", width=10, command=rest)
reset_btn.grid(row=2, column=1, padx=10, pady=10)



window.mainloop()