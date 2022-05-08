from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=600, height=500)
window.config(padx=75, pady=75)
# adding labels
my_label = Label(text="THIS IS A LABEL", font=("Segoi", 24, "bold"))  # font is a tuple (f_name, size, type)
my_label.grid(column=0, row=0)  # this will display the label in gui program
# my_label.pack(side="left") # can be configured to left right or bottom
# my_label.pack(expand=True) # use entire height and width of available screen size

# my_label["text"] = "New Label" # components can be modified like a dictionary item
my_label.config(text="New label 2")  # configure,change or update properties of a particular components that we created
my_label.config(padx=45, pady=45)

# Buttons

def button_clicked():
    new_input = window_input.get()
    my_label.config(text=new_input)


button = Button(text="Click Me", command=button_clicked)  # command takes function name without parenthesis
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)



# Entry

window_input = Entry(width=10)
window_input.grid(column=3, row=2)
print(window_input.get())




# # Other Widgets
#
# # Text
# text = Text(height=5, width=30)
# # Puts cursor in textbox.
# text.focus()
# # Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# # Gets current value in textbox at line 1,  from character 0
# print(text.get("1.0", END))
# text.pack()
#
#
# # Spinbox
# def spinbox_used():
#     # gets the current value in spinbox.
#     print(spinbox.get())
#
#
# spinbox = Spinbox(from_=-10, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
#
# # Scale
# # Called with current scale value.
# def scale_used(value):
#     print(value)
#
#
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
#
# # Checkbutton
# def checkbutton_used():
#     # Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
#
#
# # variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
#
# # Radiobutton
# def radio_used():
#     print(radio_state.get())
#
#
# # Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
# # Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#     my_label.config(text=listbox.get(listbox.curselection()))
#
#
# listbox = Listbox(height=7)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()


window.mainloop()  # keeps the window running
