from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
FONT = ('Arial', 12, 'normal')
output_path = 'data.txt'
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_text = website_entry_box.get()
    email_text = e_u_entry_box.get()
    pw_text = pw_entry_box.get()

    file_text = f"{website_text} | {email_text} | {pw_text}\n"

    website_entry_box.delete(0, END)
    pw_entry_box.delete(0, END)

    with open(output_path, 'a') as d_file:
        d_file.writelines(file_text)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# == Canvas setup (Lock Image) ==
canvas = Canvas(width=200, height=200)

lock_bg = PhotoImage(file='logo.png')
canvas.create_image((100, 100), image=lock_bg)

canvas.grid(column=1, row=0)

# == Website Label & Input ==
website_label = Label(text='Website:', font=FONT)
website_label.grid(column=0, row=1)

website_entry_box = Entry(width=45)
website_entry_box.focus()
website_entry_box.grid(column=1, row=1, columnspan=2)

# == Email/Username Label & Input ==
e_u_label = Label(text='Email/Username: ', font=FONT)
e_u_label.grid(column=0, row=2)

e_u_entry_box = Entry(width=45)
e_u_entry_box.insert(0, string='@yahoo.com.sg')
e_u_entry_box.grid(column=1, row=2, columnspan=2)

# == Password Label & Input ==
pw_label = Label(text='Password: ', font=FONT)
pw_label.grid(column=0, row=3)

pw_entry_box = Entry(width=27)
pw_entry_box.grid(column=1, row=3)

pw_btn = Button(text='Generate Password', command=generate_password, bg='white')
pw_btn.grid(column=2, row=3)

# == Add Button ==
add_btn = Button(text='Add', width=40, command=save, bg='white', highlightthickness=0)
add_btn.grid(column=1, row=4, columnspan=2)
window.mainloop()