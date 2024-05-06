import random

def guess(x_num):
    random_number = random.randint(1, x_num)

    guess = 0
    tries = 0

    while guess != random_number:
        guess = int(input(f"Enter any number from 1 to {x_num}: "))

        if guess < random_number:
            print(f"Your number is too low. Maybe you have to guess in range of 1 - {int((random_number - guess) * 2)}")
        elif guess > random_number:
            print(f"Your number is too high. Maybe you have to guess in range of 1 - {int((guess - random_number) * 2)}")
        tries += 1
    print(f"|  Congrats, you guessed the random number - {random_number}  |\n|  You needed {tries} tries for the result  |")

guess(random.randint(50, 100))

decision = input("Play again?: y / n - ")
 
while decision == "Y" or decision == "y":
    guess(random.randint(50, 100))
    decision = input("Play again?: y / n - ")
print("Thanks for playing!")