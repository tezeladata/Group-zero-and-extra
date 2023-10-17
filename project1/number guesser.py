import random
print("This is random number generator from 1 to 10")
print("Try to guess this number")
comp_numb = random.randrange(1,10)
user_numb = int(input("your number: "))
while comp_numb != user_numb:
    if user_numb < comp_numb:
        print("Too low")
        user_numb = int(input("Enter number again: "))
    elif user_numb > comp_numb:
        print("Too high!")
        user_numb = int(input("Enter number again: "))
    else:
        break
print("You guessed it right")