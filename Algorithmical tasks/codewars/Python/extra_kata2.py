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
    
#Mumbling
def accum(s):
    new=""
    for i in range(len(s)):
        new+=s[i].upper()
        new+=(s[i]*(i)).lower()
        new+="-"
    return new.strip("-")

#String ends with?
def solution(text, ending):
    counter=len(ending)
    for i in range(len(ending)):
        if text[-counter:]==ending:
            return True
        else:
            return False
        
#Credit Card Mask
def maskify(cc):
    if len(cc)<=4:
        return cc
    else:
        new=""
        a=len(cc)
        for i in range(a-4):
            new+="#"
        new+=cc[-4:]
    return new

#Friend or Foe?
def friend(x):
    new=[]
    for element in x:
        if len(element)==4:
            new.append(element)
    return new

#Binary Addition
def add_binary(a,b):
    c=bin(a+b)
    d=""
    d+=c[2:]
    return d

#Is this a triangle?
def is_triangle(a, b, c):
    return a+b>c and b+c>a and a+c>b

#Regex validate PIN code
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

#Multiply the number
def multiply(n):
    a=str(n)
    a=a.replace("-","")
    b=len(a)
    return n*5**b

#Two to One
def longest(a1, a2):
    return "".join(sorted(set(a1+a2)))

#Growth of a Population
from math import floor
def nb_year(p0, percent, aug, p):
    a=1
    multip=1+percent/100
    previous=p0
    while previous<p:
        ne=floor((previous*multip+aug))
        previous=ne
        a+=1
    return a-1

#Categorize New Member
def open_or_senior(data):
    new=[]
    for element in data:
        if element[0]>=55 and element[1]>7:
            new.append("Senior")
        else:
            new.append("Open")
    return new

#Find the next perfect square!
import math
def find_next_square(sq):
    a=math.sqrt(sq)
    if a%1==0:
        return (a+1)**2
    else:
        return -1
    
#Printer Errors
def printer_error(s):
    correct_letters="abcdefghijklm"
    counter=0
    length=len(s)
    for i in s:
        if i not in correct_letters:
            counter+=1
    return "{}/{}".format(counter, length)

#Ones and Zeros
def binary_array_to_number(arr):
    new=""
    for i in arr:
        new+=str(i)
    a=int(new, 2)
    return a

#Number of People in the Bus
def number(bus_stops):
    counter=0
    for element in bus_stops:
        counter+=element[0]-element[1]
    return counter

#Reverse words
def reverse_words(text):
    text=list(text.split(" "))
    new=""
    for element in text:
        new+=element[::-1]
        new+=" "
    return new.strip(" ")

#Odd or Even?
def odd_or_even(arr):
    sum_of_all=0
    for i in arr:
        sum_of_all+=i
    if sum_of_all%2==0:
        return "even"
    else:
        return "odd"
    
#The highest profit wins!
def min_max(lst):
    if len(lst)==1:
        new1=[]
        new1.append(lst[0])
        new1.append(new1[0])
        return new1
    else:
        new2=[]
        new2.append(min(lst))
        new2.append(max(lst))
        return new2
    
#Find the divisors!
def divisors(integer):
    divisors=[]
    for x in range(2, integer):
        if integer%x==0:
            divisors.append(x)
    if len(divisors)>0:
        return divisors
    else:
        return "{} is prime".format(integer)
    
#Sum of the first nth term of Series
def series_sum(n):
    num=1
    counter=1
    divisor=4
    while counter<n:
        num+=1/divisor
        divisor+=3
        counter+=1
    if n==0:
        return "0.00"
    else:
        rounded="{:0.2f}".format(num)
        return rounded
    
#Remove the minimum
def remove_smallest(numbers):
    new=[]
    for x in numbers:
        new.append(x)
    if len(numbers)==0:
        return []
    else:
        new.remove(min(new))
        return new
    
#Testing 1-2-3
def number(lines):
    new=[]
    counter=1
    a=len(lines)
    while counter<a+1:
        new.append("{}: {}".format(counter, lines[counter-1]))
        counter+=1
    return new

