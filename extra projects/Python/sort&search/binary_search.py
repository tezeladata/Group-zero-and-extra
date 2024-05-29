import math
import random
from timeit import default_timer as timer

def binarysearch(sorted_cabinet, looking_for):
    guess = math.floor(len(sorted_cabinet) / 2)
    upperbound = len(sorted_cabinet)
    lowerbound = 0
    steps = 0

    while abs(sorted_cabinet[guess] - looking_for) > 0.0001:  # Loop until the guess is close enough to the target
        steps += 1
        if sorted_cabinet[guess] > looking_for:
            upperbound = guess
        else:
            lowerbound = guess + 1
        
        guess = math.floor((upperbound + lowerbound) / 2)

        # If bounds overlap, it means the element is not found
        if lowerbound >= upperbound:
            return -1, steps

    return guess, steps

def generate_res():
    # To generate array
    length = int(input("How many elements do you want in your array: "))
    user_arr = sorted([random.randint(-100000, 100000) for _ in range(length)])

    # Choose a random element to search for
    look_for = random.choice(user_arr)

    # For exact timing
    start = timer()
    guess, steps = binarysearch(user_arr, look_for)
    end = timer()
    difference = end - start

    # Result
    return f"{user_arr}\n\nBinary search algorithm needed {difference:.6f} seconds and {steps} steps to find index of {look_for}: {guess} in the array above"

print(generate_res())