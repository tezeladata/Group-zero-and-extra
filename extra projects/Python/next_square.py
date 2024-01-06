import math
def next_square(number):
    a=math.sqrt(number)
    if a%1==0:
        return "Perfect square after {} is {}.".format(number, (a+1)**2)
    else:
        return "Perfect square after {} is {}.".format(number, (math.floor(a)+1)**2)
print(next_square(number=float(input("Enter non-negative number: "))))