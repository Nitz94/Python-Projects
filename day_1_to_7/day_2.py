# num_char=len(input(" what is your name"))
# new_num_char = str(num_char)
# print( "your name has"+ new_num_char + "characters")

# print(70 +float("100.5"))
# 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[1])
# sum = first_digit + second_digit
# print(sum)


# print( 3*(3 +3) /3 -3 )
# 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Body_Mass_Index = float(weight) / (float(height) ** 2 )
# BMI_as_integer = int(Body_Mass_Index)
# print(BMI_as_integer)

# print("""testing message for
# multiple line message
# display""")

# score=0
# height=1.8
# iswinning=True
# print(f"your score is {score}, your height is {height}, yuu are winning is {iswinning}")

# 🚨 Don't change the code below 👇
# age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# your_age=int(age)
# age_in_months = your_age*12
# age_in_weeks = your_age*52
# age_in_days = your_age*365
#
# age_in_days_at90 = 90*365
# age_in_months_at90 = 90*12
# age_in_weeks_at90 = 90*52

# age_left_in_days = age_in_days_at90-age_in_days
# age_left_in_weeks = age_in_weeks_at90-age_in_weeks
# age_left_in_months = age_in_months_at90-age_in_months
# print(f"you have {age_left_in_days} days, {age_left_in_weeks} weeks, {age_left_in_months} months left")

#OR

# years_remaining = 90-your_age
# days_remaining = years_remaining*365
# weeks_remaining = years_remaining*52
# months_remaining = years_remaining*12
# message=f"""" you have {years_remaining} years,
#                        {months_remaining} months,
#                        {weeks_remaining} weeks,
#                        {days_remaining}days remaining till 90"""
# print(message)

#TIP CALCULATOR PROJECT

welcome_message = "Welcome To The Tip Calculator"
print(welcome_message)
bill = float(input("What was the total bill? $ "))
tip = int(input("What percentage tip would you like to give? 10, 12 , or 15? "))
people = int(input("How many people to split the bill? "))
# bill_with_tip = tip/100 * bill+bill
tip_as_percentage = tip / 100
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${bill_per_person}")









