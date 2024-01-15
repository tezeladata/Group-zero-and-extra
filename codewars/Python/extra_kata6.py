#simple calculator
def calculator(x,y,op):
    if op == "+" and (type(x)==int and type(y)==int):
        return x+y
    elif op=="-":
        return x-y
    elif op=="*":
        return x*y
    elif op=="/":
        return x/y
    else:
        return "unknown value"
    
#Is there a vowel in there?
def is_vow(inp):
    for n in range(0, len(inp)):
        if inp[n]==97: inp[n] = "a"
        if inp[n]==101: inp[n] = "e"
        if inp[n]==105: inp[n] = "i"
        if inp[n]==111: inp[n] = "o"
        if inp[n]==117: inp[n] = "u"
    return inp

#Who is going to pay for the wall?
def who_is_paying(name):
    trun=[]
    trun.append(name)
    trun.append(name[:2])
    if len(name)<=2:
        simple=[]
        simple.append(name)
        return simple
    else:
        return trun
    
#Collatz Conjecture (3n+1)
def hotpo(n):
    counter=0
    while n >1:
        if ((n % 2) == 0):
            n= n // 2
        else:
            n = n *3 +1
        counter+=1
    return counter

#Quadrants
def quadrant(x, y):
    if x>0 and y>0:
        return 1
    elif x<0 and y>0:
        return 2
    elif x<0 and y<0:
        return 3
    else:
        return 4
    
#Chuck Norris VII - True or False? (Beginner)
def if_chuck_says_so():
    return 3==5

#Unexpected parsing
def get_status(is_busy):
    status = "busy" if is_busy else "available"
    return {"status": status}

#Thinkful - Number Drills: Blue and red marbles
def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    blue=blue_start-blue_pulled
    red=red_start-red_pulled
    return blue/(blue+red)

#ASCII Total
def uni_total(s):
    a=0
    for i in s:
        a+=ord(i)
    return a

#For UFC Fans (Total Beginners): Conor McGregor vs George Saint Pierre
def quote(fighter):
    a={
        'george saint pierre': "I am not impressed by your performance.",
        'conor mcgregor'     : "I'd like to take this chance to apologize.. To absolutely NOBODY!"
    }
    return a[fighter.lower()]

#Who ate the cookie?
def cookie(x):
    if type(x)==str:
        return "Who ate the last cookie? It was Zach!"
    elif type(x)==float or type(x)==int:
        return "Who ate the last cookie? It was Monica!"
    else:
        return "Who ate the last cookie? It was the dog!"
    
#validate code with simple regex
def validate_code(code):
    a=[int(i) for i in str(code)]
    if a[0]==1 or a[0]==2 or a[0]==3:
        return True
    else:
        return False
    
#Localize The Barycenter of a Triangle
def bar_triang(point_a, point_b, point_c): 
    x=(point_a[0]+point_b[0]+point_c[0])/3
    y=(point_a[1]+point_b[1]+point_c[1])/3
    return [round(x, 4), round(y, 4)]

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