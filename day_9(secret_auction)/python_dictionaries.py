# DICTIONARY HAS A KEY : AND ITS VALUE

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",

}

# Retrieving items from a dictionary:
# print(programming_dictionary["Loop"])


# Adding new items to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again"


# Create an empty dictionary
# empty_dictionary = {}


#Wipe an existiing dictionary
# programming_dictionary = {}


#Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer"


#Loop through a dictionary
# for key in programming_dictionary:
    # print(key)  # gives only keys
    # print(programming_dictionary[key])

# NESTING

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# NESTING A LIST IN A DICTIONARY

travel_log = {
    "France": ["Paris", "Dijon", "Cannes"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

#NESTING A DICTIONARY INSIDE A DICTIONARY

travel_log = {
    "France": {"cities_visited": ["Paris", "Dijon", "Cannes"], "total_visits": 15},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# NESTING DICTIONARY IN A LIST

travel_log = [
    {
        "Country": "France",
        "cities_visited": ["Paris", "Dijon", "Cannes"],
        "total_visits": 15
    },
    {
        "Country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
]