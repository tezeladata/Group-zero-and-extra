def is_ore(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    divisor_sum = sum([1 / i for i in divisors])

    result = len(divisors) / divisor_sum

    epsilon = 1e-9
    return abs(result - round(result)) < epsilon