print("Welcome, this code finds root of your number")
num=float(input("Enter number: "))
degree=float(input("Degree is 1/x, x="))
while degree>0:
    a=num**(1/degree)
    print(a)
    break
