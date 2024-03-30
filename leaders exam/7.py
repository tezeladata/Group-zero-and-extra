def char_count(first_str):
    new_str = ""
    first_str=first_str.lower()

    first_str = list(first_str)
    for i in range(len(first_str)):
        if first_str.count(first_str[i]) == 1:
            new_str += "("
        elif first_str.count(first_str[i]) >= 2:
            new_str += ")" 
        else:
            new_str += first_str[i]

    return new_str


print(char_count("recede"))
print(char_count("Success"))