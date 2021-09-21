from tkinter import *

window = Tk()
window.title("My First App")
window.geometry('300x300')

def changeText():
    label.configure(text = "Bye From Ravi...")

label = Label(window, text="Hello From Ravi...")
label.grid()

# Binding
btn = Button(window, text="Click Here", fg="red", command = changeText)
btn.grid(column=1, row=0)

window.mainloop()