#Count the divisors of a number
def divisors(n):
    divisors=0
    for x in range(1, n+1):
        if n%x==0:
            divisors+=1
    return divisors

#Find the stray number
def stray(arr):
    for num in arr:
         if arr.count(num)==1:
            return num
         
#Sort Numbers
def solution(nums):
    if type(nums)==list:
        if nums==[]:
            return []
        else:
            if len(nums)>0:
                a=len(nums)
                new=[]
                while a>0:
                    new.append(min(nums))
                    nums.remove(min(nums))
                    a-=1
            return new
    else:
        return []
    
#Breaking chocolate problem
def break_chocolate(n, m):
    if n==0 or m==0:
        return 0
    else:
        return n*m-1
    
#Make a function that does arithmetic!
def arithmetic(a, b, operator):
    if operator=="add":
        return a+b
    elif operator=="subtract":
        return a-b
    elif operator=="multiply":
        return a*b
    else:
        return a/b
    
#Count the Digit
def nb_dig(n, d):
    counter=0
    for i in range(n+1):
        counter+=str(i**2).count(str(d))
    return counter

#Anagram Detection
def is_anagram(test, original):
    return sorted(test.lower())==sorted(original.lower())

#Sum of a sequence
def sequence_sum(begin_number, end_number, step):
    count=0
    for x in range(begin_number, end_number+1, step):
        count+=x
    return count

#Sum of odd numbers
def row_sum_odd_numbers(n):
    return n**3

#Money, Money, Money
def calculate_years(principal, interest, tax, desired):
    count=0
    while principal<desired:
        principal+=(interest*principal) * (1-tax)
        count+=1
    return count

#Remove anchor from URL
def remove_url_anchor(url):
    for i in url:
        if "#" in url:
            a=url.index("#")
            return url[0:a]
        else:
            return url
        
#Don't give me five!
def dont_give_me_five(start,end):
    new=[]
    for i in range(start, end+1):
        if "5" not in str(i):
            new.append(i)
        
    return len(new)

#Factorial
def factorial(n):
    factorial=1
    if 0<n<=12:
        for i in range(1, n+1):
            factorial*=i
        return factorial
    else:
        if n==0:
            return 1
        elif n<0:
            raise ValueError
        else:
            raise ValueError
        
#Find the capitals
def capitals(word):
    word=list(word)
    index=[]
    i=0
    for letter in word:
        if letter.isupper():
            index.append(i)
        i+=1
    return index

#Small enough? - Beginner
def small_enough(array, limit):
    for i in array:
        if max(array)<=limit:
            return True
        else:
            return False
        
#Summing a number's digits
def sum_digits(number):
    if number<0:
        number*=-1
    number=str(number)
    count=0
    for i in number:
        count+=int(i)
    return count

#Leap Years
def is_leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
#Sum of angles
def angle(n):
    return 180*(n-2)

#Two Oldest Ages
def two_oldest_ages(ages):
    new=[]
    new.append(max(ages))
    ages.remove(max(ages))
    new.append(max(ages))
    if new[0]>new[1]:
        new2=[]
        new2.append(new[1])
        new2.append(new[0])
        return new2
    else:
        return new
    
#Find the middle element
def gimme(input_array):
    return input_array.index(sorted(input_array)[1])

#Simple Fun 176: Reverse Letter
def reverse_letter(string):
    new_str=""
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for i in string:
        if i in alphabet:
            new_str+=i
    return new_str[::-1]

#Round up to the next multiple of 5
def round_to_next5(n):
    if n%5==0:
        return n
    else:
        if n%5==1:
            return n+4
        elif n%5==2:
            return n+3
        elif n%5==3:
            return n+2
        elif n%5==4:
            return n+1
        
#Maximum Multiple
def max_multiple(divisor, bound):
    new=[]
    for i in range(divisor, bound+1):
        if i%divisor==0:
            new.append(i)
    return max(new)

