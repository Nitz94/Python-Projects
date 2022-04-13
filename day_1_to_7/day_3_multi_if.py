print("Welcome to the Roller coaster!!")
height = int(input("Enter your height in cm "))
bill = 0

if height >= 120:
 print ("You can ride the Roller coaster!")
 age = int(input("What is your age? "))
 if age<12:
     bill = 5
     print("child tickets arw $5")
 elif age <=18:
     bill = 7

     print("youth tickets are $7")
 elif age>=45 and age<=55:
     print(" your tickets are free")
 else:
     bill = 12
     print(" adult tickets are $12")
 wants_photo = input("do you want a photo taken? Y or N ")
 if wants_photo == "Y":
     bill += 3
     print(f"your final bill is {bill}")
else:
 print("sorry you have to grow more to ride this Roller coaster")