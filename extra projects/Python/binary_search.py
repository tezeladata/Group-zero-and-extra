import random
import time

def binary_search(user_list, target_number):
    low = 0
    high = len(user_list) - 1

    while low <= high:
        midpoint = (low + high) // 2

        if user_list[midpoint] == target_number:
            return midpoint
        elif user_list[midpoint] < target_number:
            low = midpoint + 1
        else: # when user_list[midpoint] > target_number
            high = midpoint - 1
    
    return f"{target_number} not in your list"

# Execution
def main():
    length = 5000000
    sorted_list = list(range(-2500000, 2500001))

    # Using time to know in what time program executed
    start = time.perf_counter()  # Using perf_counter() for precise timing
    res = binary_search(sorted_list, random.randint(-2500000, 2500000))
    end = time.perf_counter()

    if isinstance(res, int):
        print(f"Binary search needed {end - start} seconds to get target index - {res}")
    else:
        print(f"Binary search did not work, because your number is not in list")

main()