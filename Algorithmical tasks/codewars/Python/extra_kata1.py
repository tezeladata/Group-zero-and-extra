#To square(root) or not to square(root)
import math
def square_or_square_root(arr):
    new=[]
    for i in arr:
        square_root=i**0.5
        if square_root.is_integer():
            new.append(square_root)
        else:
            new.append(i**2)
    return new

#A wolf in sheep's clothing
def warn_the_sheep(queue):
    i=len(queue) - queue.index("wolf") - 1
    if i==0:
        return "Pls go away and stop eating my sheep"
    else:
        return "Oi! Sheep number {}! You are about to be eaten by a wolf!".format(i)
        
#Determine offspring sex based on genes XX and XY chromosomes
def chromosome_check(chromosome):
    if "XX" in chromosome:
        return "Congratulations! You're going to have a daughter."
    elif "XY" in chromosome:
        return "Congratulations! You're going to have a son."

#Convert to Binary
def to_binary(n):
    a=bin(n)
    return int(a[2:])

#The Wide-Mouthed frog!
def mouth_size(animal): 
    animal=animal.upper()
    if animal=="ALLIGATOR":
        return "small"
    else:
        return "wide"
    
#Well of Ideas - Easy Version
def well(x):
    if x.count("good")==1 or x.count("good")==2:
        return "Publish!"
    elif x.count("good")>2:
        return "I smell a series!"
    else:
        return "Fail!"
    
#Holiday VIII - Duty Free
def duty_free(price, discount, holiday_cost):
    new_price=price * discount / 100
    return int(holiday_cost / new_price)

#Add Length
def add_length(str_):
    new=[]
    for word in str_.split():
        new.append(word + " " + str(len(word)))
    return new

#Bin to Decimal
def bin_to_decimal(inp):
    return int(inp, 2)

#The 'if' function
def _if(bool, func1, func2):
    if bool==True:
        func1()
    else:
        func2()

#FIxme: Replace all dots
def replace_dots(s):
    return s.replace(".", "-")

#Hello, Name or World!
def hello(name=""):
    if name!="":
        return "Hello, " + name.capitalize() + "!"
    else:
        return "Hello, World!"
    
#Hex to Decimal
def hex_to_dec(s):
    hex={
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3, 
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "a": 10,
        "b": 11,
        "c": 12,
        "d": 13,
        "e": 14,
        "f": 15
        }
    sum=0
    lenght=len(s)-1
    for i in s:
        sum +=hex[i] * 16**lenght
        lenght-=1
    return sum

#Grasshopper - Function syntax debugging
def main(verb, noun):
    return verb + noun

#No zeros for heros
def no_boring_zeros(n):
    if n==0:
        return n
    else:
        while n%10==0:
            n=n/10
    return n
        
#Grasshopper - Terminal game combat function
def combat(health, damage):
    if health>damage:
        return health-damage
    else:
        return 0

#Exclamation marks series #1: Remove an exclamation mark from the end of string
def remove(s):
    if s!="":
        if s[-1]=="!":
            return s[0:-1]
        else:
            return s
    else:
        return ""
    
#Enumerable Magic #25 - Take the First N Elements
def take(arr,n):
    if n>0:
        return arr[:n]
    else:
        return []
    
#Welcome to the City
def say_hello(name, city, state):
    names=" ".join(name)
    return "Hello, {}! Welcome to {}, {}!".format(names, city, state)

#Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence
def replace_exclamation(s):
    for i in "AEIOUaeiou":
        s=s.replace(i, "!")
    return s

#Is this my tail?
def correct_tail(body, tail):
     if body[-1]==tail:
        return True
     else:
        return False
     
#Find the position!
def position(alphabet):
    alph={
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26 
    }
    for i in alphabet:
        return "Position of alphabet: {}".format(alph[i])
    
