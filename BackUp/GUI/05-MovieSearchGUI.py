from tkinter import *
import MovieSearch

window = Tk()
window.geometry('900x500')
window.title("Movie Search Engine")

label_1 = Label(window, text = "Movie Search Engine", font=('Arial',28,'bold'))
label_1.pack()

textBox = Entry(window, width=30, font=('Arial',20,'bold'))
textBox.place(x=10, y=70)

label_2 = Label(window, text = "", font=('Arial',20,'bold'))
label_2.place(x = 10, y=160)

label_3 = Label(window, text = "", font=('Arial',20,'bold'))
label_3.place(x = 10, y=200)

label_4 = Label(window, text = "", font=('Arial',20,'bold'), wraplength=700)
label_4.place(x = 10, y=250)

def showResult():
    movieName = textBox.get()
    title, summary, rating = MovieSearch.search(movieName)
    label_2.config(text = title)
    label_3.config(text = rating)
    label_4.config(text = summary)

btn = Button(window, text="Search Movie", width=20, font=('Arial',15), command=showResult)
btn.place(x=500, y=70)

window.mainloop()