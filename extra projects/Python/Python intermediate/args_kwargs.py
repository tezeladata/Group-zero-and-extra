# This function accepts three arguments
def total (x, y, z):
    return x + y + z
print(total(4, 2, 5))

# When calling a function, you need to use the same number of arguments that have been defined, in the same order.

# *args allows you to provide any number of arguments without the need to create a list before calling the function each time.
def better_total (*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)
better_total(3, 5, 6, 7, 5, 3, 2, 2, 10, 20)

# * is unpacking operator, it tells function that it will receive iterable and 
# it should be unpacked to receive its values as individual arguments.

# Note that args is just a name, you can use any name for it
def player_scores (*players_list):
    new_list = [str(x) + " player" for x in players_list]
    return new_list
print(player_scores(10, 23, 34, 234, 2342, 11))

# When defining a function with both regular arguments and *args, the regular arguments must come before *args in the function definition.
def all_categories (category, *list):
    print(f"Category: {category}")
    for item in list:
        print(item)

all_categories("alphabet", "a", "b", "c", "d", "e", "f")

# *args receive tuples, *kwargs receive dictionaries
def total(*nums, **new_dict):
    for i in range(len(nums)):
        print(nums[i] ** 2)
    for key, value in new_dict.items():
        print(f"{key} : {value}")

new_dict = {
    "Name": "David",
    "Surname": "Tezelashvili",
    "Age": 16,
    "Address": "Tbilisi"
}
total(3, 4, 5, 2, 55, 6, **new_dict) # Use ** operator for dicts.