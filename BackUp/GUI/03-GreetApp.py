from tkinter import *

window = Tk()
window.title("My First App")
window.geometry('700x600')

def changeText():
    text = textBox.get()
    label_2.configure(text = "Hello : " + text)

label = Label(window, text="Enter your name : ", fg='red', font=('Arial',28,'bold'))
# label.grid(column=0, row=0)
label.place(x = 10, y = 10)

textBox = Entry(window, width=20, font=('Arial',20,'bold'))
# textBox.grid(column=1, row=0)
textBox.place(x = 10, y = 70)

label_2 = Label(window, text="", font=('Arial',28,'bold'))
# label_2.grid(column=0, row=2)
label_2.place(x = 10, y= 140)

# Binding
btn = Button(window, text="Click Here", fg="red", command = changeText)
# btn.grid(column=1, row=1)
btn.place(x = 400, y = 70, width=200, height=30)

window.mainloop()