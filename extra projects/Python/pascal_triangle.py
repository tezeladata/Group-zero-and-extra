def generate_pascals_triangle():
    print("Hello, this is Pascal's Triangle")
    n = int(input("Enter number of rows: "))
    a = []

    for i in range(n):
        a.append([])
        a[i].append(1)
        for j in range(1, i):
            a[i].append(a[i-1][j-1] + a[i-1][j])
        if n != 0:
            a[i].append(1)
    
    print(a)

# Call the function
generate_pascals_triangle()