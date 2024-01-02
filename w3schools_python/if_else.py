# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

if 1==1:
    print("GOA")
else:
    print("Novatori")

#short if
a=1
b=2
print(a) if a > b else print(b)
#This technique is known as Ternary Operators, or Conditional Expressions.

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
b=234
a=23
if not a > b: 
    print(b)

#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
if True==True:
    pass