# with open("226 weather-data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv  # inbuilt module
# with open("226 weather-data.csv") as data_file:
#     data = csv.reader(data_file)    # creates a csv object which can be looped
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))   # converting string temp to int values
#     print(temperatures)

# import pandas
# data = pandas.read_csv("226 weather-data.csv")
# # data_dict = data.to_dict()    # pandas can convert data into multiple formats like dicts lists html excel etc.
# # print(data_dict)
# data_list = data["temp"].tolist()
# # print(data_list)

# average_temp = sum(data_list)/len(data_list)

# print(average_temp)
# finding average temperature
# avg = data["temp"].mean()  # series methods and attributes are super useful. check pandas documentation
# print(avg)

# finding maximum temperature

# max_temp = data["temp"].max()
# print(max_temp)

# Get data in columns
# print(data["condition"])   # can be worked with as in a dictionary or like an object
# or
# print(data.condition)


# Get data in row
# print(data[data.day == "Monday"])  # looks in data where column name is day and in that colum check for the row monday


# Which row of data has the highest temperature of the week
# print(data[data.temp == data.temp.max()])
# when a particular column is equal to a particular value we get hold of a row
# monday = data[data.day == "Monday"]
# print(monday.condition)

# finding mondays temperature in fahrenheit
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# Create a data frame from scratch

# data_dict = {
#     "Members": ["Snake", "Saitama", "Dutch", "Ripley", "McLain"],
#     "Points": ["93", "99", "92", "98", "90"]
# }
# calling Dataframe class to create data frame for dictionary
# data = pandas.DataFrame(data_dict)
# creating and saving new file. path is the argument
# data.to_csv("new_data.csv")


# CREATE A CSV DATA FILE WHICH HAS THE NUMBER OF SQUIRRELS PER COLOR

# import pandas
# data = pandas.read_csv("Central-Park-Squirrel-Census-Squirrel-Data.csv")
#
# # getting hold of the rows with primary fur colors
# gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# # # once we get hold of rows it is treated like a list and iterable. so functions like len can be used
# #
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# #
# squirrel_color_dict = {
#     "Fur Color": ["Gray", "Black", "Cinnamon"],
#     "Count": [gray_squirrels_count, black_squirrels_count, cinnamon_squirrels_count]
# }
# #
# # # creating data frame and saving it as csv file
# squirrel_data = pandas.DataFrame(squirrel_color_dict)
# squirrel_data.to_csv("Squirrel-Color-Count.csv")

# getting hold of number of all adult squirrels
# adult_squirrels = len(squirrel_data[squirrel_data["Age"] == "Adult"])  # or data.age can be written
# print(adult_squirrels)

import pandas
student_scores = {
    "student": ["student_1", "student_2", "student_3"],
    "scores": [ "75", "80", "73"]
}

# loop through a dictionary
# for (key, value) in student_scores.items():
#     print(value)

student_data_frame = pandas.DataFrame(student_scores)
print(student_data_frame)
# to loop through a  data frame there is an inbuilt method where index and rows of data frame is used for key reference

for(index, rows) in student_data_frame.iterrows():
    # print(rows)
 # # print(rows.student)
 #    print(rows.scores)








