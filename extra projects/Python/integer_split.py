def split_integer(num, parts):
    base_size = num // parts 
    remainder = num % parts  
    
    result = [base_size + 1] * remainder + [base_size] * (parts - remainder)
    
    return sorted(result)

print(split_integer(num=int(input("Enter natural number: ")), parts=int(input("Enter how many parts you want already entered number to be splitted in (natural number): "))))