#Alan Partridge II - Apple Turnover
def apple(x):
    if type(x)==int:
        if x**2>1000:
            return "It's hotter than the sun!!"
        else:
            return "Help yourself to a honeycomb Yorkie for the glovebox."
    elif int(x)**2>1000:
        return "It's hotter than the sun!!"
    elif int(x)**2<1000:
        return "Help yourself to a honeycomb Yorkie for the glovebox."
    
#Grasshopper - Debug
def weather_info (temp):
    c = convert_to_celsius(temp)
    if (c < 0):
        return (str(c) + " is freezing temperature")
    else:
        return (str(c) + " is above freezing temperature")
    
def convert_to_celsius (temperature):
    celsius = (temperature - 32) * (5/9)
    return celsius

#Find the Remainder
def remainder(a,b):
    if min(a,b)==0:
        return None
    elif a>b:
        return a%b
    else:
        return b%a
    
#Generate range of integers
def generate_range(min, max, step):
    a=[]
    for i in range(min, max+1, step):
        a.append(i)
    return a

#101 Dalmatians - squash the bugs, not the dogs!
def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    if n <=10:
        respond=dogs[0]
    elif n <=50:
        respond=dogs[1]
    elif n==101:
        respond=dogs[3]
    else:
        respond=dogs[2]
    return respond

