from tkinter import *

window = Tk()
window.title('Amount Book')

na = {}


def save():
    n = e1.get()
    a = e2.get()
    na[n] = a
    e1.delete(0, END)
    e2.delete(0, END)


def check():
    print(na)


l1 = Label(window, text='Name:')
l1.place(x=10, y=10)
e1 = Entry(window, width=25)
e1.place(x=70, y=10)
l2 = Label(window, text='Amount:')
l2.place(x=10, y=40)
e2 = Entry(window, width=25)
e2.place(x=70, y=40)
bu1 = Button(window, text='Save', command=save)
bu1.place(x=70, y=80)
bu2 = Button(window, text='Check', command=check)
bu2.place(x=70, y=120)

window.mainloop()
