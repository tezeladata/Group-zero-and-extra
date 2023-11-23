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