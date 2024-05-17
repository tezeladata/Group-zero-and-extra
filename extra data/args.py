# parameter that packs all arguments into a tuple
# useful so that a function can accept a varying amount of arguments

# args now becomes tuple, so indexing is not allowed
def procuct_of_nums(*args):
    product = 1
    for i in args:
        product *= i
    return product
print(procuct_of_nums(1, 4, 5, 3, 2, 1, 3, 4, 5, 6, 10, 34))

# Task:
def find_min_max_difference(*some_numbers):
    some_numbers = list(some_numbers)
    return max(some_numbers) - min(some_numbers)
print(find_min_max_difference(234, 22, 4234, 6456, 678, 3, 5435, 23424))

# Task:
def custom_sort(key, *number_lists):
    res_list = []
    for list in number_lists:
        new_list = []
        for number in list:
            new_list.append(number*key)
        res_list.append(new_list)
    return res_list
print(custom_sort(4, [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]))