#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.
#  lambda      argument  :         expression
a= lambda      a         :         a**2
print(a(34))

x= lambda x:x+2
print(x(54))

#Lambda functions can take any number of arguments:
i = lambda a,b : a//b
print(i(45,3))

x= lambda a,b,c : a**2 + b**2 + c**2
print(x(43, 22, 11))

def func1(n):
    return lambda x: x*n
multiplication=func1(34)
print(multiplication(44))