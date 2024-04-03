def is_triangle_number(number):
    if type(number) == int:
        triangle_arr = [0]
        for n in range(1, number+1):
            result = n * (n + 1) / 2
            triangle_arr.append(result)
        
        res_arr = [int(x) for x in triangle_arr]
        if number in res_arr:
            return f"{number} is triangle number\nOthers in that area are: {res_arr}"
        else:
            return f"{number} is not triangle number, but\nOthers in that area are: {res_arr}"
    else:
        return f"{number} is not triangle number, but\nOthers in that area are: {res_arr}"
    
print("Hello, this code checks if your number is triangle number")
print(is_triangle_number(number=int(input("Enter whole number / integer to check if it is triangle number: "))))