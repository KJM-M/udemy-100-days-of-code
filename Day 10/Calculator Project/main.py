from art import logo
print(logo)

n1 = float(input("Enter first number: "))
print("+\n-\n*\n/\n")
operator = input("Enter operator: ")
n2 = float(input("Enter second number: "))

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

go_again = True

while go_again:
    result = operations.get(operator)(n1, n2)
    print(f"\n{n1} {operator} {n2} = {result}")
    continue_with_current_result = input(f"\nType 'y' to continue calculating with {result},\nType 'n' to start a new calculation,\nType 'q' to quit program. ").lower()

    if continue_with_current_result == "y":
        n1 = result
        print("+\n-\n*\n/\n")
        operator = input("Enter operator: ")
        n2 = float(input("Enter second number: "))

    elif continue_with_current_result == "n":
        n1 = float(input("Enter first number: "))
        print("+\n-\n*\n/\n")
        operator = input("Enter operator: ")
        n2 = float(input("Enter second number: "))

    elif continue_with_current_result == "q":
        go_again = False


# Solution

# import art
#
#
# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def divide(n1, n2):
#     return n1 / n2
#
#
# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide,
# }
#
# # print(operations["*"](4, 8))
#
#
# def calculator():
#     print(art.logo)
#     should_accumulate = True
#     num1 = float(input("What is the first number?: "))
#
#     while should_accumulate:
#         for symbol in operations:
#             print(symbol)
#         operation_symbol = input("Pick an operation: ")
#         num2 = float(input("What is the next number?: "))
#         answer = operations[operation_symbol](num1, num2)
#         print(f"{num1} {operation_symbol} {num2} = {answer}")
#
#         choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
#
#         if choice == "y":
#             num1 = answer
#         else:
#             should_accumulate = False
#             print("\n" * 20)
#             calculator()
#
#
# calculator()