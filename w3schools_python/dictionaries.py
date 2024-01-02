#dictionaries
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
dict1={
    "brand": "bmw",
    "model": "e92",
    "year": "2005"
}
print(dict1)
print(dict1["brand"])
#there is also other method called get:
a=dict1.get("model")
print(a)
#Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
#Duplicate values will overwrite existing values:
dict1={
    "brand": "bmw",
    "model": "5 series",
    "year": 1972,
    "year": 2023
}
print(dict1["year"]) #it overwrited
#length
print(len(dict1))
#The values in dictionary items can be of any data type
#It is also possible to use the dict() constructor to make a dictionary.
dict2=dict(Name = "David", Age= 15)
print(dict2)

#The keys() method will return a list of all the keys in the dictionary.
a=dict2.keys()
#The values() method will return a list of all the values in the dictionary.
b=dict2.values()
print(a,b)
#The items() method will return each item in a dictionary, as tuples in a list.
c=dict2.items()
print(c)

#You can change the value of a specific item by referring to its key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"]=2004
print(thisdict)

#The update() method will update the dictionary with the items from the given argument.
thisdict.update({"year": 2001})
print(thisdict)

dict3={
    "Continent": "Asia",
    "Country": "Georgia"
}
dict3["City"]="Tbilisi"
print(dict3)

#The pop() method removes the item with the specified key name
dict3={
    "Continent": "Asia",
    "Country": "Georgia"
}
dict3.pop("Country")
print(dict3)
#The popitem() method removes the last inserted item
#The del keyword removes the item with the specified key name
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["year"]
print(thisdict)
#The clear() method empties the dictionary

#Make a copy of a dictionary with the copy() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict4=thisdict.copy()
print(dict4)

#Another way to make a copy is to use the built-in function dict().
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict4=dict(thisdict)
print(dict4)

#nested
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
#access
print(myfamily["child2"]["name"])
