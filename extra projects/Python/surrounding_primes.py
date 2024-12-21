def prime_bef_aft(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    before = n - 1
    while not is_prime(before): before -= 1

    after = n + 1
    while not is_prime(after): after += 1

    return [before, after]
