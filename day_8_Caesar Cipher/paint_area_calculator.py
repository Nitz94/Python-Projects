#Write your code below this line 👇
import math
def paint_calc(height, width, cover):
    no_of_cans=(test_h*test_w)/coverage  #area=w*h & no_of_cans=math.ceil(area/coverage)
    no_of_cans=math.ceil(no_of_cans)
    print(f"total number of cans needed : {no_of_cans}")







#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
