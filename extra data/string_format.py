# optional method that gives users more control when displaying output

# {} is called format field

name = "David"
age = 16

# Basic
print("Hello " + name + ", you are", age, "years old!")

# .format
print("Hello {} you are {} years old".format(name, age))

# We can also write indexes inside curly braces
print("{1} {0} {3} {2}".format(name, age, name, age)) # Positional arguments

# Keyword arguments
print("{name} was released in {year}".format(name="Harry Potter", year=1997))

# Other way
text = ("{first} {last}")
print(text.format(first = "Hello", last = "World!"))

# format padding
print("Hello, my name is {:>10}".format(name)) # Right allign
print("Hello, my name is {:<10}".format(name)) # Left allign
print("Hello, my name is {:^10}".format(name)) # Center allign
# If we want to add positional or keyword argument before padding, we have to write it before colon
print("Hello, my name is {name:^20} nice to meet you".format(name="David"))

# Number digits:
number = 3.14159
print("Your number is {:.2f}".format(number))
# f is for floating point, 2 is number of digits we want after the dot
print("Your number is {:.3f}".format(number))
print("Your number is {:.4f}".format(number))
# It also round digits

# Adding comma:
number = 1000
print("Your number is {:,}".format(number))
# Automatically added comma after 1

# Binary representation of number:
print("Binary of {0} is {0:b}".format(number))
# b for binary

# Octal representation of number:
print("Binary of {0} is {0:o}".format(number))
# o for binary

# Hexadecimal representation of number:
print("Binary of {0} is {0:x}".format(number))
# x for lowercase hex
print("Binary of {0} is {0:X}".format(number))
# X for uppercase hex


# Task:
def personal_info():
    name = input("Enter name: ")
    phone = int(input("Enter phone: "))
    email = input("Enter email: ")
    age = int(input("Enter age: "))
    address = input("Enter address: ")

    print("\nContact Information:\n\nName: {0}\nPhone: {1}\nEmail: {2}\nAge: {3} ({3:b})\nAddress: {4}".format(name, phone, email, age, address))
# personal_info()


# Task2:
def print_formatted(number):
    width = len(bin(number)[2:])  # Determine the width needed for binary representation
    for i in range(1, number+1):
        decimal = str(i).rjust(width)  # Right align the decimal number
        octal = oct(i)[2:].rjust(width)  # Right align the octal number
        hexadecimal = hex(i)[2:].upper().rjust(width)  # Right align the hexadecimal number
        binary = bin(i)[2:].rjust(width)  # Right align the binary number
        print(f"{decimal.rjust(width)}{octal.rjust(width+1)}{hexadecimal.rjust(width+1)}{binary.rjust(width+1)}")

print_formatted(10)