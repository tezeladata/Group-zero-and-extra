# Function arguments can also be functions, for example:
def person_name(name):
    return name + " lives in Tbilisi"
def name_output(name, func):
    print(func(name))

name_output("David", person_name)

# Functions can also be nested in python
def outer_function():
    print("Hello from outer function")

    def inner_function():
        print("Hello from inner function")
outer_function()

# You can also return result of nested function inside parent function
def greet(name):
    print(f"Hello {name}!")
    def account_creator():
        return f"Account created for {name}"
    message = account_creator()
    print(message)

greet("David")

# If you don't want to alter the original function's result, you can create a decorator, which will work on changing that result
def welcome():
    return "hello world!"

def uppercase():
    def wrapper(func):
        res = func()
        res = res.upper()
        return res
    return wrapper
print(uppercase()(welcome))
#                nested function

# First function will return square of number, second function will return fourth power of original number
def square(num):
    return num ** 2

def fourth():
    def changer(func):
        def inner(num):
            squared_num = func(num) 
            fourth_pow = squared_num ** 2
            return fourth_pow
        return inner
    return changer

print(square(5))
print(fourth()(square)(5))