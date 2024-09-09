def padovan(n):
    res = [1, 1, 1]
    while len(res) < n+1: res.append(res[-2]+res[-3])
    return res[-1]

print(padovan(n=int(input("Enter a number you want Padovan number sequence's item for: "))))