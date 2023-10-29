print("Hello, this is divisibility check")
lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))
num = int(input("Number to be divided with: "))
for i in range(lower, upper):
    if i%num==0:
        print(i)
print("Thanks for attention!")