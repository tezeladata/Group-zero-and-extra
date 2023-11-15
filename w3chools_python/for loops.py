#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
cars = ["ford", "ferrari", "lamborgini", "pagani"]
for y in cars:
    print(y)

for x in "apple":
    print(x)

#With the break statement we can stop the loop before it has looped through all the items:
cars = ["ford", "ferrari", "lamborgini", "pagani"]
for x in cars:
    print(x)
    if x=="ferrari":
        break

cars = ["ford", "ferrari", "lamborgini", "pagani"]
for x in cars:
    if x=="ferrari":
        break
    print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(3):
    print(x)

for x in range(2, 7):
    print(x)

#third number defines what value is added
for x in range(2, 30, 3):
  print(x)

#Printing numbers from 2 to 17, and printing a message when the loop ends:
for x in range(2, 17):
   print(x)
else:
   print("finished")

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

numbers1 = ["3", "7", "27"]
numbers2 = ["5", "234", "32"]
for x in numbers1:
   for y in numbers2:
      print(x, y)

#loop with no content
for x in range(2, 5):
   pass