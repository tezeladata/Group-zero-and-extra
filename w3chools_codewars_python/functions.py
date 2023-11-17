#To call a function, use the function name followed by parenthesis:
def function1():
    print("first function")
function1()

def myfunction2(fname):
    print(fname)
myfunction2("david")

def myfunction3(fname, lname):
    print(fname  + " " + lname)
myfunction3("david", "tezelashvili")

#error
#def my_function(fname, lname):
#  print(fname + " " + lname)
#my_function("david")


#  *args
def myfunction4(*best_car):
    print("best car is " + best_car[2])
myfunction4("mercedes", "audi", "bmw")

def myfunction4(car1, car2, car3):
    print(car1 + car2 + car3)
myfunction4(car1="nissan ", car2="toyota ", car3="honda ")

#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
def myfunction4(**cars):
    print("best car is " + cars["car1"])
myfunction4(car1="bmw ", car2="toyota ", car3="honda ")

def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def function5(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
function5(fruits)


#To let a function return a value, use the return statement:
def function6(x):
    return 5 * x
print(function6(4))
print(function6(23))
print(function6(9))

def function7():
    pass

#recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)