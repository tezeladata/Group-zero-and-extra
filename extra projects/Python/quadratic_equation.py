print("This code finds roots from quadratic equation.")
print("Quadratic equation: ax^2 + bx + c")
def equation(a, b, c):
    d=(b**2)-(4*a*c)
    if d<0:
        print("Roots are imaginary numbers")
    else:
        d1=d**0.5
        x1=(-b+d1)/2*a
        x2=(-b-d1)/2*a
        print("First root is:", x1, "and second root is:", x2)
equation(a=float(input("enter a: ")), b=float(input("enter b: ")), c=float(input("enter c: ")))
print("Thanks for attention!")