def lucasnum(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1

    seq, neg = [2, 1], False

    if n < 0:
        n *= -1

        # sequence number is negative if n is odd and negative
        if n % 2 == 1: neg = True

    for i in range(n - 1): seq.append(seq[-1] + seq[-2])

    return seq[-1] * -1 if neg else seq[-1]