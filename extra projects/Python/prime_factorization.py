def prime_factor(num):
    original = num
    if num == 1: return [1]

    n = 2
    factors = []
    while n**2 <= num:
        if num % n == 0:
            factors.append(n)
            num //= n
        else:
            n += 1
    
    if num > 1:
        factors.append(num)

    return f"Prime factors of {original} are:\n{"  *  ".join([f"{num}**{factors.count(num)}" if factors.count(num) > 1 else f"{num}" for num in sorted(list(set(factors)))])}"

print(prime_factor(int(input("Enter natural number: "))))