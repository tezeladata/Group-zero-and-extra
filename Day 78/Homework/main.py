# 1
def merge_lists(list_one, list_two):
    merged = list_one
    for i in list_two:
        if i not in merged:
            merged.append(i)
    return merged

print(merge_lists([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))


# 2
def squared_list(list):
    new_list = []
    for i in list:
        new_list.append(i**2)
    return new_list
print(squared_list([1, 2, 3, 4, 5]))
# or:
result = [(lambda x: x**2)(x) for x in [6, 7, 8, 9, 10]]
print(result)


# 3
def odd_numbers(list):
    result = [x for x in list if x%2!=0]
    return result
print(odd_numbers([1, 2, 3, 4, 5]))
# or:
print(list(filter(lambda x: x%2!=0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))


# 4
def common_elements(list_one, list_two):
    common_list = []
    for i in list_one:
        if i in list_two:
            common_list.append(i)
    return list(set(common_list))
print(common_elements([1, 2, 3, 4, 5, 5], [3, 4, 5, 5, 6, 7]))
# or:
print(list(set([1, 2, 3, 4, 5, 5]) & set([10, 11, 1, 2, 5])))


# 5
def remove_duplicates(list):
    result_list = []
    for i in range(len(list)):
        if list.count(list[i]) < 2:
            result_list.append(list[i])
    return result_list
print(remove_duplicates([1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8]))
# or:
print(list(filter(lambda x: [1, 2, 3, 4, 4, 4, 2, 5, 6, 7].count(x) < 2, [1, 2, 3, 4, 4, 4, 2, 5, 6, 7])))


# 6
def merge_dicts(dict1, dict2):
    result_dict = dict()
    for key, value in dict2.items():
        result_dict[f"{key}"] = f"{value}"
    for key, value in dict1.items():
        if key not in result_dict.keys():
            result_dict[f"{key}"] = f"{value}"
    return result_dict

dict1 = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40
}
dict2 = {
    "c": 130,
    "d": 140,
    "e": 150, 
    "f": 160
}
print(merge_dicts(dict1, dict2))
# Better:
def merge_dicts2(dict1, dict2):
    result_dict = dict(dict1) 
    for key, value in dict2.items():
        result_dict[key] = value  
    return result_dict
print(merge_dicts2(dict1, dict2))


# 7
def squared_dict(dict1):
    res_dict = dict()
    for key, value in dict1.items():
        if type(value) == int or type(value) == float:
            res_dict[key] = value**2
        elif type(value) == str:
            res_dict[key] = ord(value) ** 2
    
    return res_dict
dict3 = {
    "a": 10,
    "b": 20,
    "c": "g",
    "d": "k",
    "e": 10,
    "f": 10
}
print(squared_dict(dict3))


# 8
def key_in_list(dict1):
    keys_list = []
    for key, value in dict1.items():
        keys_list.append(key)
    return keys_list
print(key_in_list(dict3))


# 9
def word_frequency_counter(user_str):
    user_str = user_str.split(" ")
    words_list = list(set(user_str)) 

    words_count = [user_str.count(word) for word in words_list]

    result_dict = dict()
    for i in range(len(words_list)):
        result_dict[f"{words_list[i]}"] = f"{words_count[i]}"
    
    return result_dict

# print(word_frequency_counter(input("Enter sentence here: ")))


# 10
def dictionary_filter(dict1, user_value):
    result_dict = dict()

    for key, value in dict1.items():
        if value == user_value:
            result_dict[key] = value

    return result_dict

dict3 = {
    "a": 10,
    "b": 20,
    "c": "g",
    "d": "k",
    "e": 10,
    "f": 10
}

# print(dictionary_filter(dict1=dict3, user_value=int(input("Enter value: "))))


# 11
def factorial(number):
    product = 1
    for i in range(2, number+1):
        product *= i
    return product

print(factorial(5))


# 12
def check_palindrome(user_str):
    return user_str == user_str[::-1]

print(check_palindrome("rotor"))
print(check_palindrome("civic"))
print(check_palindrome("car"))


# 13
def anagram_checker(input1, input2):

    def anagram_inner(string):
        word_dict = dict()
        
        char_list = list(string)
        char_set = set(char_list)  
        chars_count = [char_list.count(char) for char in char_set]

        for i, char in enumerate(char_set):
            word_dict[char] = chars_count[i]

        return word_dict
    
    return anagram_inner(input1) == anagram_inner(input2)

print(anagram_checker("Hello", "Hello"))
print(anagram_checker("ello", "Hello"))
print(anagram_checker("Helo", "Hello"))


# 14
def sentence_reversal(user_input):
    return " ".join(reversed(user_input.split(" ")))

# print(sentence_reversal(user_input=input("Enter sentence: ")))


# 15
def to_do_list():
    # Main functions
    def add_or_edit_items(user_dict):
        name = input("Enter name of your task: ")
        data = input("Enter description of your task: ")
        user_dict[name] = data

    def delete_items(user_dict):
        name = input("Enter name of the task you want to delete: ")
        del user_dict[name]

    print("Hello, this is a simple To-do list")
    user_dict = dict()

    # Main logic
    def main_logic(user_dict):
        print(f"Your list now looks like this: {user_dict}")
        print("You can add / edit / remove items from your list")
        choice = input("Select operation: ")

        if choice.lower() == "add":
            add_or_edit_items(user_dict)
            print("")
            print(user_dict)
            print("")
        elif choice.lower() == "edit":
            add_or_edit_items(user_dict)
            print("")
            print(user_dict)
            print("")
        elif choice.lower() == "remove":
            delete_items(user_dict)
            print("")
            print(user_dict)
            print("")
        else:
            print("Incorrect operation!")
            print("")
            print(user_dict)
            print("")

    main_logic(user_dict)

    user_decision = input("Continue? Y/N - ")

    while user_decision.lower() == "y":
        main_logic(user_dict)
        user_decision = input("Continue? Y/N - ")
    print("Thanks for the attention!")

# to_do_list()


# 16
def merged_list(key_list, value_list):
    res_dict = dict()
    for i in range(len(key_list)):
        res_dict[key_list[i]] = value_list[i]
    return res_dict
print(merged_list(["a", "b", "c", "d"], [10, 20, 30, 40]))


# 17
def key_in_dict(dict1, key1):
    return dict1.get(key1, "Key not found")
print(key_in_dict(dict3, key1="a"))


# 18
def sum_key(dict1):
    res_dict = dict()
    for key, value in dict1.items():
        res_dict[f"{sum(value)}"] = value
    return res_dict
dict4 = {
    "a": [1, 2, 3, 4, 5],
    "b": [2, 4, 6, 8],
    "c": [1, 3, 5, 7]
}

print(sum_key(dict4))


# 19
def split_list(list1, user_num):
    res_dict = dict()

    less = []
    more_or_equal = []

    for i in list1:
        if i < user_num:
            less.append(i)
        else:
            more_or_equal.append(i)
    
    res_dict["less"] = less
    res_dict["more or equal"] = more_or_equal

    return res_dict

print(split_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))


# 20
def list_intersection(list1, list2):
    return [i for i in list1 if i in list2]

print(list_intersection([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))