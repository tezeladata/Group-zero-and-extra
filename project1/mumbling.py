def mumbling(str):
    new_str=""
    for i in range(len(str)):
        new_str+=str[i].upper()
        new_str+=(str[i]*(i)).lower()
        new_str+="-"
    return new_str.strip("-")
print(mumbling(str=input("Enter words: ")))