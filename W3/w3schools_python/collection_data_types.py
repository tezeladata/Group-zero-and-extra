# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.



#lists
#Lists are created using square brackets.
#The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
#Lists allow duplicates
#List items can be of any data type:
my_list1=[True, False, 23, "Hello", 343.23]
print(my_list1)
#Another way to have list:
my_list3=list(("234", 454, 23.1459, "Hello", True))    #we have to use double brackets
print(my_list3, type(my_list3))
#slicing:
print(my_list3[2:4])
print(my_list3[:3])    #not including item with index number 3
print(my_list3[1:])
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list



#tuples
#tuples are opened with brackets
#Tuples are used to store multiple items in a single variable.
#A tuple is a collection which is ordered and unchangeable.
#Tuple items are ordered, unchangeable, and allow duplicate values.
#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
tuple1=("Hello",)
print(type(tuple1))
#Tuple items can be of any data type
#A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")
#It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
#unpacking
tuple6=("Bmw", "Ford", "Ferrari", "Nissan")
(german, american, italian, jaapnese) = tuple6
print(german, italian)
#adding items
#convert to list, append, convert to tuple
#or add tuple to tuple
tuple3=("A", "B", "C", "D")
tuple4=("E", "F", "G", "H")
tuple5=tuple3+tuple4
print(tuple5)
#deleting items
#convert to list, remove, convert to tuple
#if we want to delete tuple completely, we use del
tuple4=("E", "F", "G", "H")
del tuple4
#print(tuple4)
#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found



#sets
#Sets are used to store multiple items in a single variable.
#Set items are unordered, unchangeable, and do not allow duplicate values
#Sets are written with curly brackets.
#Set items can be of any data type
#It is also possible to use the set() constructor to make a set.
set1=set((123, 34, 65))
print(type(set1))    #note the double round-brackets
#Once a set is created, you cannot change its items, but you can add new items.
#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
#Both union() and update() will exclude any duplicate items.
# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others



#dictionaries
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
dict1={
    "brand": "bmw",
    "model": "e92",
    "year": 2005
}
print(dict1)
#Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
#Duplicate values will overwrite existing values:
dict1={
    "brand": "bmw",
    "model": "5 series",
    "year": 1972,
    "year": 2023
}
print(dict1["year"]) #it overwrited
#The values in dictionary items can be of any data type
#It is also possible to use the dict() constructor to make a dictionary.
dict2=dict(Name = "David", Age= 15)
print(dict2)
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary
