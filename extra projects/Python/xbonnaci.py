def xbonacci(signature, n):
    res = signature.copy()
    while len(res) < n: res.append(sum(res[-len(signature):]))
    return res[:n]