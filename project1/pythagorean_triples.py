print("Hello, this code calculates pythagorean triples until limit.")
def triples(n):
    for b in range(n):
        for a in range(1, b):
            c=((a**2 + b**2)**0.5)
            if c % 1 == 0:
                print("Pythagorean triplets are:", a, b, int(c))
    if n<=0:
        print("Not natural number")
triples(n=int(input("Enter upper limit: ")))
print("Thanks for attention!")