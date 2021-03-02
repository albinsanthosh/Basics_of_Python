from tkinter import *
main_window = Tk()
main_window.title('Phone Book')


def add():
    add_window = Toplevel(main_window)
    add_window.title('Add Contact')

    def saving():
        n = name_enter.get()
        p = phone_enter.get()
        print(f'{n}:{p} Added')
        file = open('C:/Users/Albin/Desktop/Phonebook.txt', 'a+')
        file.write(f'{n}:{p} ')
        file.close()
        name_enter.delete(0, END)
        phone_enter.delete(0, END)

    name = Label(add_window, text='Name:')
    name.pack(fill=BOTH, expand=True, padx=10, pady=10, ipadx=10, ipady=10)
    name_enter = Entry(add_window, width=25)
    name_enter.pack(fill=BOTH, expand=True, padx=10, pady=10, ipadx=10, ipady=10)
    phone = Label(add_window, text='Phone number:')
    phone.pack(fill=BOTH, expand=True, padx=10, pady=10, ipadx=10, ipady=10)
    phone_enter = Entry(add_window, width=25)
    phone_enter.pack(fill=BOTH, expand=True, padx=10, pady=10, ipadx=10, ipady=10)
    save = Button(add_window, text='Save', command=saving)
    save.pack(fill=BOTH, expand=True, padx=10, pady=10, ipadx=10, ipady=10)


def search():
    search_window = Toplevel(main_window)
    search_window.title('Search Contact')

    def searching():
        word = s_name_enter.get()
        file2 = open('C:/Users/Albin/Desktop/Phonebook.txt', 'a+')
        file2.seek(0)
        r = file2.read()
        n = r.split(' ')
        for i in n:
            m = i.split(':')
            if m[0] == word:
                print(f'Phone number of {word} : {m[1]}')
                return
            else:
                continue
        print(f'{word} number not found, please add the number')
        s_name_enter.delete(0, END)

    s_name = Label(search_window, text='Name:')
    s_name.pack(fill=BOTH, expand=True, padx=10, pady=10, ipadx=10, ipady=10)
    s_name_enter = Entry(search_window, width=25)
    s_name_enter.pack(fill=BOTH, expand=True, padx=10, pady=10, ipadx=10, ipady=10)
    search_bu = Button(search_window, text='Search', command=searching)
    search_bu.pack(fill=BOTH, expand=True, padx=10, pady=10, ipadx=10, ipady=10)


bu1 = Button(main_window, text='Search Contact', command=search, bg='red', fg='white')
bu1.pack(fill=BOTH, expand=True, padx=10, pady=10, ipadx=10, ipady=10)

bu2 = Button(main_window, text='Add Contact', command=add, bg='green', fg='black')
bu2.pack(fill=BOTH, expand=True, padx=10, pady=10, ipadx=10, ipady=10)

main_window.mainloop()