class Create_acc:

    def __init__(self, fullname, mail, address, password):
        self.fullname = fullname
        self.mail = mail
        self.address = address
        self.password = password

    def return_all(self):
        return f"Your name is: {self.fullname}, you live in {self.address}. \nYour mail is: {self.mail} and your password is: {self.password}"
    
user1 = Create_acc("David Tezelashvili", "datatezelashvili8@gmail.com", "Tbilisi", "helloworld123!")
print(user1.return_all())


def return_frequency(user_str):
    # user_str = user_str.split(" ")
    # res_dict = dict()
    # for i in user_str:
    #     res_dict[i] = user_str.count(i)

    return {i: user_str.count(i) for i in user_str.split(" ")}

print(return_frequency("hello hello this is David"))


def return_val(user_dict, val):
    return {key: value for key, value in user_dict.items() if value == val}

dict1 = {
    "a": 1, 
    "b": 1,
    "c": 2,
    "d": 2
}
print(return_val(dict1, 1))


numbers = [1, 2, 3, 4, 5]
num1, num2, *num3 = numbers
print(num3, type(num3))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))


# Dict and it's methods
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car["year"])


acc = {
    "fullname": "David Tezelashvili", 
    "academy": "GOA",
    "georgian": True,
    "address": {
        "region": "Kartli",
        "city": "Tbilisi"
    }
}
print(acc["address"]["region"], acc["address"]["city"])


my_dict = {
    "fullname": "David Tezelashvili",
    "mail": "datatezelashvili8@gmail.com",
    "address": "Tbilisi",
    "password": "helloworld123!"
}

# 1
for i in my_dict:
    print(my_dict[i])
# 2
for key, value in my_dict.items():
    print(f"{key}: {value}")


def manual_items(user_dict):
    # return [[i, user_dict[i]] for i in user_dict]
    return [[key, user_dict[key]] for key in user_dict]

print(manual_items(dict1))


print(my_dict.get("fullname", "Not valid"))
print(my_dict.get("Fullname", "Not valid"))


def manual_get(user_dict, user_key, default_value = "Not valid"):
    # for key, value in user_dict.items():
    #     if key == user_key:
    #         return value
    #     else:
    #         return "Not valid!"
    
    if user_key in user_dict.keys():
        return user_dict[user_key]
    return default_value
        
print(manual_get(my_dict, "fullname"))
print(manual_get(my_dict, "Fullname"))


def manual_pop(dict_collection, key_to_remove):
    res = dict()

    for key in dict_collection.keys():
        if key != key_to_remove:
            res[key] = dict_collection[key]

    return res

print(manual_pop(my_dict, "mail"))