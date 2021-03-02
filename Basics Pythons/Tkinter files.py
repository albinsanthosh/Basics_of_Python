# Canvas, Textbox
from tkinter import *

window = Tk()
window.title('Test')

fm = LabelFrame(window, text="Hello this is label frame")
fm.pack()

can = Canvas(window, height=100, width=100, bg='red')
can.pack()

can.create_line(0, 0, 300, 300, fill='white', width=5)
can.create_line(50, 50, -300, 300, fill='white', width=5)
can.create_rectangle(40, 40, 60, 60)

tb = Text(window, height=10, width=30, selectbackground='yellow')
tb.pack()
# Event


def right(e):
    print('I am right')


bu = Button(window, text="Click me event right!")
bu.pack()
bu.bind("<Button-3>", right)

# checkbutton
j = IntVar()


def accept():
    print(j.get())


cb = Checkbutton(window, text='I accept', variable=j, onvalue=1, offvalue=0, command=accept)
cb.pack()

# Spinbox


def spin():
    print(sb.get())


sb = Spinbox(window, from_=0, to_=100)
sb.pack()

spin_bu = Button(window, text="Click me spinbox value", command=spin)
spin_bu.pack()

# Listbox, list(map(sq,seq))


def lb_func():
    v = lb.curselection()
    print(v)


lb = Listbox(window, selectmode=MULTIPLE)
lb.insert(0, 'Apple', 'Mango', 'Orange', 'Guava')
lb.pack()

lb_bu = Button(window, text="Click me spinbox value", command=lb_func)
lb_bu.pack()

window.mainloop()
