#Tuples are used to store multiple items in a single variable.
#A tuple is a collection which is ordered and unchangeable.
#Tuple items are ordered, unchangeable, and allow duplicate values.
#Tuples allow duplicate values:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#len for length
print(len(thistuple))
#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
tuple1=("Hello",)
print(type(tuple1))
#Tuple items can be of any data type
#A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")
#It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#accesing items:
tuple2=(123, 434, 1223)
print(tuple2[2])
print(tuple2[-2])
#it is same with lists for ranges

#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
tuple3=("A", "B", "C", "D")
a=list(tuple3)
a[3]="E"
tuple3=a
print(tuple3)

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

#unpacking
tuple6=("Bmw", "Ford", "Ferrari", "Nissan")
(german, american, italian, jaapnese) = tuple6
print(german, italian)
#using asterisk-*, remaining values will be assigned to the variable, which has *
tuple2=(123, 434, 1223, 23423, 22)
(first, second, *third)=tuple2
print(third)