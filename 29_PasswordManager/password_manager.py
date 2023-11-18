from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
FONT = ('Arial', 12, 'normal')
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    pass
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

# == Canvas setup (Lock Image) ==
canvas = Canvas(width=200, height=200)

lock_bg = PhotoImage(file='logo.png')
canvas.create_image((100, 100), image=lock_bg)

canvas.grid(column=1, row=0)

# == Website Label & Input ==
website_label = Label(text='Website:', font=FONT)
website_label.grid(column=0, row=1)

website_entry_box = Entry(width=35)
website_entry_box.grid(column=1, row=1, columnspan=2)

# == Email/Username Label & Input ==
e_u_label = Label(text='Email/Username: ', font=FONT)
e_u_label.grid(column=0, row=2)

e_u_entry_box = Entry(width=35)
e_u_entry_box.grid(column=1, row=2, columnspan=2)

# == Password Label & Input ==
pw_label = Label(text='Password: ', font=FONT)
pw_label.grid(column=0, row=3)

pw_entry_box = Entry(width=35)
pw_entry_box.grid(column=1, row=3, columnspan=2)

# == Add Button ==
add_btn = Button(text='Add', width=35, command=add, bg='white', highlightthickness=0)
add_btn.grid(column=1, row=4, columnspan=2)
window.mainloop()