def pyramid_height(n):
    all, start = [], 1

    # fill out start
    while sum(all) < n:
        all.append(start ** 2)
        start += 1

    # return result
    for i in range(len(all)):
        if sum(all[:i + 1]) > n: return i
    return len(all)