#The Coupon Code
def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if not isinstance(entered_code, str) or not isinstance(correct_code, str):
        return False
    months={
        "January": 1,
        "February": 2, 
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6, 
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10, 
        "November": 11,
        "December": 12
    }
    if entered_code==correct_code:
        current=current_date.split(", ")
        expiration=expiration_date.split(", ")
        curyear=int(current[-1])
        expyear=int(expiration[-1])
        if curyear>expyear:
            return False
        elif curyear<expyear:
            return True
        else:
            cm, cd = current[0].split()
            em, ed = expiration[0].split()
            if months[cm]<months[em]:
                return True
            elif months[em]<months[cm]:
                return False
            else:
                return int(cd) <= int(ed)
    else:
        return False

#No oddities here
def no_odds(values):
    if values==[]:
        return []
    else:
        return [x for x in values if x%2==0]
    
#Alternate capitalization
def capitalize(s):
    word=""
    last=[]
    for i in range(0, len(s)):
        if i%2==0:
            word=word+s[i].upper()
        else:
            word=word+s[i]
    last.append(word)
    last.append(word.swapcase())
    return last

#Triangular Treasure
def triangular(n):
    if n<0:
        return 0
    else:
        return n*(n+1)//2
    
#Maximum Length Difference
def mxdiflg(a1, a2):
    max=-1
    for i in a1:
        for x in a2:
            c= abs(len(i) - len(x))
            if c>max:
                max=c
    return max

#Fix string case
def solve(s):
    count_of_lower=0
    count_of_upper=0
    for i in s:
        if i==i.upper():
            count_of_upper+=1
        else:
            count_of_lower+=1
    if count_of_lower==count_of_upper:
        return s.lower()
    elif count_of_lower>count_of_upper:
        return s.lower()
    elif count_of_lower<count_of_upper:
        return s.upper()
    
#Are the numbers in order?
def in_asc_order(arr):
    return arr==sorted(arr)

#Check the exam
def check_exam(arr1,arr2):
    score=0
    for i in range(0, 4):
        if arr2[i]==arr1[i]:
            score+=4
        elif arr2[i]=="":
            pass
        elif arr2[i]!=arr1[i]:
            score-=1
    if score>0:
        return score
    elif score<0:
        return 0
    
#Number of Decimal Digits
def digits(n):
    n=str(n)
    a=len(n)
    return a

#Two fighters, one winner.
def declare_winner(fighter1, fighter2, first_attacker):
    if fighter1.name==first_attacker:
        attacker, defender = fighter1, fighter2
    else:
        attacker, defender = fighter2, fighter1
    while True:
        defender.health-=attacker.damage_per_attack
        if defender.health <=0:
            return attacker.name
        else:
            attacker, defender = defender, attacker

#Deodorant Evaporator
import math
def evaporator(content, evap_per_day, threshold):
    return math.ceil(math.log(threshold/100)/ math.log(1.0 - evap_per_day / 100))

#Flatten and sort an array
def flatten_and_sort(a):
    return sorted([i for s in a for i in s])
#or
def flatten_and_sort(array):
    new=[]
    for element in array:
        new+=element
    return sorted(new)

#Form The Minimum
def min_value(digits):
    new=""
    for number in sorted(digits):
        number=str(number)
        if number not in new:
            new+=number
    return int(new)

#Fizz Buzz
def fizzbuzz(n):
    new=[]
    for i in range(1, n+1):
        if i%3==0 and i%5!=0:
            new.append("Fizz")
        elif i%5==0 and i%3!=0:
            new.append("Buzz")
        elif i%15==0:
            new.append("FizzBuzz")
        else:
            new.append(i)
    return new

#Factorial
def factorial(n):
    ans=1
    for i in range(1, n+1):
        ans*=i
    return ans

#Power of two
def power_of_two(x):
    current_number = 0
    counter = 0
    while current_number <= x:
        current_number = 2**counter
        counter+=1
        if current_number == x:
            return True
    return False   

#Sum of Minimums!
def sum_of_minimums(numbers):
    a=0
    for i in range(len(numbers)):
        a+=min(numbers[i])
    return a