def task_two(arr):
    new_arr = []

    # "0" -> 0:
    for i in range(len(arr)):
        if arr[i] == "0":
            arr[i] = 0

    # Main:
    for i in arr:
        if type(i) != int:
            new_arr.append("L")
        else:
            if i != 0:
                new_arr.append("N")
            else:
                new_arr.append("Z")
    
    
    return "".join(new_arr) #String

print(task_two(["0", "მ", "m", 123, "0", "m", 1]))
print(task_two([0, "m", 1, 8, "n", 10, "s"]))