print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


a=5000
b=6000
c=1.2
if b / a == c:
    print ("6000/5000=1.2")
else:
   print("you don't know math")


#The bool() function allows you to evaluate any value, and give you True or False in return
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15
print(bool(x))
print(bool(y))

x=2
x=2.5
print(bool(x))

x=0
print(bool(x))

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


#Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


x = 200
print(isinstance(x, int))

y = "MJ"
print(isinstance(y, int))