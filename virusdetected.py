from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('400x400')

def msg_warning():
    messagebox.showwarning('Alert', 'Stop! Virus Found')

def msg_info():
    messagebox.showinfo('scan result', 'no virus found, system safe')

def ask_user():
    result=messagebox.askyesno('confirmation', 'do you want to delete the virus?')
    if result == True:
        messagebox.showinfo('Deleted', 'Virus Removed')
    else:
        messagebox.showinfo('Cancelled', 'Operation Cancelled')

button1=Button(root, text = 'scan for virus', command=msg_warning, width = 25)
button1.place(x=40, y=80)

button2=Button(root, text = 'check status', command=msg_info, width = 25)
button2.place(x=40, y=120)

button3=Button(root, text = 'remove virus', command=ask_user, width = 25)
button3.place(x=40, y=160)

root.mainloop()