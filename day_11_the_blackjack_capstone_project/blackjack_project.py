import random

from blackjack_art import logo


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Returns a random card from the deck"""
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Takes the list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


# following conditions are evaluated top to bottom, function created during final step of comparing scores.
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "DRAW"
    elif computer_score == 0:
        return " LOST, OPPONENT HAS BLACKJACK"
    elif user_score == 0:
        return " WIN. WITH A BLACKJACK"
    elif user_score > 21:
        return " YOU WENT OVER, YOU LOSE"
    elif computer_score > 21:
        return "OPPONENT WENT OVER. YOU WIN"
    elif user_score > computer_score:
        return "YOU WIN"
    else:
        return " YOU LOSE"


# this function is the whole game and it is created at the final part of the process for the convenience
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    # using append to add item to list. to use extend or += the item itself has to be list.
    for _ in range(2):
        # new_card = deal_card()
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")

        # Checks if the list has blackjack or end of game
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # checking if computer has blackjack or the score is less than 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    YOUR FINAL HAND: {user_cards}, FINAL SCORE: {user_score}")
    print(f"    COMPUTER'S FINAL HAND: {computer_cards}, FINAL SCORE {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
