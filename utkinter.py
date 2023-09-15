from tkinter import *


def button_clicked():
    print('I Got Clicked!')
    my_lable.config(text=input.get())


def buttons():
    my_lable.config(text="Hello Wassup!")


window = Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)

my_lable = Label(text='I am Label', font=('Arial', '24', "bold"))
my_lable.grid(column=0, row=0)

# ENTERY COMPONENT
input = Entry(width=10)
input.grid(column=4, row=4)

button = Button(text='Click ME!', command=button_clicked)  # Only the name of the function
button.grid(column=2, row=2)

new_button = Button(text='New Button', command=buttons)
new_button.grid(column=3, row=1)

window.mainloop()
