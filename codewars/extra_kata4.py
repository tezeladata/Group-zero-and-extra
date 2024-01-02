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