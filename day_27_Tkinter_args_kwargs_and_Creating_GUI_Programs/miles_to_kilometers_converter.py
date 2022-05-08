from tkinter import *

window = Tk()
window.title("Miles To Kilometers Converter")
window.minsize(width=500, height=200)
window.config(padx=120, pady=50)

label_1 = Label(text="is equal to", font=("Segoi", 15, "bold"))
label_1.grid(column=0, row=1)


miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

label_miles = Label(text="Miles", font=("Segoi", 13, "bold"))
label_miles.grid(column=2, row=0)

label_ans_km = Label(text="0", font=("Segoi", 12, "bold"))
label_ans_km.grid(column=1, row=1)

label_km = Label(text="Km", font=("Segoi", 13, "bold"))
label_km.grid(column=2, row=1)


def button_clicked():
    miles = float(miles_input.get())
    convert = round(miles * 1.609)
    label_ans_km.config(text=f"{convert}")


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
