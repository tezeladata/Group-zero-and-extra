nums = [1, 3, 5, 2, 4, 3]
print(len(nums)) #len - სიის სიგრძე

surname = ["Keshelava"]
print(len(surname))
#difference
surname = "Keshelava"
print(len(surname))

set_of_nums = set(nums)
print(set_of_nums)

age=10
age+=5 #5 ემატება
print(age)

str = "some text"
x = len(str)
print(x) #str-ს სიგრძის დათვლა

nums = [1, 2, 3] #nums სია
nums.append(20) #append - დამატება, ამატებს სიის ბოლოში
print(nums)

words = ["Python", "fun"]
words.insert(1, "is") #სასურველი ელემენტის ჩასმა მითითებულ პოზიციაზე
#       სად ჩაჯდეს, რა ჩაჯდეს
print(words)

names=["Shalva", "Nino"]
names.insert(1, "Data")
names.append("Andria")
print(names)

nums = [9, 8, 7, 6, 5] # შეიქმნა სია
nums.append(4) #ბოლოში დაემატა 4
nums.insert(2, 11) #მეორე პოზიციაზე დაემატა 11
print(len(nums))

letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r')) #პირველად აღმოჩენილი "r"-ს პოზიცია - 2
print(letters.index('p')) #0
print(letters.index('q')) #1

x = [1, 8, 42, 3]
print(min(x)) #x-სიის მინიმალური რიცხვი
print(max(x)) #x-სიის მაქსიმალური რიცხვი

x = [2, 4, 6, 2, 7, 2, 9]
print(x.count(2)) # x სიაში ითვლის 2 რამდენჯერაა
x.remove(4) #წაშლის 4-ს x სიიდან
print(x)
x.reverse() #სიის შებრუნება
print(x)

# embed - ჩანერგვა

nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)

members = ["ნინო", "შალვა", "ირინა", "ანდრია", "დათა"]
fam = "ჩემი დედა - {0}, ჩემი მამაა - {1}, მე ვარ - {2}".format(members[0], members[1],members[4])
print(fam)

a="My name is {0}, and my surname is {1}".format("David", "Tezelashvili.")
print(a)
#or
a="My name is {}, and my surname is {}".format("David", "Tezelashvili.")
print(a)