# Following is a sequence:
# print("A")
# print("B")

# for i in range(10):
#     print(i)

# print("C")
# print("D")

# Sequencing means that the computer runs your code in order, from top to bottom.
# Iteration is the synonim of repetition
# Iteration is commonly represented as a loop.
# Selection is the conditional statement - conditions

# ალგორითმი არის რიგ-რიგობით მოცემული ინსტრუქციების ერთობლიობა

# Pseudocode is in between the natural language and programming language

def manual_pop(list, element=-1):
    new_list = []
    for i in list:
        if i != list[element]:
            new_list.append(i)
    return new_list

print(manual_pop([1, 2, 3, 4, 5, 6], 2))
print(manual_pop([1, 2, 3, 4, 5, 6]))



# def is_prime(num):
#     if num < 2:
#         is_prime = False
#     else:
#         is_prime = True
#         for i in range(2, num):
#             if num%i==0:
#                 is_prime = False
#                 break

#     if is_prime:
#         return num**2
#     return num**0.5

# list1 = [x for x in range(100)]
# print(list(map(is_prime, list1)))

# Iteration is used to automate tasks that need to be done over and over again. 

person1 = {
    "name": "David", 
    "surname": "Tezelashvili",
    "place": "Georgia"
}

person1["age"] = 16
print(person1)

print("age" in person1)

# get function:
print(person1.get("name", "Andria"))
print(person1.get("Name", "Andria"))
# If first argument of get is not dict key, second argument will be returned


name = input("Enter name: ")
surname = input("Enter surname: ")
age = input("Enter age: ")

user_dict = dict()

user_dict["name"] = name
user_dict["surname"] = surname
user_dict["age"] = age

choice = input("Enter which value you want: ")
print(user_dict.get(choice, "Key not found"))