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