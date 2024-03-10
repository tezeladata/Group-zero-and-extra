# Sets, unlike lists and tuples, are unordered collections. They are created with curly brackets { }.
names = {"David", "Andria", "Giorgi", "Vato"}
print(names)

# Sets do not support indexing
# print(names[1]) #error

# Sets do not have duplicates, so they become handy when working on big data bases
numbers = [1, 34, 2, 5, 77, 5, 2, 5, 5, 1, 1, 1, 64, 34]
numbers = set(numbers)
numbers = list(numbers)
print(numbers)

# Like lists and tuples, sets can have values with different data types.
set1 = {"Bmw", "E34", 1994, 5.7}
print(set1)
# Sets are mutable, which means that you can add and remove items.
set1.add("Germany")
set1.remove(5.7)
print(set1)

# The append() function works only with ordered collection types, like lists, and adds an item to the end of the collection. 
# Sets are unordered, that's why you can't use it on them.
# set1.append("Something here") #error

# Clear function does not depend on any order and removes all items in set
set1.clear()
print(set1) #empty set

# We can combine different sets, but after joining them, duplicates will be ommited.
set2={"a", "b", "c", "d"}
set3={"c", "d", "e", "f"}
set4=set2.union(set3) #duplicates still remain
print(set4)

# Difference returns items that are in one set and not in another
print(set2.difference(set3))