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

#Quadratic Coefficients Solver
def quadratic(x1, x2):
    p= -1* (x1 + x2)
    q= x1*x2
    return (1, p, q)

#Wilson primes
def am_i_wilson(n):
    return n==5 or n==13 or n==563

#Parse float
def parse_float(string):
    try:
        return float(string)
    except:
        return None
    
#Grader
def grader(score):
    if score<0.6 or score>1:
        return "F"
    elif score>=0.9:
        return "A"
    elif score>=0.8:
        return "B"
    elif score>=0.7:
        return "C"
    else:
        return "D"
    
#Count the number of cubes with paint on
def count_squares(cuts):
    return 6 * cuts**2 + 2

#Power
def number_to_pwr(number, p): 
    n=1
    for i in range(p):
        n*= number
    return n