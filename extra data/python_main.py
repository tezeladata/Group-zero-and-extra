import math

# The simplest directive in Python is the "print" directive - it simply prints out a line

# Python uses indentation for blocks, instead of curly braces:
print("Hello world!")
if 1 == 1:
    # code block
    print("Join GOA")



# Python is completely object oriented, and not "statically typed". You do not need to declare variables before using them, or declare their type.

# Python accepts two types of numbers: integers, floats (decimals) and complex numbers

# To define int, we can write code like this:
money = 50
# variable name, declaring operator and variable data

# If we want to declare float:
money2 = float(money)
# else:
money3 = 50.0

# Strings are defined either with a single quote or a double quotes.
# Any data, that is placed in quotes, is called string - text data

name = "David"
print(name)

# The difference between the two is that using double quotes makes it easy to include apostrophes:
print("Hello, I'm David")

# We can work with strings easily:
first_part = "Hello"
second_part = " "
third_part = "World!"
# Now we can concatenate these strings:
print(first_part + second_part + third_part)

# Assignments can be done on more than one variable
a, b = 10, 20
print(a, b)

c, d, e, f = 30, 40, 50, 60
print(c, d, e, f)

# Mixing operators between numbers and strings is not supported:
# print("Hello" + 5 + "world!")

# but we can turn any non-string into string:
print("Hello" + str(5) + "world!")



# Lists can contain any type of variable, and they can contain as many variables as you wish. Lists can also be iterated over in a very simple manner.
try:
    list1 = ["a", 10, 3.14, True, math.sqrt(-1)]
except ValueError:
    print("Imaginary number")

# We can add any element in list:
list2 = [1, 2, 3, 4, 5]

# Adding to last index:
list2.append(10)
print(list2)

# Adding to any index:
list2.insert(2, 15)
#        index, value

# Changing element at specified index:
list2[1] = 10
print(list2)

# Using loop to print out every element of our list:
for element in list2:
    print(element)

# Accessing an index which does not exist generates an exception (an error).
try:
    print(list2[10])
except IndexError:
    print(f"Not valid index, nearest is: {list2[-1]}")



# Just as any other programming languages, the addition, subtraction, multiplication, and division operators can be used with numbers.
print(((1 + 2) * (5/ 2)) + 8/2)

# Another operator available is the modulo (%) operator, which returns the integer remainder of the division. dividend % divisor = remainder.
for x in range(1, 11):
    print(x, x%2)

# When we use two multiplication symbols, we use power:
print(2 ** 5)

# We can use addition symbol if we want to concatenate strings:
print("Hello" + " " + "World!")

# Python also supports multiplying strings to form a string with a repeating sequence:
print("Hello " * 10)

# Addition operator can also be used when we want to join lists
list3 = [1, 2, 3, 4, 5]
list4 = [6, 7, 8, 9, 10]
print(list3 + list4)

# Just like strings, we can also multiplicate lists
print(list3 * 5)



# Let's say you have a variable called "name" with your user name in it, and you would then like to print
name = "David"
print("Hello %s!" % name)

# To use two or more argument specifiers, use a tuple (parentheses):
age = 16
print("Hello %s, you are %d years old!" % (name, age))

# Any object which is not a string can be formatted using the %s operator as well.
list1 = [2000, 1800, 2500]
print("Wages of some peope are %s" % list1)

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

print("Hex for 150 is %x" % 150)

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."
print(format_string % data)



# Basic string operations
full_name = "David Tezelashvili"

# Length of our string
print(len(full_name))

# Finding indexes of some characters
print(full_name.find("a"))
# It returned index of the character in full_name string

print(full_name.find("g"))
# -1 if that character is not present in full_name string

# Now with index
print(full_name.index("d"))

try:
    full_name.index("g")
except ValueError:
    print("That char not found")

# We simply use count function to count that element in collection
print(full_name.count("a"))

# Reversing strings:
print(full_name[::-1])
print("".join(reversed(full_name)))

# Lowercase and uppercase:
print("abcd".upper())
print("abcd".upper().lower())

# Returning booleans:
astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))



