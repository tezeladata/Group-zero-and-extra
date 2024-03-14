# Revise
plus_four = lambda x: x+4
print(plus_four(4))
cap = lambda word: word.capitalize()
print(cap("hello world!"))

# The map() function applies a specified function to every element in an iterable, like lists or tuples.
times_two = lambda x: x*2
num_list = (3, 4, 2, 6, 8, 3, 10)

# print(list(map(times_two, num_list)))
updated_num_list = map(times_two, num_list) # First function name, then list. This variable is not list
updated_num_list = list(updated_num_list) # Now it's a list
print(updated_num_list)

word_list = ("david", "andria", "gio", "vato")
upper_words = lambda word: word.upper()
updated_word_list = list(map(upper_words, word_list))
print(updated_word_list)



prices = [25.99, 14.50, 8.75, 19.95]
# def discount(price):
#   discounted_price = price * 0.9
#   return discounted_price

# discounted_prices = list(map(discount, prices))
# Better with lambda
discounter = lambda x: x*0.9
print(list(map(discounter, prices)))

# The map function requires the first argument to be a function and the second argument to be an iterable.
def is_best(word):
    if word=="GOA" or word=="Goal-oriented academy":
        return True
    else:
        return False
academy_list=("Novatori", "Bitcamp", "GOA")
print(list(map(is_best, academy_list)))

# Better
nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(list(map(lambda x: x*2, nums)))

# The filter() function, just like the map() function, takes in a function and an iterable as arguments. 
# The key purpose of filter() is to apply a condition specified in the provided function to each item in the iterable 
# and return only those for which the function evaluates to True.

nums = (2, 4, 5, 78, 34, 1, 33, 12, 232, 5, 66)
print(list(filter(lambda num: num > 10, nums)))

products = {'Table': 110, 'Sofa': 120, 'Chair': 45, 'Lamp': 70}
filtered = dict(filter(lambda item: item[1] < 90, products.items()))
print(filtered)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
nums = (2, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31)
print(list(filter(is_prime, nums)))