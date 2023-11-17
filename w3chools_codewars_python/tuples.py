#A tuple is a collection which is ordered and unchangeable.
tuple_1 = ("gold", "iron", "saphyre")
print(tuple_1)
#Tuple items are indexed, the first item has index [0].
#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
#Tuples can have same values in it
tuple_2 = ("car", "bicycle", "helicopter", "car")
print(len(tuple_2))
#one item tuples still contain comma
tuple_3 = ("name",)
print(type(tuple_3))
#constructing tuple
tuple_4 = tuple(("hello",))
print(type(tuple_4))

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.

tuple_2 = ("car", "bicycle", "helicopter", "car")
print(tuple_2[0])
print(tuple_2[-3])
print(tuple_2[1:3])
if "car" in tuple_2:
    print("car is in tuple_2")

#updating tuple
tuple_1 = ("gold", "iron", "saphyre")
list_1 = list(tuple_1)
list_1[1] = "diamond"
tuple_1 = tuple(list_1)
print(tuple_1)

#append() იგივეა რაც დამატება
tuple_1 = ("gold", "iron", "saphyre")
list_1 = list(tuple_1)
list_1.append("emerald")
tuple_1 = tuple(list_1)
print(tuple_1)

#adding tuple to tuple
tuple_5 = ("bmw", "mercedes", "audi")
tuple_6 = ("ford", "chevrolet", "gmc")
tuple_5 +=tuple_6
print(tuple_5)

#removing items using lists
tuple_1 = ("gold", "iron", "saphyre")
list_2 = list(tuple_1)
list_2.remove("gold")
tuple_1=tuple(list_2)
print(tuple_1)

#tuple_2= ("car", "bicycle", "helicopter", "car")
#del tuple_2
#print(tuple_2)
#this will raise an error because the tuple no longer exists

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

tuple_2 = ("car", "bicycle", "helicopter", "car")
i=0
while i<len(tuple_2):
   print(tuple_2)
   i+=1

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

tuple_7 = ("3", "1", "4", "1", "5", "9")
tuple_8 = tuple_7 * 4
print(tuple_8)