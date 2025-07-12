def sequence_classifier(arr):
    # 0 - unordered
    # 1 - strictly increasing
    # 2 - not decreasing
    # 3 - strictly decreasing
    # 4 - not increasing
    # 5 - constant
    
    if arr.count(arr[0]) == len(arr): return 5

    inc = dec = True
    for i in range(len(arr) - 1):
        if arr[i] < arr[i+1]: dec = False
        if arr[i] > arr[i+1]: inc = False

    if inc and all(arr[i] < arr[i+1] for i in range(len(arr)-1)): return 1
    if inc: return 2
    if dec and all(arr[i] > arr[i+1] for i in range(len(arr)-1)): return 3
    if dec: return 4
    return 0