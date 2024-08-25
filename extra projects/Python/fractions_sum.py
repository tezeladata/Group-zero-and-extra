def gcd(x, y):
    return y == 0 and x or gcd(y, x % y)

def lcm(x, y):
    return abs(x * y) // gcd(x, y)

def sum_fracts(lst):
    if not lst: return None

    lst = [[int(i.split("/")[0]), int(i.split("/")[1])] for i in lst.split(" ")]

    common_denom = lst[0][1]
    for _, denom in lst[1:]:
        common_denom = lcm(common_denom, denom)
    
    numerator_sum = sum(numer * (common_denom // denom) for numer, denom in lst)
    
    common_divisor = gcd(numerator_sum, common_denom)
    numerator_sum //= common_divisor
    common_denom //= common_divisor


    if common_denom == 1: return numerator_sum
    return f"{numerator_sum} / {common_denom}"

print(sum_fracts(lst=input("Enter fractions in following format: x/y and leave spaces among different fractions: ")))