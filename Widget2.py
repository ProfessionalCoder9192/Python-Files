from tkinter import *
from datetime import date

root = Tk()
root.title('Getting started with Widgets')
root.geometry('400x300')

lbl = Label(text='hey there!', fg='white', bg = 'green', height = 1, width = 300)

name_lbl = Label(text='full name', bg = 'blue')
name_entry = Entry()

def display ():
    name = name_entry.get()
    global message 
    message = 'Welcome to Application \ntodays date is: '
    greet = 'Hello ' + name + '\n'

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box=Text(height = 3)

btn = Button(text = 'begin', command = display, height = 1, bg = 'orange', fg = 'black')

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()