# List comprehensions are useful shorthands for such operations. 
#They offer a shorter and more readable way to create lists with various settings using just a single line of code.

# longer version:
nums = []
for i in range(51):
    nums.append(i)
# Better one:
nums = [x for x in range(51)]

# List comprehensions are created using square brackets []

# <variable>: the variable that will store the newly created list
# <expression>: an expression performed on each item. If no specific action is needed, the item itself is used
# <item>: the current item being processed
# <iterable>: any iterable object, such as ranges, lists, strings, tuples, and sets
# variable = [expression for item in iterable]


# Adding hashtag to all items:
names = ["David", "Andria", "Oto"]
hashtag_arr = ["#" + i for i in names]
print(hashtag_arr)
lower_arr = [x.lower() for x in names]
print(lower_arr)

# Using if statement
evens = [x for x in range(11) if x%2==0]
print(evens)