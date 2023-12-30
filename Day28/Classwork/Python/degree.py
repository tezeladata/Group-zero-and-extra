print("Hello, this is calculator.")
print("Functions are addition, subtraction, multiplication, division and degree")
def calculator(num1, num2, choice):
    if type(num1)!=float or type(num2)!=float:
        return "Not a number."
    elif choice not in "+-**/":
        return "Invalid operator."
    else:
        if choice=="+" or choice=="addition":
            return "Sum of {} and {} is {}\n Thanks for attention!".format(num1, num2, num1+num2)
        elif choice=="-" or choice=="subtraction":
            return "{} minus {} is {}\nThanks for attention!".format(num1, num2, num1-num2)
        elif choice=="*" or choice=="multiplication":
            return "{} multiplicated by {} is {}\nThanks for attention!".format(num1, num2, num1*num2)
        elif choice=="/" or choice=="division":
            return "{} divided by {} is {}\nThanks for attention!".format(num1, num2, num1/num2)
        elif choice=="**" or choice=="degree":
            return "{} in power of {} is {}\nThanks for attention!".format(num1, num2, num1**num2)
print(calculator(num1=float(input("Enter number: ")), num2=float(input("Enter second number: ")), choice=input("+ or - or * or / or ** (If square root enter 0.5 in degree): ")))
    