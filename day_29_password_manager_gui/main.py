from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]  # list comprehension
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)  # joins strings

    password_input.insert(0, password)  # pasting the password in entry box
    pyperclip.copy(password)   # copies strings into clipboard
    # print(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()   # getting hold of entries
    email = email_user_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:  # checking if there are empty entries
        messagebox.showinfo(title="Missing Fields", message="Please don't leave any fields empty")
    else:
        # shows a popup window right after clicking add button
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                                              f" Email/User: {email}" f"\n "f"Password: {password}\n"
                                                              f" is it ok to save")
        if is_ok:
            with open("data.txt", "a") as data_file:   # creating and saving the entries in a file
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)     # deleting entries after adding to file to improve ui experience
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)   # sets the canvas to place items
lock_img = PhotoImage(file="logo.png")   # reads the location of logo and saves it to a variable
canvas.create_image(100, 100, image=lock_img)  # placing the image at the center
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_user_label = Label(text="Email/Username:")
email_user_label.grid(column=0, row=2)

password_label = Label(text=f"Password:")
password_label.grid(column=0, row=3)

# Buttons
gen_pass_button = Button(text="Generate Password", command=generate_password)
gen_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)  # column span will extend the item to desired number of columns

# Entries
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()   # puts cursor on the entry

email_user_input = Entry(width=35)
email_user_input.grid(column=1, row=2, columnspan=2)
email_user_input.insert(0, "enter email address")   # inserts text in entry. takes index and string

password_input = Entry(width=25)
password_input.grid(column=1, row=3)

window.mainloop()
