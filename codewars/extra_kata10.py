#Did she say hallo?
def validate_hello(greetings):
    check=False
    lang=["hello","ciao","salut","hallo","hola","ahoj","czesc"]
    for x in lang:
        if x in greetings.lower():
            check=True
    return check

#Find the Integral
def integrate(coefficient, exponent):
    a=coefficient/(exponent+1)
    return "{}x^{}".format(int(a), exponent+1)

#Switch/Case - Bug Fixing #6
def eval_object(v):
    return{"+": v["a"]+v["b"],
           "-": v["a"]-v["b"],
           "/": v["a"]/v["b"],
           "*": v["a"]*v["b"],
           "%": v["a"]%v["b"],
           "**": v["a"]**v["b"], }.get(v["operation"])

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