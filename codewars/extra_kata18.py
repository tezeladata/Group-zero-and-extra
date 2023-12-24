#Your order, please
def order(sentence):
    new=[]
    for i in range(1, 10):
        for word in sentence.split():
            if str(i) in word:
                new.append(word)
    return " ".join(new)

#Split Strings
def solution(s):
    if len(s)%2!=0:
        s+="_"
    new_arr=[]
    for index in range(0, len(s), 2):
        new_arr.append(s[index:index+2])
    return new_arr

#Get number from string
def get_number_from_string(string):
    new=""
    for i in string:
        if i.isdigit()==True:
            new+=i
    return int(new)

#Palindrome chain length
def check(a):
    return str(a)==str(a)[::-1]

def palindrome_chain_length(n):
    count=0
    while check(n)!=True:
        n=n+int(str(n)[::-1])
        count+=1
    return count

#Divide and Conquer
def div_con(x):
    strs=[]
    ints=[]
    for i in x:
        if type(i)==str:
            strs.append(int(i))
        elif type(i)==int:
            ints.append(i)
    return sum(ints)-sum(strs)

#Smallest value of an array
def find_smallest(numbers, to_return):
    if to_return=="value":
        return min(numbers)
    else:
        a=min(numbers)
        return numbers.index(a)
    
#Ordered Count of Characters
def ordered_count(inp):
    new_arr=[]
    for i in inp:
        occurences=(i, inp.count(i))
        if occurences not in new_arr:
            new_arr.append(occurences)
    return new_arr

#Number Of Occurrences
def number_of_occurrences(element, sample):
    return sample.count(element)

#Largest Square Inside A Circle
def area_largest_square(r):
    square_side=(r**2 + r**2)**0.5
    return round(square_side**2)

#Convert an array of strings to array of numbers
def to_float_array(arr): 
    new_arr=[]
    for i in arr:
        new_arr.append(float(i))
    return new_arr

#Perimeter sequence
def perimeter_sequence(a, n): 
    return 4*(a*n)

#Halving Sum
def halving_sum(n): 
    if n==1:
        return 1
    else:
        return n+halving_sum(n//2)
    
#Reverse a Number
def reverse_number(n):
    if n<0:
        res=""
        res+="-"
        n=str(n)
        for i in range(len(n)):
            res+=n[-i]
        return int(res[1:])
    elif 0<=n<=9:
        return n
    else:
        n=str(n)
        return int(n[::-1])

#Is a number prime?
def is_prime(num):
    if num<=0 or num==1:
        return False
    i=2
    while (i<=num**0.5):
        if num%i==0:
            return False
        i+=1
    return True

#Are they the "same"?
def comp(array1, array2):
    if type(array1)!=list or type(array2)!=list:
        return False
    res=[]
    for i in array1:
        res.append(i**2)
    return sorted(res)==sorted(array2)