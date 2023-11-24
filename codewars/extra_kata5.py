#Get Nth Even Number
def nth_even(n):
    return n*2-2

#Remove duplicates from list
def distinct(seq):
    answer=[]
    for i in seq:
        if i not in answer:
            answer.append(i)
    return answer

#5 without numbers !!
def unusual_five():
    return len("abcde")

#Merge two sorted arrays into one
def merge_arrays(arr1, arr2):
    a=sorted(set(arr1+arr2))
    return a

#Super Duper Easy
def problem(a):
    if type(a)!=str:
        return a*50+6
    else:
        return "Error"

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
     
#