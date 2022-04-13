################------OLD CODE----###############################
# import random
# from higher_lower_art import logo
# from higher_lower_art import vs
# from game_data import data  # get hold of the data list   # from game_data import data


# # import higher lower logo
# continue_game = True
# while continue_game:
#     print(logo)

#     # generate and display a random name_1, who is name_1,where is name_1 from
#     name_1 = random.choice(data)
#     name_a = name_1["name"]
#     description_a = name_1["description"]
#     country_a = name_1["country"]
#     A = f"{name_a}. a {description_a}, from {country_a}"
#     print(f" Compare A: {A}")

#     # import vs logo
#     print(vs)

#     # generate and display a random name_2, who is name_2,where is name_2 from
#     name_2 = random.choice(data)
#     name_b = name_2["name"]
#     description_b = name_2["description"]
#     country_b = name_2["country"]
#     B = f"{name_b}. a {description_b}, from {country_b}"
#     print(f" Against B: {B}")
#     # ask the user if name_2 is higher or lower
#     user_choice = input("Who has more followers? Type 'A' or 'B': ")
#     # if the user is correct say that use is right and give next set name_2 becomes name_1 for the new iteration
#     if user_choice == "A":
#         name_1["follower_count"] > name_2["follower_count"]
#         print("you are right")
#         name_1 = name_2
#     elif user_choice == "B":
#         name_2["follower_count"] > name_1["follower_count"]
#         print("you are right")
#         name_2 = name_1
#     else:
#         print("you are wrong")
# # find a way to repeat this if user inputs are true

# # track the usr score and display it

# # if user input is wrong, stop the game and display a message


####_________________FINAL VERSION___________________####

from higher_lower_art import logo, vs
from game_data import data
import random

# Format the account data into printable format
def format_data(account):
    """Format the account data into a printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and return if they got it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Display art
print(logo)
score = 0

game_should_continue = True
account_b = random.choice(data)

# Make the game repeatable
while game_should_continue:

    # Generate a random account from the game data # Making account at position B become next position A
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followes 'A' or 'B' : ").lower()

    # Check if user is correct

    # get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess
    # Score keeping

    if is_correct:
        score += 1
        print(f"You're right! Current score : {score}")
    else:
        game_should_continue = False
        print(f"Sorry, you're wrong. Final score: {score}")


# clear the screen between the rounds
