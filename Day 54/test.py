## Functions can have inputs/functionality/output
# def add (n1, n2):
#     return n1 + n2
# def sub (n1, n2):
#     return n1 - n2
# def mul (n1, n2):
#     return n1 * n2
# def div (n1, n2):
#     return n1 / n2


## Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.
# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)
#
# result = calculate(add, 2, 3)
# print(result)


## Functions can be nested in other functions
# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm nested")
#
#     return nested_function
#
# outer_function()


## Functions can be returned from other functions
# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm nested")
#
#     return nested_function
#
# inner_function = outer_function()
# inner_function()



# import time
#
# def delay_decorator(function):
#     def wrapped_function():
#         time.sleep(2)
#         # Do something before
#         function()
#         # Do something after
#     return wrapped_function
#
# @delay_decorator
# def say_hello():
#     print("Hello")
#
# @delay_decorator
# def say_bye():
#     print("Bye")
#
# @delay_decorator
# def say_greeting():
#     print("How are you?")
#
# decorated_function = delay_decorator(say_greeting)
# decorated_function()


import time

current_time = time.time()
# print(current_time)  # seconds since Jan 1st, 1970


# Write your code below 👇

def speed_calc_decorator(function):
    def wrapper_function():
        start = time.time()
        function()
        end = time.time()

        print(end - start)
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


decorated_function = speed_calc_decorator(slow_function)
decorated_function()



