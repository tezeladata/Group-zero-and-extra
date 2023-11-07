print("Hello, this is factorial calculator.")
def calculator():
    num1=int(input("Natural number you want factorial for: "))
    num2=int(input("Natural number you want factorial for: "))
    print("Operations are: 1-Addition, 2-substraction, 3-multiplication, 4-division")
    choice=int(input("Select operation: 1/2/3/4 - "))
    factorial1=1
    factorial2=1
    for i in range(1, num1+1):
        factorial1=factorial1*i
    for x in range(1, num2+1):
        factorial2=factorial2*x
    if choice==1:
        print("Sum of factorials of", num1, "and", num2, "is:", factorial1+factorial2)
    elif choice==2:
        print("Difference of factorials of", num1, "and", num2, "is:", factorial1-factorial2)
    elif choice==3:
        print("Product of factorials of", num1, "and", num2, "is:", factorial1*factorial2)
    elif choice==4:
        print("Division of factorials of", num1, "and", num2, "is:", factorial1/factorial2)
calculator()
print("Thanks for attention!")