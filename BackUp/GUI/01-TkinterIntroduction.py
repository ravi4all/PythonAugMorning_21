# import tkinter
from tkinter import *

# 1. Window
root = Tk()
root.title("Tkinter GUI")
root.geometry('300x300')

# nameLabel = Label(root, text = "Hello Ravi...")
# nameLabel.grid(row=0, column=0, pady=10)
# nameLabel.pack()

# Widget
# label = Label(root, text = "Hello World...")
# label.pack()
# label.place(x=10,y=10)
# label.place(relx=0.5, rely=0.5, anchor=CENTER)
# label.grid(row=0,column=1, padx=10)

btn_1 = Button(root, text="Click Here", background="red", fg="white")
btn_1.pack(expand = True, fill=BOTH, side=LEFT)

btn_2 = Button(root, text="Click Here", background="green", fg="white")
btn_2.pack(expand = True, fill=BOTH, side=LEFT)

btn_3 = Button(root, text="Click Here", background="blue", fg="white")
btn_3.pack(expand = True, fill=BOTH, side=LEFT)

btn_4 = Button(root, text="Click Here", background="red", fg="white")
btn_4.pack(expand = True, fill=BOTH, side=LEFT)

root.mainloop()