# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# opening and reading file from input folder
PLACEHOLDER = "[name]"
# read files() method reads and convert the text into a list. each line is an item in that list
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()


with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
# replace method replaces the string with another string and creates a new string
    # strip method takes away spaces from before and after the string
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        # opening target directory and creating individual letters as the loop runs through names list
        with open(f"./Output/letter_for_{stripped_name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)   # new letter written into completed letter in each loop
