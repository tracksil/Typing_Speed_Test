import time
from tkinter import *
from tkinter import Tk
from tkinter import messagebox

with open('info.txt') as data:
    decode = data.read()


def start():

    minute.set("01")
    second.set("02")
    entry.set('')

    start_btn.destroy()

    minute_label.grid(column=0, row=0)
    dots_label.grid(column=1, row=0)
    second_label.grid(column=2, row=0)

    text_label.grid(columnspan=3, column=0, row=1)

    entry_label.grid(columnspan=3, column=0, row=2)

    temp = int(minute.get())*60 + int(second.get())

    while temp > -1:
        mins, secs = divmod(temp, 60)

        minute.set("{0:2d}".format(mins))
        second.set(("{0:2d}".format(secs)))

        window.update()
        time.sleep(1)

        if temp == 0:
            number = 0
            entrys = entry.get()
            entry_words = entrys.split(' ')
            decode_words = decode.split(' ')

            for i in range(0, len(decode_words)):
                try:
                    if entry_words[i] == decode_words[i]:
                        number += 1
                except IndexError:
                    continue
            messagebox.showinfo("Time Countdown", f"Your score is {number} words per minute")

            restart_btn.grid(columnspan=3, column=0, row=3)

        temp -= 1


window = Tk()
window.title('Typing Speed Test')
window.geometry("600x550")
window.config(padx=50, pady=50)

minute = StringVar()
second = StringVar()
entry = StringVar()

start_btn = Button(text="Start", width=25, height=5, command=start)
start_btn.place(x=175, y=125)

minute_label = Label(window, width=3, font=("Arial", 18, ''), textvariable=minute)
dots_label = Label(window, text=":", width=3, font=("Arial", 18, ''))
second_label = Label(window, width=3, font=("Arial", 18, ''), textvariable=second)

text_label = Label(window, text=decode, wraplength=500, font=("Arial", 12, ''), pady=20)

entry_label = Entry(window, width=80, textvariable=entry)

restart_btn = Button(text="Restart", width=15, command=start)

window.mainloop()
