#list
n = [8, 42, 7, 0]
print(n)

#nested list, matrix
m = [[1, 2, 3],[4, 5, 6]]
print(m)
print(m[0][2])

str = "My name is David"
print(str[4])

#printing 3rd character
#text = input()
#print(text[2])

#number corresponds with letter
alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
 "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
  "T", "U", "V", "W", "X", "Y", "Z"]
#num1 = int(input())
#num2 = int(input())
#num3 = int(input())
#print(alpha[num1] + alpha[num2] + alpha[num3] )

#უმატებს
nums = [1, 2, 3]
print(nums + [4, 5, 6])

#6 is divided by 2
x = [2, 4]
x += [6, 8]
print(x)
print(x[2]//x[0])

#boolean in lists
words = ["bmw", "audi", "porsche", "aston martin", "range rower"]
print("bmw" in words)
print("nissan" in words)

nums = [1, 2, 3]
print(not 4 in nums) #4 არ არის ცვლადში რაც სწორია
print(4 not in nums) #42-ე ხაზის მსგავსია
print(not 3 in nums) #არასწორია რადგან 3 მოცემული გვაქვს ცვლადში
print(3 not in nums) #ისევ არასწორია

#smart house
supported = ["Lights off", "Lock the door", 
    "Open the door", "Make coffee", "Shut down"]
#command = input()
#if command in supported:
    #print("OK")
#else:
    #print("Unknown")

elements = ["Boron", "Potassium", "Chlorine", "Lead"]
for word in elements:
    print(word + "!")


nums = [4, 7, 3, 1]
for x in nums:
    print(x*2)

#difference between str and int
nums = ["4", "7", "3", "1"]
for x in nums:
    print(x*2)

text = "some text"
for x in text:
  if x == 'e':
    break
  print(x)

#printing sum of list items
x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]
sum= 0
for num in x:
    sum += num
print(sum)

str = "Hello world!"
for x in str:
   if x == "o":
      break
print(x)

words = ["cat", "car", "code", "home", "learn", 
    "fun", "job", "love", "friend", "zoo", "enjoy",
    "happiness", "family", "goal", "desire"]
#letter = input()
for i in words:
#    if letter in i:
        print(i)

#In order to output the range as a list, we need to explicitly convert it to a list, using the list() function.
numbers = list(range(30))
print(numbers)

print(range(20) == range(0, 20))

#third number in range shows us how much value is added
nums = list(range(3, 15, 3))
print(nums[2])

nums = list(range(15, 3, -3))
print(nums)

#printing hello five times
for i in range(5):
  print("hello!")

x = list(range(0, 100))
print(x[4])

#list slices
x = [2,4,6,23,68,23,56,222,654]
print(x[3:7])

#მეშვიდე ელემენტამდე
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2]) #ორის გამოტოვებით
print(squares[2:8:3])


sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[1::4])
# start point is index [1], no end point, print every 4th step from the start. 1, 25, 81


#შებრუნება
elements = ["Boron", "Potassium", "Chlorine", "Lead"]
x = elements[::-1]
print(x)