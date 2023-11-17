#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b
x=100
y=100 * (80/100) * (120/100)
if y > x:
    print("y is greater than x")
else:
    print("x is greater than y")
#you have to use intendation after if statement - tab

#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

a= "car"
b= "car"
print(a)
print(b)
if a==b:
    print("a is equal to b")
elif a!=b:
    print("a and b are not equal")

#else statement works if statements written above are not correct
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#one line statemnets:
if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")

a=20
b=40
c=84
if b<c and a<b:
   print("correct")

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#or is used when at least one condition is correct, but we use and when both conditions are correct

a=60
b=34.5
if not b>a:
   print("b is not greater than a")

#nested if
x=60
if x > 20:
   print("is more than 20")
   if x > 40:
      print("is also more than 40!")
   else:
      print("is not more than 40")

#არ იცი რა ჩაწერო და ერორიც არ დაგიწეროს:
a = 33
b = 200

if b > a:
  pass