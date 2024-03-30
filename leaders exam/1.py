def reverser(arr):
    new_arr = [x for x in arr if x%2==0]

    res_arr = []

    # reverse = True-თი ვერ გავაკეთე
    for i in range(len(new_arr)-1, -1, -1):
        res_arr.append(str(new_arr[i]))
    return "-".join(res_arr)

print(reverser([1, 3, 4, 45, 32, 12, 7, 8, 10]))

print(reverser([1, 48, 16, 2, 3, 97, 100, 15, 13]))