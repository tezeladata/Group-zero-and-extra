#Smallest unused ID
def next_id(arr):
    for i in range(len(arr)+1):
        if i not in arr:
            return i

#Fundamentals: Return
def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def mod(a,b):
    return a%b
def exponent(a,b):
    return a**b
def subt(a,b):
    return a-b

#Fix your code before the garden dies!
def rain_amount(mm):
    if mm < 40:
        return "You need to give your plant " + str(40-mm) + "mm of water"
    else:
         return "Your plant has had more than enough water for today!"
    
#get ascii value of character
def get_ascii(ch : str) -> int:
    return ord(ch)

#CSV representation of array
def to_csv_text(array):
    new=[]
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j]=str(array[i][j])
        new.append(",".join(array[i]))
    return "\n".join(new)

#Contamination #1 -String-
def contamination(text, char):
    new=""
    if text=="":
        return ""
    elif char=="":
        return ""
    else:
        for i in range(len(text)):
            new+=char
    return new

#Closest elevator
def elevator(left, right, call):
    l=abs(left-call)
    r=abs(right-call)
    if l<r:
        return "left"
    else:
        return "right"
    
#A Strange Trip to the Market
def is_lock_ness_monster(string):
    if "tree fiddy" in string or "three fifty" in string or "3.50" in string:
        return True
    else:
        return False
    
#Pythagorean Triple
def pythagorean_triple(integers):
    a, b, c = sorted(integers)
    if a**2 + b**2 == c**2:
        return True
    else:
        return False
    
#Exclamation marks series #4: Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string
def remove(s):
    new=""
    for i in s:
        if i!="!":
            new+=i
    return new+"!"

#Geometry Basics: Distance between points in 2D
import math
def distance_between_points(a, b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

#Leonardo Dicaprio and Oscars
def leo(oscar):
    if oscar>88:
        return "Leo got one already!"
    elif oscar==88:
        return "Leo finally won the oscar! Leo is happy"
    elif oscar==86:
        return "Not even for Wolf of wallstreet?!"
    else:
        return "When will you give Leo an Oscar?"
    
#Exclamation marks series #6: Remove n exclamation marks in the sentence from left to right
def remove(s, n):
    return s.replace("!", "", n)

#Tip Calculator
import math
def calculate_tip(amount, rating):
    rating=rating.lower()
    tip={
        "terrible": 0,
        "poor": 0.05,
        "good": 0.1,
        "great": 0.15,
        "excellent": 0.2
    }.get(rating)
    if tip==None:
        return 'Rating not recognised'
    return int(math.ceil(amount*tip))

#Are arrow functions odd?
def odds(values):
    return [x for x in values if x%2==1]

#Compare within margin
def close_compare(a, b, margin=0):
    if a-b>margin:
        return 1
    elif b-a>margin:
        return -1
    else:
        return 0
    
#BASIC: Making Six Toast.
def six_toast(num):
    if num>6:
        return num-6
    elif num==6:
        return 0
    else:
        return 6-num
    
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