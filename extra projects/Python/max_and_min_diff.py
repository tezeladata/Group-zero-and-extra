def max_and_min(arr1, arr2):
    res = []

    max1, max2 = max(arr1) - min(arr2), max(arr2) - min(arr1)
    res.append(max(max1, max2))

    # Brute force for all combinations
    number2 = float('inf')

    for arr1_number in arr1:
        for arr2_number in arr2:
            if abs(arr1_number - arr2_number) < number2: number2 = abs(arr1_number - arr2_number)

    for arr2_number in arr2:
        for arr1_number in arr1:
            if abs(arr2_number - arr1_number) < number2: number2 = abs(arr2_number - arr1_number)

    res.append(number2)
    return res