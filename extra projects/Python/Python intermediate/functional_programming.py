# Functions in Python play a crucial role in enhancing the efficiency, reusability, and organization of code.
# def welcome(name):
#   return "Welcome, " + name
# greet = welcome
# print(greet("David"))

def welcome(name):
  return "Welcome, " + name
def processing_user(name, func):
  return func(name)
print(processing_user("David", welcome))

def multiply_by_two(num):
    return num*2
def multiply_by_three(num, func):
    return func(num * 3)
print(multiply_by_three(5, multiply_by_two))


def order(dish):
    return "Your order: " + dish
def process_order(dish, func):
    print(func(dish))
print(process_order("Spaghetti", order))

# An important concept in Functional Programming is Pure Functions.
# A function is called pure if it gives the same result every time you give it the same inputs, 
# and it doesn't affect anything outside of the function.
# Pure function should only return value, not print it

# def greet(name):
#    return "Welcome " + name
# print(greet("David"))

# Creating function with lambda
greet = lambda name: "Welcome " + name
print(greet("David"))

# Lambda expressions are functions without a name that are quick to create and use. 
# They are written in just one line using the lambda keyword and are often used for small, simple tasks.

multiply_by_two = lambda x: x*2
print(multiply_by_two(51))

# You can assign the lambda expression to a variable and then call it as a regular function.
area = lambda width, height : width*height
#                             expression
print(area(100, 200))

# Lambdas execute single, concise expressions. 
# They are more limited than regular functions, which can have multiple lines and actions, and are ideal for straightforward, simple operations.

# Adding argument on-fly-by
new_func = (lambda x, y: x*y*4) (4, 5)
print(new_func)
uppercase = (lambda new_str: new_str.upper()) ("abcd")
print(uppercase)