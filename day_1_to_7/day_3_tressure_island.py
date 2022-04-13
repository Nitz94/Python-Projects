print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
#Write your code below this line 👇
choice1=input('you\'re at a crossroad which way do yo want to go? type"left" or "right"').lower()
if choice1=="left":
   choice2=input('you\'ve come to a river, to cross it do you want to "swim" or "wait" for a a boat').lower()
   if choice2=="wait":
       choice3=input('you\'ve reached other side you see a house with three doors red blue and yellow,'
                     ' which one do you want to open?')
       if choice3=="yellow":
           print('you reached the tressure. YOU WON')
       elif choice3=="blue":
           print("you were attacked by a monster.GAME OVER")
       elif choice3=="red":
           print('the room is on fire.GAME OVER')
       else:
           print('you selected a room which do not exist.GAME OVER')
   else:
       print('a crocodile got you GAME OVER')
else:
    print('you fell into a hole and GAME OVER')



































