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

#