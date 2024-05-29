import math
import random
from timeit import default_timer as timer

steps = 0

# main func:
def mergesort(user_arr):
    global steps

    # Inner func for sorting
    def merging(left,right):
        new_arr = []

        while(min(len(left),len(right)) > 0):
            if left[0] > right[0]:
                to_insert = right.pop(0)
                new_arr.append(to_insert)
            elif left[0] <= right[0]:
                to_insert = left.pop(0)
                new_arr.append(to_insert)

        if(len(left) > 0):
            for i in left:
                new_arr.append(i)
        if(len(right) > 0):
            for i in right:
                new_arr.append(i)

        return new_arr


    # main part
    new_arr = []
    global steps

    if(len(user_arr) == 1):
        new_arr=user_arr
    else:
        left = mergesort(user_arr[:math.floor(len(user_arr)/2)])
        right = mergesort(user_arr[math.floor(len(user_arr)/2):])
        new_arr = merging(left,right)

    steps += 1
    return new_arr


def get_result():
    # For correct count of steps
    global steps
    steps = 0

    # For array length
    length = int(input("How many elements do you want in your array? "))

    # For precise timing
    start = timer()
    res = mergesort([random.randint(-100000, 100000) for _ in range(length)])
    end = timer()
    difference = end - start

    # Final result
    return f"Your sorted array: {res}\nIt took {steps} steps and {difference} seconds for function to get this result"

print(get_result())