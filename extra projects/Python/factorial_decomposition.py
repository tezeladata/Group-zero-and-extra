def decomp(n):
    def prime_factor(num):
        factors = []
        d = 2
        while d * d <= num:
            while num % d == 0:
                factors.append(d)
                num //= d
            d += 1
        if num > 1:
            factors.append(num)
        return factors

    all_factors = []
    for i in range(2, n + 1): all_factors.extend(prime_factor(i))

    factor_counts = {}
    for factor in all_factors:
        factor_counts[factor] = factor_counts.get(factor, 0) + 1

    result = []
    for prime in sorted(factor_counts.keys()):
        count = factor_counts[prime]
        if count > 1: result.append(f"{prime}^{count}")
        else: result.append(str(prime))

    return " * ".join(result)

print(decomp(int(input("Enter a number for it's factorial to be decomposed: "))))