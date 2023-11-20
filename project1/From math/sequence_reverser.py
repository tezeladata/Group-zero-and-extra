print("Hello, this is sequence reverser!")
def reverse_seq(n):
    sequence=[]
    if n>0:
        for i in range(1, n+1):
            sequence.append(i)
    print("Reversed sequence for number", n, "is:", sequence[::-1])
    print("Thanks for attention!")
reverse_seq(n=int(input("Enter natural number you want reversed sequence to be written for: ")))