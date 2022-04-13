# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
#OR YOU CAN COMBINE BOTH NAMES ASSIGN IT AS A SINGLE STRING AND THEN DO THE COUNTING
t = name1.count("t") + name2.count("t")
r = name1.count("r") + name2.count("r")
u = name1.count("u") + name2.count("u")
e = name1.count("e") + name2.count("e")

l = name1.count("l") + name2.count("l")
o = name1.count("o") + name2.count("o")
v = name1.count("v") + name2.count("v")
e2 = name1.count("e") + name2.count("e")

first_number = t+r+u+e
second_number = l+o+v+e2
score = int(str(first_number)+str(second_number))
print(f"your score is {score}")
if (score<=10) or (score>=90):
          print(f"your score is {score}, you two go like coke and mentos")
elif (score>=40) and (score<=50):
    print(f"your score is {score}, you two are alright together")
else:
    print(f"your score is {score}")