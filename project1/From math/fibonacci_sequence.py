def fibonacci():
    print("Hello, this code generates fibonacci numbers for specified range!")
    range_for_fib=int(input("Enter how many numbers you want for sequence: "))
    sequence=[0,1]
    n1=0
    n2=1
    for i in range(2, range_for_fib):
        n3=n1+n2
        n1=n2
        n2=n3
        sequence.append(n3)
    print("Fibonacci sequence: {}".format(sequence))
    print("Thanks for attention!")
fibonacci()