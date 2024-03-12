# Exceptions often arise from a variety of causes, including invalid input, 
# out-of-bounds indices, incompatible type operations, and logical errors in the code.

# SyntaxError - invalid syntax, NameError - variable is not defined, IndexError - index is out of range, TypeError - incorrect argument, ValueError - incorrect value

# The sum() function only works with iterables containing numerical data types (int or float).
# prices = [250, 300, "240", 400] 
# total = sum(prices) #TypeError
# print(total)

# The try block holds code that might cause an exception. If an exception occurs, execution of the try block stops, and the except block is executed, allowing the program to continue running.
prices = [250, 300, "240", 400] 
try:
    total = sum(prices) #TypeError
    print(total)
except TypeError:
    print("Invalid argument")
print("Correct")
# Exception handling allows you to prevent program failure by processing potential exceptions in the way you need.

# color = "Green"
# try:
#   print(size)
# except NameError:
#   print("Check the variable name")

# You can have multiple except blocks to handle each possible exception specifically.
prices = [250, 300, "240", 400] 
try:
    total = sum(prices) #TypeError
    print(total)
except TypeError:
    print("Invalid argument")
except IndexError:
    print("Index out of range")
finally:
    print("No errors remaining")


# You can only use except and not error type but code block's algorithm won't be clear
# You can use the finally statement to perform an operation after the try/except block, no matter if an exception occurred or not.
prices = [250, 300, "240", 400] 
try:
    total = sum(prices) #TypeError
    print(total)
except TypeError:
    print("Invalid argument")
except IndexError:
    print("Index out of range")

# We can use use else statement with try/except block, but it will only work if there will be no errors
# We can manually raise errors
num1 = int(input("Enter number from 20 to 40: "))
if num1<20 or num1>40:
    raise ValueError("Number has to be in 20 to 40 range")