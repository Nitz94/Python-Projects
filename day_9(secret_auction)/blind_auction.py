
##################STILL HAVEN'T FOUND A BETTER WAY TO CLEAR THE RUN SCREEN BY CODE. FIX IT########################

from blind_auction_art import logo
print(logo)


from os import system, name


# # define our clear function
# def clear():
#     # for windows the name is 'nt'
#     if name == 'nt':
#         _ = system('cls')
#
#     # and for mac and linux, the os.name is 'posix'
#     else:
#         _ = system('clear')





########################OLD CODE##################################################
# should_continue = True
# while should_continue:
#     bidder_name = input("What is your name?\n")
#     bid_amount = input("What is your bid?\n$")
#     auction_entry = []
#     for entry in auction_entry:
#         auction_entry.append(auction_entry[bidder_name] = bid_amount)
#     keep_bidding = input("Is there any another bidder? type 'yes' or 'no'\n")
#     if keep_bidding == "no":
#         should_continue = False
# print(auction_entry)
##################################################################################

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner =""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid=bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Are there anu other bidders? Type 'yes or 'no'.")
    if should_continue =="no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print(""*100)
        # clear()

print(bids)



















