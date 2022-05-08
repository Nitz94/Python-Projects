# opening a file with open() method and saving it to a variable
# file = open("my_file.txt")

# reading the contents in the file using read() method and saving it to a variable
# contents = file.read()

# printing the contents
# print(contents)

# closing the file. closing the opened file is always recommended
# file.close()

# Alternatively a file can be opened with 'with' keyword

# with open("my_file.txt") as file:  # closes the file automatically after we are done with it, no need for close method
#     contents = file.read()
#     print(contents)


# writing to a file. open method has parameter mode "r" read only by default
# "w" to write.this will delete the current text and replaced with new one
# "a" appends the new text to current text just like list append
# with open("my_file.txt", mode="a") as file:
#     contents = file.write("\nNew text")
#
# if you open a file with write mode and that file do not exist the method will create the file for you.
# with open("new_file.txt", mode="w") as file:
# contents = file.write("Create a new file")

# this only works in write mode

# working with files and directories
# forward slash / for each folder or directories
# root folder is just /
# using absolute path
# with open("/Users/Nithin A N/Desktop/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# using relative path ../ for going back in a path

with open("../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

# absolute path is relative to root that is usually C in windows
# relative path is relative to current working directory
