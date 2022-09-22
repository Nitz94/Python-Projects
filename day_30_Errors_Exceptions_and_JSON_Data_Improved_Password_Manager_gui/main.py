# catching exceptions : try, except, else, finally method

# try : runs the code inside the try block which may generate an exception / error

# except : catches the exception and runs the code inside the except block. if there is a particular error,
# it will be caught and the code inside the except block will be executed. multiple except blocks can be used
# to catch multiple exceptions.

# else : runs the code inside the else block if there is no exception

# finally : runs the code inside the finally_block whether there is an exception or not

# raise : raises your own exception by specifying the exception type and message
#
# try:
#     file = open("a_file.txt")        # if the file do not exist, it will generate an exception
#     a_dictionary = {"key": "value"}  # if the key do not exist, it will generate an exception
#     print(a_dictionary["key"])
#
# except FileNotFoundError:   # for this particular error, the code inside the except block will be executed
#     file = open("a_file.txt", "w")  # a new file will be created
#     file.write("Something")
#
# except KeyError as error_message:  # for this error, the code inside the except block will be executed
#     print(f"The key{error_message} does not exist")
#
# else:  # if there is no exception, the code inside the else block will be executed
#     content = file.read()
#     print(content)
#
# finally:   # this block will always be executed
#     # file.close()
#     # print("File was closed")
#     raise TypeError(" Beep-bop;This is a custom error which I made up")  # this will crash the code no matter what


# raise is used to raise our own exceptions when there is no error in code but some values may be wrong and generate
# an incorrect output
# for example
#
# height = float(input("Height: "))  # if height and weight are unrealistic values, it still gives a result
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human height should be no more than 3m")
#
# bmi = weight / height ** 2
#
# print(f"BMI is {bmi}")


# exercise index error
# fruits = ["Apple", "Pear", "Orange"]
#
# # Catch the exception and make sure the code runs without crashing.
#
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#
#     except IndexError:
#         print("Fruit Pie")
#
#     else:
#         print(fruit + " pie")
#
#
# make_pie(3)


# exercise key error
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
#
# total_likes = 0
#
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#
#     except KeyError:
#         pass
#         # post["Likes"] = 0 # both valid
#         # total_likes += 0
#
#
# print(total_likes)

# JSON - JavaScript Object Notation
# JSON is a lightweight data-interchange format. It is easy for humans to read and write. It is easy for machines
# to parse and generate.
# data is stored in json as a dictionary with keys and values.
# json.dumps() converts a python object to a json string. takes arguments as what to dump and where to dump. w mode
# json.loads() converts a json string to a python object. takes filepath. open in read mode
# json.update() updates the json file with new data. takes filepath and new data. open in write mode
