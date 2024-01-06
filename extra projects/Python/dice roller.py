import random
print("Hello, this is dice roller")
rolls=int(input("How many times do you want to roll dice: "))

for i in range(rolls):
    num_of_dice=int(input("1/2 dice: "))
    values=[1,2,3,4,5,6]
    first=random.choice(values)
    second=random.choice(values)
    if num_of_dice!=1 and num_of_dice!=2:
        print("Incorrect amount of dice")
    elif num_of_dice==1:
        print("Result is:", first)
    elif num_of_dice==2:
        sum=first+second
        print("result is:", first, "+", second, "=", sum)


