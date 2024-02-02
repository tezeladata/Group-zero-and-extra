#With the while loop we can execute a set of statements as long as a condition is true.
# while 2>1:
#     print("Two is greater than one") infinite loop

#adding counter
counter=0
while counter>-3:
    print(counter)
    counter-=1

#With the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#With the else statement we can run a block of code once when the condition no longer is true:
i=0
while i<4:
   print(i)
   i+=1
else:
   print("i is no longer less than 4")

#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#looping in str
string="Hello"
for i in string:
   print(i)
#break statement
string="abracadabra"
for i in string:
   print(i)
   if i=="c":
      break

#To loop through a set of code a specified number of times, we can use the range() function,
#            start, end, step(iteration)
for i in range(2, 4343, 342):
   print(i)

#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for i in range(1, 7, 2):
   print(i)
else:
   print("code ended")

#A nested loop is a loop inside a loop.
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)