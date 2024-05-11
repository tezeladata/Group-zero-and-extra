def manual_sort(lst, reverse=False, key=None):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")

    if key and not callable(key):
        raise TypeError("Key function must be callable")

    sorted_lst = lst[:]  # Create a copy of the input list
    for _ in range(len(sorted_lst)):
        for i in range(len(sorted_lst) - 1):
            if sorted_lst[i] > sorted_lst[i + 1]:
                sorted_lst[i], sorted_lst[i + 1] = sorted_lst[i + 1], sorted_lst[i]

    if key:
        sorted_lst = [key(item) for item in sorted_lst]

    if reverse:
        sorted_lst.reverse()

    return sorted_lst

def key_func(val):
    return val ** 2

print(manual_sort([1, 231, 324234, 2243, 45], True, key_func))
print(manual_sort([1, 231, 324234, 2243, 45], True))
print(manual_sort([1, 231, 324234, 2243, 45]))