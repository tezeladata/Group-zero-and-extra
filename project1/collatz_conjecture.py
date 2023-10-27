print("Welcome, this is collatz conjecture or simply 3x+1 calculator:")
def collatz_conjecture(num):
    sequence = [num]
    while num >1:
        if ((num % 2) == 0):
            num = num // 2
        else:
            num = num *3 +1
        sequence.append(num)
    return sequence
    
num = int(input("Enter any natural number: "))
if num>1:
    print("Sequence for", num, "is:")
    print(collatz_conjecture(num))
else:
    print(num, "is not natural number.")