#Price of Mangoes
def mango(quantity, price):
    return price * (quantity - (quantity // 3))

#Surface Area and Volume of a Box
def get_size(w,h,d):
    answer=[]
    answer.append(2*(w*h + w*d + h*d))
    answer.append(w*h*d)
    return answer

#Printing Array elements with Comma delimiters
def print_array(arr):
    if arr!=None:
        return ",".join(str(i) for i in arr)
    
#Remove First and Last Character Part Two
def array(string):
    a= string.strip().split(",")
    b= a[1:-1]
    c= " ".join(b)
    if len(c)==0:
        return None
    else:
        return c

#Reversing Words in a String
def reverse(st):
    st=st.split()
    st.reverse()
    return " ".join(st)

#Pillars
def pillars(num_pill, dist, width):
    if num_pill<=1:
        return 0
    else:
        return (num_pill-2)*width + (num_pill-1)*dist*100
    
#Dollars and Cents
def format_money(amount):
    dollar=int(amount)
    cent=str(int((amount-dollar)*100 +0.1))
    if len(cent)<1:
        cent="00"
    elif len(cent)<2:
        cent+="0"
    return "$" + str(dollar) + "." + cent

#Return to Sanity
def mystery():
    results = {
    'sanity': 'Hello'
    }
    return results

#String cleaning
def string_clean(s):
    new=""
    for i in s:
        if i not in "0123456789":
            new+=i
    return new

#Sum of differences in array
def sum_of_differences(arr):
    arr.sort(reverse=True)
    sum=0
    i=1-1
    if len(arr)==0:
        return 0
    else:
        while i!=len(arr)-1:
            sum=sum+(arr[i] - arr[i+1])
            i+=1
    return sum


#Simple Fun #1: Seats in Theater
def seats_in_theater(tot_cols, tot_rows, col, row):
    return ((tot_cols-col+1)*(tot_rows-row))

#Grasshopper - Array Mean
def find_average(nums):
    if len(nums)>=1:
        return sum(nums) / len(nums)
    else:
        return 0

#Exclusive "or" (xor) Logical Operator
def xor(a,b):
    return a!=b

#Regular Ball Super Ball
class Ball(object):
    def __init__(self, object="regular"):
        self.ball_type = object

#Gravity Flip
def flip(d, a):
    if d == "L":
        return sorted(a, reverse=True)
    else:
        return sorted(a)
    
#Enumerable Magic - Does My List Include This?
def include(arr,item):
    if item in arr:
        return True
    else:
        return False
    
#Sum of Multiples
def sum_mul(n, m):
    sum=0
    if m>0 and n>0:
        for i in range(n,m,n):
            sum+=i
        return sum
    else:
        return "INVALID"
    
#Find out whether the shape is a cube
def cube_checker(volume, side):
    if side>0:
        if side**3==volume:
            return True
        else:
            return False
    else:
        return False
    
#Multiple of index
def multiple_of_index(arr):
    new=[]
    if arr[0]==0:
        new.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i]%i==0:
            new.append(arr[i])
    return new

#Simple validation of a username with regex
def validate_usr(username):
    if len(username)<4 or len(username)>16:
        return False
    for i in username:
        if i not in "abcdefghijklmnopqrstuvwxyz0123456789_":
            return False
    return True

#Kata Example Twist
websites = []
for i in range(1000):
    websites.append("codewars")

#Swap Values
def swap_values(args): 
    args[0], args[1] = args[1], args[0]

#Check same case
def same_case(a, b): 
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower="abcdefghijklmnopqrstuvwxyz"
    if a in upper and b in upper:
        return 1
    elif a in lower and b in lower:
        return 1
    elif a in upper and b in lower:
        return 0
    elif a in lower and b in upper:
        return 0
    else:
        return -1
    
#Find Nearest square number
import math
def nearest_sq(n):
    root=round(math.sqrt(n))
    return root * root

#Take the Derivative
def derive(coefficient, exponent): 
    der=coefficient*exponent
    return "{}x^{}".format(der, exponent-1)

#Sleigh Authentication
class Sleigh(object):
    def authenticate(self, name, password):
        if name=="Santa Claus" and password=="Ho Ho Ho!":
            return True
        else:
            return False
        
#L1: Bartender, drinks!
def get_drink_by_profession(param):
    param=param.lower()
    if param=="jabroni":
        return "Patron Tequila"
    elif param=="school counselor":
        return "Anything with Alcohol"
    elif param=="programmer":
        return "Hipster Craft Beer"
    elif param=="bike gang member":
        return "Moonshine"
    elif param=="politician":
        return "Your tax dollars"
    elif param=="rapper":
        return "Cristal"
    else:
        return "Beer"
    
#String Templates - Bug Fixing #5
def build_string(*args):
    return "I like {}!".format(", ".join(args))

#Never visit a . . . !?
fruit = ["kiwi",
    "pear",
    "kiwi",
    "banana",
    "melon",
    "banana",
    "melon",
    "pineapple",
    "apple",
    "pineapple",
    "cucumber",
    "cucumber",
    "pineapple",
    "orange",
    "grape",
    "orange",
    "grape",
    "apple",
    "grape",
    "cherry",
    "pear",
    "cherry",
    "pear",
    "kiwi",
    "banana",
    "kiwi",
    "apple",
    "melon",
    "banana",
    "melon",
    "pineapple",
    "melon",
    "pineapple",
    "cucumber",
    "orange",
    "apple",
    "orange",
    "grape",
    "orange",
    "grape",
    "cherry",
    "pear",
    "cherry",
    "pear",
    "apple",
    "pear",
    "kiwi",
    "banana",
    "kiwi",
    "banana",
    "melon",
    "pineapple",
    "melon",
    "apple",
    "cucumber",
    "pineapple",
    "cucumber",
    "orange",
    "cucumber",
    "orange",
    "grape",
    "cherry",
    "apple",
    "cherry",
    "pear",
    "cherry",
    "pear",
    "kiwi",
    "pear",
    "kiwi",
    "banana",
    "apple",
    "banana",
    "melon",
    "pineapple",
    "melon",
    "pineapple",
    "cucumber",
    "pineapple",
    "cucumber",
    "apple",
    "grape",
    "orange",
    "grape",
    "cherry",
    "grape",
    "cherry",
    "pear",
    "cherry",
    "apple",
    "kiwi",
    "banana",
    "kiwi",
    "banana",
    "melon",
    "banana",
    "melon",
    "pineapple",
    "apple",
    "pineapple"]
    
def sum_digits(number):
    sm=0
    for n in list(str(number)):
        sm+=int(n)
    return sm
    
def subtract_sum(number):
    result=number-sum_digits(number)
    if result<100:
        return fruit[result-1]
    else:
        return subtract_sum(result)
    
#Return the day
def whatday(num):
    days={
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    if 1<=num<=7:
        return days[num]
    else:
        return "Wrong, please enter a number between 1 and 7"
    
#Basic Training: Add item to an Array
websites.append("codewars")

#Area of a Square
import math
def square_area(A):
    r=(A*4)/(2*math.pi)
    return round(r*r,2)

#Triple Trouble
def triple_trouble(one, two, three):
    new=""
    for i in range(len(one)):
        new+=one[i]
        new+=two[i]
        new+=three[i]
    return new

#How old will I be in 2099?
def calculate_age(year_of_birth, current_year):
    if year_of_birth-1>current_year:
        return "You will be born in {} years.".format(year_of_birth-current_year)
    elif year_of_birth==current_year:
        return "You were born this very year!"
    elif year_of_birth-1 == current_year:
        return "You will be born in {} year.".format(year_of_birth-current_year)
    elif current_year-1 == year_of_birth:
        return "You are {} year old.".format(current_year-year_of_birth)
    else:
        return "You are {} years old.".format(current_year-year_of_birth)

#Regex count lowercase letters
def lowercase_count(strng):
    count=0
    for i in strng:
        if i!=i.upper():
            count+=1
    return count

#USD => CNY
def usdcny(usd):
    chn=str(usd*6.75)
    if "." in chn:
        if chn[-2]==".":
            chn+="0"
    else:
        chn+="00"
    return "{} Chinese Yuan".format(chn)

#Formatting decimal places #0
def two_decimal_places(n):
    return round(n*100)/100

#Name on billboard
def billboard(name, price=30):
    new=0
    for i in name:
        new+=price
    return new

#How many stairs will Suzuki climb in 20 years?
def stairs_in_20(stairs):
    total=0
    for day in stairs:
        for stair in day:
            total+=stair
    return total*20

#OOP: Object Oriented Piracy
class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    def is_worth_it(self):
        return self.draft - self.crew *1.5 > 20
    
#Miles per gallon to kilometers per liter
def converter(mpg):
    return round(mpg * 1.609344 / 4.54609188, 2)

#Incorrect division method
def divide_numbers(x,y):
    return x / y

#Holiday VI - Shark Pontoon
def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin==True:
        shark_speed=shark_speed*0.5
    my_time=pontoon_distance / you_speed
    shark_time=shark_distance / shark_speed
    if my_time>shark_time:
        return "Shark Bait!"
    else:
        return "Alive!"
    
#Define a card suit
def define_suit(card):
    if card[-1]=="C":
        return "clubs"
    elif card[-1]=="D":
        return "diamonds"
    elif card[-1]=="H":
        return "hearts"
    else:
        return "spades"
    
#Do you speak "English"?
def sp_eng(sentence): 
    return "english" in sentence.lower()

#SpeedCode #2 - Array Madness
def array_madness(a,b):
    new_arr1=[]
    new_arr2=[]
    for i in a:
        new_arr1.append(i**2)
    for x in b:
        new_arr2.append(x**3)
    return sum(new_arr1) > sum(new_arr2)

#No Loops 2 - You only need one
def check(a, x): 
    return x in a

#Grasshopper - Combine strings
def combine_names(first_name, last_name):
    return "{} {}".format(first_name, last_name)

#Find the Difference in Age between Oldest and Youngest Family Members
def difference_in_ages(ages):
    new=(min(ages), max(ages), max(ages)-min(ages))
    return new

#The falling speed of petals
def sakura_fall(v):
    if v>0:
        return 400/v
    else:
        return 0
    
#Remove the time
def shorten_to_date(long_date):
    numb=long_date.index(",")
    return long_date[0:numb]

#Exclamation marks series #2: Remove all exclamation marks from the end of sentence
def remove(s):
    while s[-1]=="!":
        s=s[:-1]
    return s

#Is it a number?
def is_digit(s):
    if len(s)==0 or s[0] not in "-+.0123456789":
        return False
    for char in s[1:]:
        if char not in ".0123456789":
            return False
    return True

#Regexp Basics - is it a digit?
def is_digit(n):
    return n in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

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