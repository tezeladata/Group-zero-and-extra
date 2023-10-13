thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print (thisdict)
#Dictionaries are used to store data values in key:value pairs.

cardict = {
  "brand": "bmw",
  "model": "e92",
  "year": 2005
}
print(cardict)
print(cardict["brand"])
print(cardict["model"])
print(cardict["year"])

#Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
#Dictionaries cannot have two items with the same key

#Duplicate values will overwrite existing values:
fruitdict = {
    "name": "banana",
    "color": "green",
    "color": "yellow"
}
print(len(fruitdict))
print(fruitdict)

#The values in dictionary items can be of any data type:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

#dict type is <class dict>
cardict = {
  "brand": "bmw",
  "model": "e92",
  "year": 2005
}
print(type(thisdict))

cardict = dict(brand = "audi", model = "r8",  country = "Germany")
print(thisdict)

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car["model"]
print(x)

#There is also a method called get() that will give you the same result:
x = car.get("model")
x = car.keys()
print(x)

car["color"] = "white"

print(x) #after the change

#The values() method will return a list of all the values in the dictionary.
x = thisdict.values()
print(x)

x = thisdict.items()
print(x)


#adding item value in original list
data = {
    "name": "David",
    "surname": "Tezelashvili",
    "age": 15
}

data["age"] = 14
print(data)

data = {
    "name": "David",
    "surname": "Tezelashvili",
    "age": 15
}
if "age" in data:
    print("there's age determined in dictionary called data")
print(data)

#The update() method will update the dictionary with the items from the given argument.
data = {
    "name": "David",
    "surname": "Tezelashvili",
    "age": 15
}
data.update ({"name": "დათა"})
print(data)

#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
cardict = {
  "brand": "bmw",
  "model": "e34 M",
  "year": 1988
}
cardict["color"]=("purple")
print(cardict)

#can use method stated above or update() method
cardict = {
  "brand": "bmw",
  "model": "e34 M",
  "year": 1988
}
cardict.update({"color": "purple"})

#There are several methods to remove items from a dictionary: pop(); popitem(); del; clear().
#pop()- ით დადგენილ ცვლადს ვშლით
cardict = {
  "brand": "bmw",
  "model": "e34 M",
  "year": 1988
}
cardict.pop("year")
print(cardict)

#popitem()-ით ბოლო ცვლადს შლის
cardict = {
  "brand": "bmw",
  "model": "e34 M",
  "year": 1988
}
cardict.popitem()
print(cardict)
#del ფუნქციაც pop()-ისავით მუშაობს
cardict = {
  "brand": "bmw",
  "model": "e34 M",
  "year": 1988
}
del cardict["brand"]
print(cardict)

#clear მთლიანად შლის ბიბლიოთეკას
cardict = {
  "brand": "bmw",
  "model": "e34 M",
  "year": 1988
}
cardict.clear()
print(cardict)



#loop
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

#printing values assigned to variable
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])

#დაკოპირება და dict ფუქნცია
cardict = {
  "brand": "bmw",
  "model": "e34 M",
  "year": 1988
}
cardict2=cardict.copy()
print(cardict2)

cardict = {
  "brand": "bmw",
  "model": "e34 M",
  "year": 1988
}
cardict3=dict(cardict)
print(cardict3)

#nested directory
#A dictionary can contain dictionaries, this is called nested dictionaries.

fruits = {
   "fruit1": {
      "name": "apple",
      "color": "green",
   },
   "fruit2": {
      "name": "banana",
      "color": "green",
   }
   }
print(fruits)


fruit1 = {
      "name": "apple",
      "color": "green",
   },
fruit2 = {
      "name": "banana",
      "color": "green",
   },
all_fruits = {
   "fruit1": fruit1,
   "fruit2": fruit2
}
print(all_fruits)


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])
