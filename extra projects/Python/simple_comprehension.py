def variations():
    x = int(input("Number one: "))
    y = int(input("Number two: "))
    z = int(input("Number three: "))
    n = int(input("Enter sum: "))
    
    result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(result)

variations()