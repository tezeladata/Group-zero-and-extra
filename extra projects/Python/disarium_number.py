print("Hello, this code checks if your number is disarium")
def disarium_number(number):
    a=str(number)
    b=len(a)
    disarium_sum = sum(int(a[i]) ** (i + 1) for i in range(b))
    if disarium_sum==number:
        return "{} is disarium number.".format(number)
    else:
        return "{} is not disarium number.".format(number)
print(disarium_number(number=int(input("Enter whole positive number: "))))