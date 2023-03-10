abb = "x"
from tkinter import *
from tkinter import ttk

clicks = 4

def click_button():
    global clicks
    clicks += 1
    #текст
    btn["text"] = f"(*-*) (:>)"

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

# кнопка
btn = ttk.Button(text="(-_-)", command=click_button)
btn.pack()

root.mainloop()
