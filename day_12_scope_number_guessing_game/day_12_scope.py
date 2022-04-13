################### Scope ####################

enemies = 1


def increase_enemies():
    # enemies = 2
    print(f"enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Local scope: exists within the function or indented inside the function
# When a variable ofr a function is defined within a function that variable
# is only accessable or can be used only from within that function.

# Global Scope: variables defined on top or outside a function can be accessed from anywhere

# This property is called namespace. if you name anything it has a namespace


# DO not try to modify global variables inside a function as it may lead to bugs and confusion,
# instead change it by returning the value and later assigning it to global variableS

# Global constants are variables which are defined and never going to change or modify the value eg. mathematical or scientific constants.
# By convension these global variables are named in UPPERCASE and separated with _
