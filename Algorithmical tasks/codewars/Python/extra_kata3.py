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