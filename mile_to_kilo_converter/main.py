from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)


def convert():
    miles = float(miles_entry.get())
    km = round(miles * 1.60934)
    answer_label.config(text=km)


miles_entry = Entry(width=10)
miles_entry.insert(END, string="0")
miles_entry.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equals_label = Label(text="is equal to")
equals_label.grid(row=1, column=0)

answer_label = Label(text="0")
answer_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

button = Button(text="Calculate", command=convert)
button.grid(row=2, column=1)

window.mainloop()
