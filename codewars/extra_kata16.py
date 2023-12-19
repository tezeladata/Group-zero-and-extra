#Switcheroo
def switcheroo(s):
    res=""
    for letter in s:
        if letter=="a":
            letter="b"
        elif letter=="b":
            letter="a"
        res+=letter
    return res

#Sum of Triangular Numbers
def sum_triangular_numbers(n):
    if n<0:
        return 0
    else:
        return (n*(n+1)*(n+2))/6
    
#Even numbers in an array
def even_numbers(arr,n):
    new=[]
    for num in arr:
        if num%2==0:
            new.append(num)
    return new[-n:]

#Filter the number
def filter_string(string):
    new=""
    for i in string:
        if i>="0" and i<="9":
            new+=i
    return int(new)

#Simple beads count
def count_red_beads(n):
    if n<2:
        return 0
    else:
        return (n-1)*2
    
#Boiled Eggs
import math
def cooking_time(eggs):
    a=math.ceil(eggs/8)
    return a*5

#Functional Addition
def add(n):
    return lambda x: x+n

#My Language Skills
def my_languages(results):
    new=[]
    for key, value in results.items():
        if value>=60:
            new.append(key)
    return sorted(new, key=lambda x: results[x], reverse=True)

#Sort arrays - 1
def sortme(names):
    return sorted(names)

#Speed Control
def gps(s, x):
    if len(x)<2:
        return 0
    else:
        numb=max(x[i] - x[i-1] for i in range(1, len(x)))
    return numb*3600.0/s

#Minimize Sum Of Array (Array Series #1)
def min_sum(arr):
    arr=sorted(arr)
    last_num=0
    for i in range(len(arr)//2):
        last_num+=arr[i]*arr[-i-1]
    return last_num

#Odd-Even String Sort
def sort_my_string(s):
    even=""
    odd=""
    for i in range(0, len(s), 2):
        even+=s[i]
    for i in range(1, len(s), 2):
        odd+=s[i]
    return "{} {}".format(even, odd)

#Maximum Triplet Sum (Array Series #7)
def max_tri_sum(numbers):
    numbers=set(numbers)
    numbers=list(numbers)
    a=0
    a+=max(numbers)
    numbers.remove(max(numbers))
    a+=max(numbers)
    numbers.remove(max(numbers))
    a+=max(numbers)
    return a

#Most digits
def find_longest(arr):
    len_arr=[]
    for i in arr:
        len_arr.append(len(str(i)))
    return arr[len_arr.index(max(len_arr))]

#Multiples of 3 or 5
def solution(number):
    if number<0:
        return 0
    else:
        count=0
        for i in range(1, number):
            if i%3==0 or i%5==0:
                count+=i
        return count
    
#Who likes it?
def likes(names):
    if len(names)==0:
        return "no one likes this"
    elif len(names)==1:
        return "{} likes this".format(names[0])
    elif len(names)==2:
        return "{} and {} like this".format(names[0], names[1])
    elif len(names)==3:
        return "{}, {} and {} like this".format(names[0], names[1], names[2])
    else:
        return "{}, {} and {} others like this".format(names[0], names[1], len(names)-2)
    
#Create Phone Number
def create_phone_number(n):
    first="({}{}{})".format(n[0], n[1], n[2])
    second="{}{}{}-{}{}{}{}".format(n[3], n[4], n[5], n[6], n[7], n[8], n[9],)
    return "{} {}".format(first, second)

#Find the odd int
def find_it(seq):
    for i in seq:
        if (seq.count(i))%2!=0:
            return i
        
#Sum of Digits / Digital Root
def digital_root(n):
    a=sum([int(num) for num in str(n)])
    if len(str(a)) >=2:
        a=digital_root(a)
    return a