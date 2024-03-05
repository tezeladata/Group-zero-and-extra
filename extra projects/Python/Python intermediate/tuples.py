# Collection is a data type that holds multiple items

# Examples of data types:
name = "David" #str
age = 16 #int
data = ["David", "Tezelashvili", "Tbilisi"] #list

# Indexing:
print(name[2], data[2])

# List it mutable (ცვალებადი) so it's data can be changed:
data.append("Georgia")
data[0]="Andria"
print(data)

# Tuples, like lists, are ordered collections of items created with parentheses.
user2 = ("John", "Smith", 32, "USA")
print(user2)
# The items in tuples also have their indexes, starting from 0. You can access the items in tuples just like you do with lists.
print(user2[1][2])

# Tuples are immutable.
# They are useful when the data stored in collections shouldn't be accidentally modified during the program execution:
# In other words:
# tuples are a fundamental collection type used for storing an ordered sequence of items that should remain unchanged.


# user2[1]="Rock" #Error, because tuple's data cannot be changed
# print(user2)

ids = (1906, 9371, 8237, 3901) #tuple
users = ["Mery", "Anna", "Bob"] #list
message = "Registered" #str
print(type(ids), type(users), type(message))

# Tuples, like lists, can contain duplicate elements.
ages = (11, 12, 13, 14, 11, 15, 11, 23, 22, 19)
# We use count() to count specifical elements in tuples:
print(ages.count(11))

# Many other functions can be used with tuples, but they cannot modify them
print(len(ages))
# Max for maximum value
print(max(ages))

# We can use tuples in control flow:
points = (11, 12, 9, 8, 7, 12, 6, 5, 21)
for i in points:
    if i>10:
        print ("passed")

# Tuple unpacking for creating variables:
birthday_date = (1, 3, 2008)
day, month, year = birthday_date
print(year, month, day)

# While unpacking, number of variables should match the length of tuple

# The * operator in tuple unpacking is used to gather multiple elements from the tuple into a list. 
# This is useful when dealing with tuples of unknown length.
academy = ("GOA", "Mziuri", "Novatori", "Bitcamp", "Reeducate")
best, *others = academy
print(best) #str
print(others) #list
# the * operator in tuple unpacking allows for flexible assignment of elements to variables
