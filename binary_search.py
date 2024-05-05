import random
import time

def binary_search(user_list, target_number, low = None, high = None):
    # Setting low and high bounds
    if low is None:
        low = 0
    if high is None:
        high = len(user_list) -1

    if high < low:
        return f"{target_number} not in your list"

    # This algortihm uses midpoints instead of analyzing every item
    midpoint = (low + high) // 2

    # Main algorithm:
    if user_list[midpoint] == target_number:
        return midpoint # Returning index of this number
    elif user_list[midpoint] < target_number:
        return binary_search(user_list, target_number, low, midpoint - 1)
    else: # when user_list[midpoint] > target_number
        return binary_search(user_list, target_number, midpoint + 1, high)