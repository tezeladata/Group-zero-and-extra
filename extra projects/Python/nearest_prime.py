def solve(n):
    def is_prime(num):
        if num < 2: return False
        for i in range(2, int(num ** .5) + 1):
            if num % i == 0: return False
        return True

    low, up = n, n

    while is_prime(low) == False:
        low -= 1
    while is_prime(up) == False:
        up += 1

    dist1, dist2 = n - low, up - n
    if dist1 == dist2:
        return low
    elif dist1 > dist2:
        return up
    return low