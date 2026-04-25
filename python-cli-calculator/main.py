from art import logo

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    first_number = float(input("What's the first number? "))
    lets_continue = True
    while lets_continue:
        for symbol in operations:
            print(symbol)
        
        operation_symbol = input("Pick an operation: ")
        second_number = float(input("What's the second number? "))
        calculate = operations[operation_symbol](first_number, second_number)
        print(f"{first_number} {operation_symbol} {second_number} = {calculate}")

        yes_or_no = input(f"Type 'y' to continue calculating with {calculate}, or "
                          f"type 'n' to start a new calculation: ").lower()
        
        if yes_or_no == "y":
            first_number = calculate
        else:
            lets_continue = False
            print("\n * 20")
            calculator()

calculator()
