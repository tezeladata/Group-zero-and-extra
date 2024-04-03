def num_primorial(n):
    prim_arr = []
    start_num = 2 
    while len(prim_arr) != n:
        if prime_check(start_num):
            prim_arr.append(start_num)
        start_num += 1
        
    product = 1
    for num in prim_arr:
        product *= num
    return f"Primorial array is {prim_arr}\nTheir product is: {product}"

        
def prime_check(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

print("Hello, this is primorial generator. You enter number and that many primes are generated")
print("You have to enter primorial number")
print(num_primorial(n=int(input("Enter whole number / integer: "))))