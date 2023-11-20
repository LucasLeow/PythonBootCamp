import json
import random
from tkinter import *
from tkinter import messagebox  # messagebox not a class, not imported in *

# ---------------------------- CONSTANTS ------------------------------- #
FONT = ('Arial', 12, 'normal')
output_path = 'data.json'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pw_entry_box.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list = password_list + [random.choice(symbols) for _ in range(nr_symbols)]
    password_list = password_list + [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    pw_entry_box.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_text = website_entry_box.get()
    email_text = e_u_entry_box.get()
    pw_text = pw_entry_box.get()

    if len(website_text) == 0:
        messagebox.showinfo(title='error', message='Website cannot be empty')
        return

    if len(pw_text) == 0:
        messagebox.showinfo(title='error', message='Password cannot be empty')
        return

    # file_text = f"{website_text} | {email_text} | {pw_text}\n"
    json_data = {
        website_text: {
            'email': email_text,
            'password': pw_text
        }
    }

    is_ok = messagebox.askokcancel(title=website_text, message=f"These are the details entered: \n"
                                                               f"Website: {website_text}\n"
                                                               f"Email: {email_text}\n"
                                                               f"Password: {pw_text}\n"
                                                               f"Is it ok to save?")

    if is_ok:
        website_entry_box.delete(0, END)
        pw_entry_box.delete(0, END)

        e_u_entry_box.delete(0, END)  # reset email field in case it was modified
        e_u_entry_box.insert(0, string='@yahoo.com.sg')

        try:
            with open(output_path, 'r') as r_file:
                exist_data = json.load(r_file)
                exist_data.update(json_data)

        except FileNotFoundError:
            with open(output_path, 'w') as w_file:
                json.dump(json_data, w_file, indent=4)

        except json.decoder.JSONDecodeError:  # json file empty initially
            with open(output_path, 'w') as w_file:
                json.dump(json_data, w_file, indent=4)

        else:
            with open(output_path, 'w') as w_file:
                json.dump(exist_data, w_file, indent=4)

        finally:
            messagebox.showinfo(title='success', message='Details saved successfully')


# ---------------------------- Search Details ------------------------------- #
def search():
    website_text = website_entry_box.get()
    if len(website_text) == 0:
        messagebox.showinfo(title='error', message='Website cannot be empty')
        return

    try:
        with open(output_path, 'r') as r_file:
            exist_data = json.load(r_file)
            messagebox.showinfo(title=website_text,
                                message=f"Email: {exist_data[website_text]['email']} \n"
                                        f"Password: {exist_data[website_text]['password']}")

    except FileNotFoundError:
        messagebox.showinfo(title='error', message='No Data File Found')
        return
        # with open(output_path, 'w') as w_file: # create JSON file if not exist
        #     pass

    except KeyError:
        messagebox.showinfo(title='error', message='No details for website found')
        return


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

website_entry_box = Entry(width=27)
website_entry_box.focus()
website_entry_box.grid(column=1, row=1)

search_btn = Button(text='Search', command=search, bg='white', width=15)
search_btn.grid(column=2, row=1)

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
