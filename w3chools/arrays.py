#Arrays are used to store multiple values in one single variable:
names = ["John", "David", "Dean"]
a=names[0]
print(a)
names[0]="Andrew"
print(names)
print(len(names))
#The length of an array is always one more than the highest array index.
#for example, if the last last undex is [5], array lenght is 6

#it is better to use for loops in aray
for x in names:
    print(x)

#adding item
names.append("Marvin")
for x in names:
    print(x)

#removing items in array
names.pop(1)
print(names)
#or
names = ["John", "David", "Dean"]
names.remove("John")
for x in names:
    print(x)