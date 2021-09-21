from tkinter import *

window = Tk()
window.geometry('300x400')
window.title("Calculator")

expression = StringVar()

textBox = Entry(window, text=expression, width=40, justify='right')
textBox.grid(row=0, columnspan=4, padx=10, pady=10, ipady=5)

buttons = [
    ['c','<-','%','='],
    ['7','8','9','*'],
    ['4','5','6','/'],
    ['1','2','3','-'],
    ['.','0','e','+'],
]

def calc(event):
    # print(event.widget.cget('text'))
    expression = event.widget.cget('text')
    value = textBox.get()
    textBox.insert(len(value), expression)

buttons_dict = {}
for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        current_btn = 'btn_{}'.format(buttons[i][j])
        btn = Button(window, text=buttons[i][j], font=('Arial',16), width=3)
        buttons_dict[current_btn] = btn
        buttons_dict[current_btn].grid(row=i+1, column=j, ipadx=5, ipady=5, padx=5, pady=5)
        buttons_dict[current_btn].bind('<Button-1>', calc)

# print(buttons_dict)
window.mainloop()