print("In this code each digit is repeated a number of times it's value.")
def repeat(s):
    s=str(s)
    s=list(s)
    ans=""
    for i in s:
        ans+=str(i)*int(i)
    return "Exploded number for your number is {}.".format(ans)
print(repeat(s=(int(input("Enter natural number: ")))))