# Key-value pairs are a fundamental concept in programming, allowing for efficient organization and retrieval of data.
# Dictionaries are collection types used to store data in key:value pairs, which are considered as items. 
# They are ideal for organizing data into pairs, where each piece of data (value) has its unique identifier (key).

car_dict = {
    "brand": "bmw",
    "model": "f10",
    "year": 2014,
    "color": "gray"
}
# Values can be any data type
# Dict keys should be immutable, which means that they cannot be changed

# Dicts can have duplicate values, bot not keys
# name_dict = {
#     "name": "David",
#     "name": "Andria" #error
# }

# Accesing values using indexing
print(car_dict["brand"])
# We can also use dot notation, like in js
print(car_dict.get("year"))

# Using values() and keys() to access them:
print(car_dict.keys())
print(car_dict.values())

# items() function returns key:value items:
print(car_dict.items())


# Working with dicts
car_name=car_dict["model"]
print(car_name)
# Changing value:
car_dict["year"]=2013
print(car_dict["year"])
# Adding new key:
car_dict["country"]="Germany"
print(car_dict)

user = {
  "Name": "Albert",
  "Age": 29
}
user.update({"Age": 30})
print(user)


# The pop() function removes the item with the specified key name. It accepts the key of the item you want to remove as an argument.
user.pop("Name")
print(user)

# Checking if item is in dict - You can use the in operator to check if a key or a value occurs in a dictionary.
print("Age" in user)

# To check if a value occurs in a dictionary, you need to use the values() function.
print(30 in user.values())

# If you loop through a dictionary, it will return the keys.
for i in car_dict:
    print(i)
# Showing values:
for i in car_dict.values():
    print(i)