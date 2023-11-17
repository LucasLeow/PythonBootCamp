from tkinter import *

window = Tk()
window.title('first GUI')
window.minsize(width=300, height=500)
window.config(padx=20, pady=20)  # add padding to components


def button_clicked():
    print('Button clicked')


# pack : place components (default top-down)
# cannot specify precise location
my_label = Label(text='Label 1', font=('Arial', 24, 'bold'))
my_label.grid(column=0, row=0)
# my_label.pack(side='left')


# place
# can place at precise location (x, y)
btn = Button(text='Button 1', command=button_clicked)
# btn.place(x=0, y=0)
btn.grid(column=1, row=1)

btn2 = Button(text='Button 2', command=button_clicked)
btn2.grid(column=0, row=2)

# grid: window divided to rows & cols of grid
# grid relative to first grid component
input_box = Entry(width=10)
input_box.grid(column=3, row=2)
# input_box.grid(column=0, row=0)

# grid & pack cannot be used together
# grid usually more often used


window.mainloop()
