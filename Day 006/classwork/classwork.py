print(1 == 1 or 2 == 2)

if (1 == 1) and ( 2 + 2 > 3):
    print("true")
else:
    print("false")

print(1 == 1 or 2!=2)

age = 15
money = 500
if money > 12 or money >100:
    print("welcome")


age=24
limit=18
height=191
if age > limit and height > 180:
    print("valid")

age=24
limit=18
height=174
print(age > limit and height > 180)

age=15
limit=18
height=190
if age > limit and height > 180:
    print("valid")
else:
    print("დაბალი ხარ ან პატარა")


#age=int(input("your age: "))
#limit=18
#height=int(input("yout height: "))
#if age>limit and height > 180:
#    print("მაღალიც და ზრდასრულიც")
#elif age>limit and height<180:
    print("ზრდასრული, მაგრამ დაბალი")
#elif age<limit and height<180:
#    print("დაბალი და პატარა")
#elif age<limit and height>180:
#    print("პატარა, მაგრამ მაღალი")
#else:
#    print("ვერც ერთ კრიტერიუმს ვერ აკმაყოფილებ")

print(not 1==1)

if not True:
    print("1")
elif not (1+1 ==3):
    print("2")
else:
    print("3")

for i in range(5):
  print("Hello")
print("Goodbye")

country = "US"
age = 42
if (country == "US" or country == "GB") and (age > 0 and age < 100):
    print("cool")

hour=9
day=23
print(hour> 12 and day <=15 or hour < 10)
print((hour> 12 and day <=15) or hour < 10)

#საიტერაციო ცვლადი - განმრეორება (ფუძე იტერაცია)

i=1
while i<=5:
    print(i)
    i=i+1
print("finished")