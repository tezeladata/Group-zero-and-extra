def rotate(arr, n):
    # no change
    if n == 0: return arr

    # positive rotation
    if n > 0:
        if n > len(arr): n %= len(arr)

        all = [[arr[i], i + n] for i in range(len(arr))]

        for i in all:
            if i[1] >= len(arr): i[1] = i[1] % len(arr)

        return [i[0] for i in sorted(all, key=lambda x: x[1])]

    # negative rotation
    if n < 0:
        n = -n % len(arr)
        return arr[n:] + arr[:n]