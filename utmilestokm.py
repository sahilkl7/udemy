from tkinter import *

windows = Tk()
windows.title('Miles To KM')
windows.config(padx=20,pady=20)


def button_clicked():
    miles = float(miles_input.get())
    km = miles*1.6
    my_label3.config(text= km)



my_label = Label(text = 'is equal to')
my_label.grid(column=0,row=1)


my_label1 = Label(text = 'Miles')
my_label1.grid(column=3,row=0)


my_label2 = Label(text = 'KM')
my_label2.grid(column=3,row=2)



my_label3 = Label(text ='0')
my_label3.grid(row=2,column=2)


button = Button(text = 'Calculate',command = button_clicked)
button.grid(row=3,column=2)


miles_input = Entry(width=5)
miles_input.grid(row=0,column=2)


windows.mainloop()