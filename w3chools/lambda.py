#A lambda function is a small anonymous function.
i= lambda x: x + 10
print(i(20))

b= lambda i: i/10
print(b(200))

c = lambda a: a*15
print(c(40))

a = lambda b, c: b*c
print(a(40,123))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def func(x):
    return lambda a: a + x
a=func(2)
print(a(34))

#triple the value
def func(n):
    return lambda a: a*n
tripler=func(3)
print(tripler(22))

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))