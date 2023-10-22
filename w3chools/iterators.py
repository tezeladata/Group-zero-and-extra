#iterate - გამეორება, იტერაცია
#An iterator is an object that contains a countable number of values.
tuple1 = ("John", "Steve", "Damian")
iter1 = iter(tuple1)
print(next(iter1))
print(next(iter1))
print(next(iter1))

#Strings are also iterable objects, containing a sequence of characters:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#We can also use for loops for iteration in tuples and strs
a = "Apple"
for x in a:
    print(x)

tuple2 = ("Europe", "Africa", "Asia", "Australia")
for x in tuple2:
    print(x)

#As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.
#The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
#The __next__() method also allows you to do operations, and must return the next item in the sequence.

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
