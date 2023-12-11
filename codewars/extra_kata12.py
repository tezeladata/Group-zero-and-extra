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