from time import process_time
from tkinter import *
import time

window = Tk()
window.title("Pomodoro")
window.geometry("230x210")
window.config(background = "#FEFADC", padx = 10, pady = 10)

work = True
status = 0
reset_time = 5
work_time = 1
second_time = 60

def set_reset():
    global status
    if status == 0:
        time_label.config(text="00:00", background = "#FEFADC", font=("Arial", 16))
        main_label.config(text="Work", background = "#FEFADC", font=("Arial", 16))
        count_label.config(text="0", background = "#FEFADC",  font=("Arial", 16))
        status = 1
        print(status)

def work_time_set():
    global second_time, work_time, second_time, status, reset_time, work
    print(status)

    while True:
        if status == 0:
            if second_time > 0:
                second_time -= 1
                time_label.config(text = f"{work_time}:{second_time}")
                main_label.config(text = f"Pomodoro")
                if second_time < 10:
                    time_label.config(text=f"{work_time}:0{second_time}")
                print(second_time)
            elif second_time == 0:
                time_label.config(text = f"{work_time}:{second_time}")
                second_time = 60
            # start_btn.config(state="disabled")
        elif status == 1:
            second_time = 60
            work_time = 1
            status = 0
            break
        time.sleep(0.2)
        window.update()


# /-- labels --/
main_label = Label(window, text="Work", background = "#FEFADC", font=("Arial", 16))
main_label.grid(row=0, column=0, columnspan=2, padx=60, pady=10)

time_label = Label(window, text="00:00", background = "#FEFADC", font=("Arial", 16))
time_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

count_label = Label(window, text="0", background = "#FEFADC",  font=("Arial", 16))
count_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# /-- buttons --/
start_btn = Button(window, text="Start", width=10, command=work_time_set)
start_btn.grid(row=2, column=0, padx=10, pady=10)

reset_btn = Button(window, text="Reset", width=10, command=set_reset)
reset_btn.grid(row=2, column=1, padx=10, pady=10)



window.mainloop()