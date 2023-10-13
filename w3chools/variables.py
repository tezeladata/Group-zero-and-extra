#if
if 5 > 2:
    print("Five is greater than two!")
#tab უნდა გამოვიყენო 


if 5 > 2:
    print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!")
#tab-ის 2-ჯერ გამოყენებაც შეიძლება

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")
# """ - multiline string - კომენტარის ჩაწერა ასეც შეიძლება

x = 5
y = "John"
print(x)
print(y)
#variables

x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)
#specify

x = 5
y = "John"
print(type(x))
print(type(y))
# type() გიჩვენებს კოდის ტიპს


#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (age, Age and AGE are three different variables)
#A variable name cannot be any of the Python keywords.

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# variable-ს ჩაწერის ახალი გზა

x = y = z = "Orange"

print(x)
print(y)
print(z)


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)


x = 5
y = 10
print(x + y)

x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()


x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)


def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
# global ფუნქციით x variable ეკუთვნის მთლიან კოდს


x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
# x="fantastic" გადაეწერა x="awesome"-ს