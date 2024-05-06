import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    tries = 0

    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"is {guess} too low(l), too high(h) or correct(c)? - ").lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

        tries += 1
    
    print(f"Correct one, computer guessed your number - {guess}. You needed {tries} tries!")

computer_guess(1000)