# Python uses boolean logic to evaluate conditions. The boolean values True and False are returned when an expression is compared or evaluated.
print(3 > 3)
print(3 != 3)
print(3 == 3)

# Building a more complex logic:
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

# The "in" operator could be used to check if a specified object exists within an iterable object container
print("a" in "David")
print(5 in [1, 2, 3, 4])

# Using "not" before a boolean expression inverts it
print(not False)
print((not False) or (not True))



# There are two types of loops in Python, for and while.
for i in range(5, 16, 2):
    print(i, i%5 == 0)

count = 0
while count < 10:
    count += 1
print(count)

# break is used to exit a for loop or a while loop, whereas continue is used to skip the current block, and return to the "for" or "while" statement.
i = 0
while i < 10:
    i += 1

    if i == 5:
        break

for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

# If break not given in loop, we can add else:
for x in range(5):
    print(x)
else:
    print(x + 10)



# Functions are a convenient way to divide your code into useful blocks, allowing us to order our code, make it more readable, reuse it and save some time. 
def greet(name):
    return f"Hello, {name}"
print(greet(name = "David"))



# The __init__() function, is a special function that is called when the class is being initiated. It's used for assigning values in a class.
class Car_class:

    variable = "Car constructor"

    def __init__(self, brand, model, year, engine):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine = engine

    def return_all(self):
        return f"Brand: {self.brand}, model: {self.model}, year: {self.year}, engine: {self.engine}"

car1 = Car_class("Bmw", "e92", 2008, 3.0)
print(car1.model)
print(car1.return_all())
print(Car_class.variable)



# A dictionary is a data type similar to arrays, but works with keys and values instead of indexes.
person1 = {
    "name": "David",
    "surname": "Tezelashvili",
    "age": 16,
    "role": "Future mentor"
}

print(person1)

# Dictionaries can be iterated over, just like a list. However, a dictionary, unlike a list, does not keep the order of the values stored in it. To iterate over key value pairs, use the following syntax:
for key, value in person1.items():
    print(f"{key}: {value}")

phone_dict = {
    "David": 592290607,
    "Andria": 577234242,
    "John": 532234082,
    "James": 599453534
}

for name, phone_number in phone_dict.items():
    print("{}: {:x}".format(name, phone_number))

# Ways to delete pair:
del phone_dict["John"]
phone_dict.pop("James")

print(phone_dict)



# Generators are used to create iterators, but with a different approach. Generators are simple functions which return an iterable set of items, one at a time, in a special way.
def get_values():
    yield "Hello world!"
    yield "GOA"
    yield "Programming"

def return_values():
    # This prints out generator object
    print(get_values())

    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    for gen in get_values():
        print(gen)

return_values()

def collatz(user_num):
    while True:
        if user_num%2==0:
            user_num//=2
        else:
            user_num = user_num*3 + 1
        yield user_num

        if user_num == 1:
            break

def get_collatz():
    seq = list(collatz(10))
    print(seq)

get_collatz()

# Generator:
squares = (x**2 for x in range(5))

# When using generator, memory is not allocated on it. But when we want to use it's data, then we'll have to convert result into data type
print(squares)
print(list(squares))

# def fib():
#     a, b = 1, 1
#     while 1:
#         yield a
#         a, b = b, a + b



# List Comprehensions is a very powerful tool, which creates a new list based on another list, in a single, readable line.
print([x**x for x in range(10) if x%2==0])



# we can use python's lambda functions, which are inline functions defined at the same place we use it. So we don't need to declare a function somewhere and revisit the code just for a single time use.
print(list(map(lambda x: x**2, [1, 2, 3, 4, 5])))

print(list(map(lambda x: x%2==0, [2,4,7,3,14,19])))



def do_stuff_with_number(n):
    print(n)

def catch_this():
    the_list = (1, 2, 3, 4, 5)

    for i in range(20):
        try:
            do_stuff_with_number(the_list[i])
        except IndexError: # Raised when accessing a non-existing index of a list
            do_stuff_with_number(0)

catch_this()



print(list(set(["Jake", "John", "Eric"]).difference(set(["John", "Jill"]))))

print(type(type)) 