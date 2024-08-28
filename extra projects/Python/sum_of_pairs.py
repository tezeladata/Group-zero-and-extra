def sum_pairs(arr, s):
    seen = set()
    for num in arr:
        complement = s - num
        if complement in seen:
            return [complement, num]
        seen.add(num)
    return None

print("Hello, this algorithm finds pair in array which has sum of number you want")
ls = [int(i) for i in input("Enter numbers for array, just leave 1 space between them: ").split(" ")]
user_num = int(input("Enter integer for sum: "))
print(sum_pairs(ls, user_num))