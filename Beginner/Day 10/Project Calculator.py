from art import logo

def add(n1, n2):
    """returns the sum of two numbers"""
    return n1 + n2

def sub(n1, n2):
    """returns the subtraction of two numbers"""
    return n1 - n2

def mul(n1, n2):
    """returns the multiplication of two numbers"""
    return n1 * n2

def div(n1, n2):
    """returns the division of two numbers"""
    return n1 / n2

calc_dict = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

# calculation_over = False
# while not calculation_over:
def calculator():
    print(logo)
    ask_number1 = False
    while not ask_number1:
        try:
            number1 = float(input("What is the first number? "))
            ask_number1 = True
        except ValueError:
            print("Wrong input, please enter a valid number.")

    continue_counting = True
    while continue_counting:
        ask_operation = False
        while not ask_operation:
            for symbol in calc_dict:
                print(symbol)
            operation = input("Pick an operation: ")
            if operation != "+" and operation != "-" and operation != "*" and operation != "/":
                print("Wrong input, please enter a valid operation.")
            else:
                ask_operation = True

        ask_number2 = False
        while not ask_number2:
            try:
                number2 = float(input("what is the next number? "))
                ask_number2 = True
            except ValueError:
                print("Wrong input, please enter a valid number.")

        result = calc_dict[operation](number1, number2)
        print(f"{number1} {operation} {number2} = {result}")

        ask_continue = False
        while not ask_continue:
            user_input = input(
                f"type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
            if user_input == "y":
                number1 = result
                ask_continue = True
            elif user_input == "n":
                ask_continue = True
                continue_counting = False
                calculator()
            else:
                print("Wrong input, please enter a valid answer.")

calculator()