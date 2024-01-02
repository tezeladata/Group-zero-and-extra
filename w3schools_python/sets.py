#Sets are used to store multiple items in a single variable.
#Set items are unordered, unchangeable, and do not allow duplicate values.
# Sets are written with curly brackets.
set1={"A", "B", "C", "D"}
print(type(set1))
print(set1)

#if we have duplicates
set1={"A", "B", "C", "D", "D", "A"}
print(set1)
#False and 0 is same. Also, True and 1 is same.
#Set items can be of any data type

#It is also possible to use the set() constructor to make a set.
set2=set((123, 34, 65))
print(type(set2))    #note the double round-brackets

#You cannot access items in a set by referring to an index or a key.
#But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
set1={"A", "B", "C", "D"}
for x in set1:
    print(x)

#cheking:
print("A" in set1)

#adding items:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
#adding from another set
set3={"Bmw", "Audi", "Porsche"}
set4={"Ferrari", "Pagani", "Alfa Romeo"}
set3.update(set4)
print(set3)
#We can also use union
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
#Both union() and update() will exclude any duplicate items.
#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

#To remove an item in a set, use the remove(), or the discard() method.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#if you want to remove random item, yoy can use pop()
thisset = {"apple", "banana", "cherry"}
thisset.pop()
print(thisset)

#The intersection_update() method will keep only the items that are present in both sets.
set5={23, 44, 12, 434, 56}
set6={343, 54, 34, 43,23}
set5.intersection_update(set6)
print(set5)
#The intersection() method will return a new set, that only contains the items that are present in both sets.
set5={23, 44, 12, 434, 56, 3, 55, 787}
set6={343, 54, 34, 43, 23, 4, 787, 3}
set7=set5.intersection(set6)
print(set7)

#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

#The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
