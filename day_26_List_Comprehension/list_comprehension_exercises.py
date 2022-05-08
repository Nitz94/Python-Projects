
#
# new_list = []
# for n in numbers:
#     add_1 = n+1
#     new_list.append(add_1)

# LIST COMPREHENSION : CREATING A LIST FROM A PREVIOUS LIST. can be used instead of regular for loops to simplify code

# SYNTAX new_list = [new_item for item in list]


# numbers = [1, 2, 3, 4]
#
# new_list_c = [n+1 for n in numbers]
# print(new_list_c)

# list comprehension works with python sequences which are lists, range, strings, tuple because they have an order

# name = "Nithin"
# new_list_3 = [letter for letter in name]
# print(new_list_3)


# names = ['Alex', 'Eleanor', 'Beth', 'Freddie', 'Dave', 'Caroline']

# short_names = [name for name in names if len(name) < 5]
# print(short_names)

# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)
# range_list = [number * 2 for number in range(1, 10)]
# print(range_list)

# EXERCISE 1 SQUARED NUMBERS
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
#
# # Write your 1 line code 👇 below:
# squared_numbers = [number**2 for number in numbers]
# # Write your code 👆 above:
# print(squared_numbers)


# EXERCISE 2 FILTERING EVEN NUMBERS
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
# even_numbers = [number for number in numbers if number % 2 == 0]
# print(even_numbers)

# EXERCISE 3 DATA OVERLAP
# with open("file_1.txt") as file_1:
#     data1 = file_1.readlines()
#
# with open("file_2.txt") as file_2:
#     data2 = file_2.readlines()
#
# repeating_number = [int(number) for number in data1 if number in data2]
# print(repeating_number)


# DICTIONARY COMPREHENSION
# create a new dictionary from the values from another list or dictionary

# syntax is new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict,item}

# names = ['Alex', 'Eleanor', 'Beth', 'Freddie', 'Dave', 'Caroline']
# import random
# students_scores = {student:random.randint(0,100) for students in names}

# creating a new dict using values from an existing dict
# passed_students = {student:score for (student,score) in students_scores.items() if score > 60}
