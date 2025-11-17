import art

def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2


operations = {
    "+" : addition,
    "-" : subtraction,
    "*" : multiplication,
    "/" : division
}

def calculator():
    print(art.logo)
    loop_continue = True
    first_number = float(input("What is your first number?: "))

    while loop_continue:
        for symbol in operations:
            print(symbol)
        set_operation = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))

        output = operations[set_operation](n1=first_number, n2=second_number)
        print(f"{first_number} {set_operation} {second_number} = {output}")
        user_selection = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ").lower()
        if user_selection == "y":
            first_number = output
        elif user_selection == "n":
            print("\n" * 20)
            calculator()
        else:
            print("Exiting calculator. Have a great day!")
            loop_continue = False

calculator()
