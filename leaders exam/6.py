def shortest_word(str):
    str = str.lower()
    str = list(str)
    new_arr = []
    for i in str:
        if str.count(i) == 1:
            new_arr.append(i)
    
    if new_arr == []:
        return "mgeli200"
    else:
        return new_arr[0]
    


print(shortest_word("Traqtori"))
print(shortest_word("sTress"))
print(shortest_word(".merrraaabbii")) # ეს იგივე test case არაა
print(shortest_word("aabb"))