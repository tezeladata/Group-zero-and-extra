def is_prime(n):
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

def backwards_prime(start, stop):
    primes_arr = []
    for num in range(start, stop+1):
        reversed_num = int(str(num)[::-1])
        if is_prime(num) and is_prime(reversed_num) and num != reversed_num:
            primes_arr.append(num)

    print("Your result is: ")
    for i in range(len(primes_arr)):
        print(f"{i}: {primes_arr[i]}")
    print(f"{primes_arr} contains {len(primes_arr)} elements")

print("Backwards Read Primes are primes that when read backwards are a different prime.")
print("In this code, you enter starting and ending numbers, backwards primes are generated in that range.")
backwards_prime(start=int(input("Enter starting number: ")), stop=int(input("Enter stopping number: ")))