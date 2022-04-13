from calculator_art import logo

print(logo)

# ADD


def add(n1, n2):
    return n1 + n2


# SUBTRACT


def subtract(n1, n2):
    return n1 - n2


# MULTIPLY


def multiply(n1, n2):
    return n1 * n2


# DIVIDE


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("Enter the first number "))

for operation in operations:
    print(operation)
operation_symbol = input("Choose an operation from above  ")


num2 = int(input("Enter the second number "))


calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = { first_answer}")

# USING RETURN TO GET HOLD OF FIRST ANSWER TO DO NEXT OPERATION BY USING IT AS AN INPUT TO ANOTHER FUNCTION CALL

operation_symbol = input("Choose an operation from above  ")
num3 = int(input("Enter the next number "))
calculation_function = operations[operation_symbol]
second_answer = calculation_function(first_answer, num3)
print(f"{first_answer} {operation_symbol} {num3} = { second_answer}")

# continue_calculation = True
# while continue_calculation:
#     should_continue = input("Do you want to continue with {second_answer}? type 'y' for yes and 'n' to exit")
#     if should_continue == "y":
#         operation_symbol = input(" choose an operation: ")
#         num_n = int(input("Enter the next number "))
#         calculation_function = operations[operation_symbol]
#         third_answer = calculation_function(second_answer, num_n)
#         return f"{second_answer} {operation_symbol} {num_n} = { third_answer}")
# if should_continue == "n":
#     continue_calculation = False
