from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


try:
    # reading csv file to access words
    data = pandas.read_csv("data/words_to_learn.csv.csv")

except FileNotFoundError:
    original_data = pandas.read_csv("data/German Words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")  # splits the data into multiple dictionaries as per the order in csv file


def next_card():
    global current_card, flip_timer    # to access this in flip_card function
    window.after_cancel(flip_timer)    # stopping timer till the user lands on a card and weights 3 sec
    current_card = random.choice(to_learn)   # selecting a random word from csv file
    # print(current_card["German"])# configuring what item to change and what thing to configur about it
    canvas.itemconfig(card_title, text="German", fill="green")
    canvas.itemconfig(card_word, text=current_card["German"], fill="green")
    canvas.itemconfig(card_background, image=card_front)  # going back to front side again after flipping the card
    flip_timer = window.after(3000, func=flip_card)  # setting timer again


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    # getting corresponding eng word from current card dict
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)  # configuring card_background to flip side


def is_known():   # removes the known card from the list of words to display
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)


window = Tk()
window.title("FLASHY")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# delaying card before flipping
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)  # width and height of the image
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=0)

wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=1)

next_card()  # calling before mainloop to show the next card at start instead of placeholder words "text" and "word"

window.mainloop()
