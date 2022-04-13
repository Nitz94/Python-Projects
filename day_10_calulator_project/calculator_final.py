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


def calculator():

    num1 = float(input("Enter the first number: "))

    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if (
            input(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
            )
            == "y"
        ):
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
