from tkinter import *


window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

FONT = ('Arial', 14)

usr_input = Entry(width=7)
usr_input.grid(column=1, row=0)

miles_label = Label(text='Miles', font=FONT)
miles_label.grid(column=2, row=0)

converted_label = Label(text="is equal to", font=FONT)
converted_label.grid(column=0, row=1)

converted_2_label = Label(text="0", font=FONT)
converted_2_label.grid(column=1, row=1)

converted_3_label = Label(text="Km", font=FONT)
converted_3_label.grid(column=2, row=1)

def convert_miles():
    usr_input_miles = float(usr_input.get())
    converted_km = round(usr_input_miles * 1.60934)
    converted_2_label.config(text=f"{converted_km}")

calc_btn = Button(text='Calculate', command=convert_miles)
calc_btn.grid(column=1, row=2)

window.mainloop()
