def factors_range(n, m):
    def factors(num):
        return [i for i in range(2, num) if num % i == 0]

    res = {}
    for i in range(n, m + 1):
        fc = factors(i)

        if fc != []:
            res[i] = fc
        else:
            res[i] = ["None"]

    return res