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