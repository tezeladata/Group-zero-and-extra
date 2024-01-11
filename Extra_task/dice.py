import random
print("Hello, this is dice roller")
choice=(input("Roll a dice? "))


values=[1,2,3,4,5,6]
if choice=="yes":
    comp=random.choice(values)
    your=random.choice(values)
    print("You rolled:", your, "and computer rolled:", comp)
    if your==comp:
        print("Draw!")
    elif your>comp:
        print("You won!")
    else:
        print("Computer won!")
else:
    print("Good Luck!")