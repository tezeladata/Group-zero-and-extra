#Lists are used to store multiple items in a single variable.
#Lists are created using square brackets.
my_list1=["A", "B", "C", "D"]
print(my_list1)
#List items are indexed, the first item has index [0], the second item has index [1] etc.
#The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
#Lists allow duplicates
#We use len to check lenght of list
print(len(my_list1))
#List items can be of any data type:
my_list2=[True, False, 23, "Hello", 343.23]
print(my_list2)
#checking class type:
print(type(my_list2))

#another way to have list
my_list3=list(("234", 454, 23.1459, "Hello", True))    #we have to use double brackets
print(my_list3, type(my_list3))

#list items:
print(my_list3[3])
#negative indexs:
print(my_list3[-1])
#slicing:
print(my_list3[2:4])
print(my_list3[:3])    #not including item with index number 3
print(my_list3[1:])

#changing items in list
my_list3=list(("234", 454, 23.1459, "Hello", True))
my_list3[1]=3.14
print(my_list3)
#using ranges:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
thislist[1:2]=["A", "B"]
print(thislist)
#adding items:
thislist.insert(3, 34222)
print(thislist)
#Another way is append, but it adds item to the end of the list:
thislist.append("Fruit")
print(thislist)
#if we want to combine two lists:
list1=["A", "B", "C", "D"]
list2=["E", "F", "G", "H"]
list1.extend(list2)
print(list1)
#extend can also include other iterable objects (tuples, sets, dictionaries etc.).

#removing items
list1=["A", "B", "C", "D", "C"]
list1.remove("C")    #remove() method removes the first occurance
print(list1)
#pop works with specified index:
list1.pop(0)
print(list1)
#if not specified, pop removes last item
list1.pop()
print(list1)
#same is with del
del list1[0]
print(list1)
del list1
#list is deleted, but still remains using clear

#looping:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#sorting:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#if we want descending order, we have to write reverse=True
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)

#reverse:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)