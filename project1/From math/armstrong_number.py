print("This code checks if your number is Armstrong number.")
def armstrong_num(number1):
    a=str(number1)
    b=len(a)
    count=0
    for i in range(b):
        count+=int(a[i])**b
    if count==number1:
        return "{} is Armstrong number.".format(number1)
    else:
        return "{} is not Armstrong number.".format(number1)
    
print(armstrong_num(number1=int(input("Enter Natural number: "))))