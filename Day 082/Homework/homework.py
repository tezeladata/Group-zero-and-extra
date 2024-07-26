dict1 = {
    "b": 2,
    "d": 4,
    "c": 3,
    "a": 1
}

dict2 = {
    "g": 10,
    "h": 40,
    "o": -2,
    "j": 15
}

# Task1:
def sort_keys(user_dict):
    res_keys = list(user_dict.keys())
    res_keys.sort()
    return res_keys

print(sort_keys(user_dict=dict1))


# Task2:
def min_and_max(user_dict):
    for key, value in user_dict.items():
        if value == max(user_dict.values()):
            max_key = key
        
        if value == min(user_dict.values()):
            min_key = key

    return f"Key for maximum value is: {max_key}. Key for minimum value is : {min_key}"

print(min_and_max(user_dict=dict1))


# Task3:
def combine_dicts(user_dict1, user_dict2):
    # list1, list2 = list(user_dict1.items()), list(user_dict2.items())

    # res_list = []
    # for i in list1:
    #     res_list.append(i)
    # for i in list2:
    #     res_list.append(i)

    # return res_list

    return list(user_dict1.items()) + list(user_dict2.items())

print(combine_dicts(dict1, dict2))


# Task4:
def key_in_dict(user_dict, user_key):
    return user_dict.get(user_key, f"{user_key} not in dict")

print(key_in_dict(dict1, "b"))


# Task5:
def remove_and_return(user_dict, user_key):
    res = user_dict[user_key]
    user_dict.pop(user_key)

    return f"Dict after pop is: {user_dict}, value is: {res}"

print(remove_and_return(dict1, "a"))


# Task6:
def manual_keys(user_dict):
    # res_keys = []

    # for i in user_dict:
    #     res_keys.append(i)

    # return res_keys
    return [i for i in user_dict]

print(manual_keys(dict2))


# Task7:
def manual_values(user_dict):
    # res_values = []

    # for i in user_dict:
    #     res_values.append(user_dict[i])

    # return res_values
    return [user_dict[i] for i in user_dict]

print(manual_values(dict2))


# Task8:
def manual_items(user_dict):
    # res_list = []

    # for i in user_dict:
    #     res_list.append(tuple([i, user_dict[i]]))

    # return res_list
    return [tuple([i, user_dict[i]]) for i in user_dict]

print(manual_items(dict2))


# Task9:
def manual_get(user_dict, user_key, default_value = "Not valid"):
    if user_key in user_dict.keys():
        return user_dict[user_key]
    return default_value

print(manual_get(dict2, "o"))
print(manual_get(dict2, "10"))


# Task10:
def manual_pop(user_dict, user_key=None):
    if user_key is None:
        raise ValueError("Please provide a key to continue.")
    
    res = {key: value for key, value in user_dict.items() if key != user_key}

    if len(res) == len(user_dict):
        raise KeyError("Key not found in dictionary.")
    else:
        return res

print(manual_pop(user_dict=dict2, user_key="o"))
print(manual_pop(user_dict=dict2))
print(manual_pop(user_dict=dict2, user_key=10))