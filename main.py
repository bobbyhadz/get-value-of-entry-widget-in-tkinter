# How to get the value of an Entry widget in Tkinter

from tkinter import *
from tkinter import ttk

root = Tk()

root.geometry('600x300')

entry = ttk.Entry(root)
entry.pack(pady=50)

label = ttk.Label(root, text='')
label.pack(pady=20)


def get_entry_value():
    value = entry.get()
    print(value)

    label.config(text=value)


button = ttk.Button(root, text="Get Entry Value", command=get_entry_value)
button.pack(pady=25)

root.mainloop()