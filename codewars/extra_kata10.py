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

#