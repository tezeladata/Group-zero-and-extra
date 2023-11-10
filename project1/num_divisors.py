def divisors():
    print("Hello, this code writes you divisors of number.")
    number=int(input("Enter natural number: "))
    divisors=[1]
    for i in range(2, number+1):
        if number%i==0:
            divisors.append(i)
    a = sum(divisors)
    print("Divisors of number are:", divisors, "and their sum is:", a)
divisors()