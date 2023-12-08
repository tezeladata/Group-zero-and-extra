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

#Vowel Count
def get_count(sentence):
    counter=0
    for i in sentence:
        if i in "aeiou":
            counter+=1
    return counter

#Disemvowel Trolls
def disemvowel(string_):
    new_str=""
    for i in string_:
        if i not in "aeiouAEIOU":
            new_str+=i
    return new_str

#Highest and Lowest
def high_and_low(numbers):
    new=[int(x) for x in numbers.split()]
    return "{} {}".format(max(new), min(new))

#You're a square!
import math
def is_square(n):    
    new=[]
    for i in range(100000):
        new.append(i)
    if n<0:
        return False
    else:
        sqr=math.sqrt(n)
        if sqr in new:
            return True
        else:
            return False
#or
def is_square(n):    
    sqr=n**0.5
    if n>=0:
        if sqr%1==0:
            return True
        else:
            return False
    else:
        return False
    
#Descending Order
def descending_order(num):
    num=str(num)
    num=list(num)
    num=sorted(num)
    num=reversed(num)
    num="".join(num)
    return int(num)

#List Filtering
def filter_list(l):
    new=[]
    for i in l:
        if type(i)!=str:
            new.append(i)
    return new

#Get the Middle Character
def get_middle(s):
    a=len(s)
    b=int(a/2)
    if a%2==0:
        return s[b-1:b+1]
    else:
        return s[b:b+1]
    
#Isograms
def is_isogram(string):
    string=string.lower()
    for char in string:
        if string.count(char) >1:
            return False
    return True

#Exes and Ohs
def xo(s):
    if s.count("x")+s.count("X")==s.count("o")+s.count("O"):
        return True
    else:
        return False
    
#Jaden Casing Strings
def to_jaden_case(string):
    if len(string)==0:
        return string
    str=string.split()
    for i in range(len(str)):
        str[i]=str[i].capitalize()
    return " ".join(str)

#Shortest Word
def find_short(s):
    new=list(s.split(" "))
    counter=[]
    for element in new:
        counter.append(len(element))
    return min(counter)

#Complementary DNA
def DNA_strand(dna):
    twin={"A":"T", "T":"A", "C":"G", "G":"C"}
    return "".join(twin[x] for x in dna)

#Sum of two lowest positive integers
def sum_two_smallest_numbers(numbers):
    a=0
    a+=(min(numbers))
    numbers.remove(min(numbers))
    b=0
    b+=(min(numbers))
    return a+b

#Beginner Series #3 Sum of Numbers
def get_sum(a,b):
    counter1=0
    counter2=0
    if a==b:
        return a
    elif a>b:
        for i in range(b, a+1):
            counter1+=i
        return counter1
    elif a<b:
        for i in range(a, b+1):
            counter2+=i
        return counter2