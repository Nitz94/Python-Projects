import random
from number_guesser_art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# 1 choosing  a random number between 1 and 100

# 4 function to check users's guess against actual number/# 5 Track the number of turns and reduce by 1 if they get it wrong
def check_answer(guess, answer, turns):
    """Checks the guess against answer and returns the number of turns remaining"""
    if guess < answer:
        print("Too Low")
        return turns - 1
    elif guess > answer:
        print("Too high")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")


# 2 make function to set difficulty
def set_difficulty():
    level = input("Choose your difficulty, Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("Welcome to the number guessing game")
    print("I'm thinking of a number between 1 and 100 can you find it?")
    answer = random.randint(1, 100)
    # print(f"psst the number is {answer}")

    turns = set_difficulty()

    # 6 repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        # 3 let the user guess a number
        guess = int(input("Make a Guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out op attempts, you lose")
            return
        elif guess != answer:
            print("Guess again: ")


game()
