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