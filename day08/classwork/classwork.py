name="data"
print(name[2])

nums = [3, 5, 9, 24]
print(nums[0:2])

words = ["His", "name", "is", "David"]
print(words[0])
print(words[1])
print(words[2])
print(words[3])

x = ["a", "b", "c"]
y = [1, 2, 3, 4, 5]
print(x[1])
print(y[3])

y = ["1", "2", "3", "4", "5"]
print((int(y[2])) + (int(y[4])))

#2 განზომილებიანი ცხრილი - მატრიცა
m = [
    [1, 2, 3],
    [4, 5, 6]
    ]
print(m)

m = [
[1, 2, 3],
[4, 5, 6]
]

print(m[1][2])

x = [
[2, 4, 6],
[8, 10, 12],
[14, 16, 18]
]
#second line
print(x[1])
#second line's last element
print(x[1][2])

things = ["text", 0, [1, 2, 8], 4.56]
print(things[2][2])

my_str = "Hello world!"
         #0123456
print(my_str[6])

my_str = "hello world"
print(my_str[6])

nums = [5, 8, 2]
nums[1] = 42
print(nums)

#2

nums = [1, 2, 3, 4, 5]
nums[3] = nums[1]
print(nums[3])

#concatenation - გაერთიანება
nums = [1, 2, 3]
print(nums + [4, 5, 6])

x = [2, 4]
x += [6, 8]
print(x)
print(x[2]//x[0])

nums = [1, 2, 3]
print(nums * 3)

#boolean
words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

#7
nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5 #მენულე ადგილზე მყოფი გადაიქცევა პირველ ადგილის ელემენტს გამოკლებული 5
if 4 in nums: #თუ 4 მოცემულია ცვლად nums-ში
  print(nums[3]) #დაიპრინტოს ცვლად nums-ის მესამე ელემენტი
else: #თუარადა
  print(nums[4]) #დაიპრინტოს ცვლადის მეოთხე ელემენტი


nums = [1, 2, 3]
print(not 4 in nums) #4 არ არის ცვლადში რაც სწორია
print(4 not in nums) #93-ე ხაზის მსგავსია
print(not 3 in nums) #არასწორია რადგან 3 მოცემული გვაქვს ცვლადში
print(3 not in nums) #ისევ არასწორია

words = ["hello", "world", "spam", "eggs"]
for word in words:
  print(word + "!")

i=0 #საიტერაციო ცვლადის შექმნა
while i<10:
   print(i)
   i+=1 #ინკრემენტაცია

for i in range (1,20,3): #3-ით იზრდება 
    print(i)

for char in "დათა":
   print(char)


my_list = ["bmw", "audi", "porsche", "mercedes"]
for element in my_list:
   print(element)