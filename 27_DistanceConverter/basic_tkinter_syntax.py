from tkinter import *

# init windows
window = Tk()
window.title('first GUI')
window.minsize(width=500, height=500)

# Method 1 of specifying labels
my_label = Label(text='I am a label', font=('Arial', 24, 'bold'))
my_label.pack(side='bottom') # To manage placement on screen (geometry management system)
# .pack() must be used on another components to place it on window


# Changing text of existing label, both methods valid, pick 1
my_label['text'] = 'New Text'
my_label.config(text='New Text')


def button_clicked():
    print('button clicked')
    usr_text = usr_input.get()
    text_box_text = t_box.get("1.0", END) # Get row 1 value
    print(text_box_text)
    my_label.config(text=usr_text)


# Buttons
btn = Button(text='click me', command=button_clicked)
btn.pack()

# User Entry Box
usr_input = Entry(width=10)
usr_input.insert(END, string='Placeholder text')
usr_input.pack()

# Textbox
t_box = Text(height=3, width=30)
t_box.focus() # creates active cursor within textbox
t_box.insert(END, 'Placeholder text')
t_box.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()


