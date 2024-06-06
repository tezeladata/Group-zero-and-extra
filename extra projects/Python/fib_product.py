def product_fib(prod):
    res = [0, 1]
    
    while res[-1] * res[-2] < prod:
        res.append(res[-1] + res[-2])
        
    if res[-1] * res[-2] == prod: return [res[-2], res[-1], True]
    return [res[-2], res[-1], False]

print(product_fib(int(input("Enter natural number to see if it is product of any consecutive fibbonaci numbers: "))))