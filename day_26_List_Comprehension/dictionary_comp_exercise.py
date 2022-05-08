# create a dictionary that takes each word in the given sentence and calculates the number of letters in each word.

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"  # split gives a list of words in a list
# # Don't change code above 👆
# sentence_list = sentence.split()
#
# # Write your code below:
#
# result = {word: len(word) for word in sentence_list}
#
# print(result)


# use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature
# in degrees Celsius and converts it into degrees Fahrenheit.


# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
# weather_f = {day: (temp_c * 9/5) + 32 for(day, temp_c) in weather_c.items()}   # items() mtd gives all items in the dict
#
# # Write your code 👇 below:
#
# print(weather_f)
