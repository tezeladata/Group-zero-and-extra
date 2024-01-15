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

#Bit Counting
def count_bits(n):
    n=bin(n)
    n=str(n)
    count=0
    for i in n:
        if i=="1":
            count+=1
    return count

#Counting Duplicates
def duplicate_count(text):
    dupes=[]
    text=text.lower()
    for chr in text:
        count=text.count(chr)
        if count>1:
            if chr not in dupes:
                dupes.append(chr)
    return len(dupes)

#Duplicate Encoder
def duplicate_encode(word):
    word=word.lower()
    new=""
    for i in word:
        if word.count(i)>1:
            new+=")"
        else:
            new+="("
    return new

#Find The Parity Outlier
def find_outlier(integers):
    even=[]
    odd=[]
    for i in integers:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    if len(even)==1:
        return even[0]
    else:
        return odd[0]
    
#Replace With Alphabet Position
def alphabet_position(text):
    text=text.lower()
    alphabet={
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26  
    }
    new_str=""
    new_arr=[]
    for i in text:
        if i in alphabet:
            new_str+=str(alphabet[i])
            new_arr.append(str(alphabet[i]))
        else:
            continue
    if len(new_str)==1 or len(new_str)==2:
        return new_str
    else:
        return " ".join(new_arr)
        
#Persistent Bugger.
def persistence(n):
    a=0
    while n>9:
        a+=1
        n_str=str(n)
        total=1
        for i in n_str:
            total=total*int(i)
        n=total
    return a
            
#Take a Ten Minutes Walk
def is_valid_walk(walk):
    ab=walk.count("s")==walk.count("n")
    cd=walk.count("e")==walk.count("w")
    length=len(walk)==10
    return ab and cd and length

#Convert string to camel case
def to_camel_case(text):
    text=text.replace("-", "_")
    text=text.split("_")
    a=0
    c_case=""
    for word in text:
        a+=1
        if a==1:
            c_case+=word
        else:
            c_case+=word.capitalize()
    return c_case

#Moving Zeros To The End
def move_zeros(lst):
    new_arr=[]
    for i in lst:
        if i!=0:
            new_arr.append(i)
    a=lst.count(0)
    for i in range(a):
        new_arr.append(0)
    return new_arr

#Does my number look big in this?
def narcissistic( value ):
    a=str(value)
    b=len(a)
    count=0
    for i in range(b):
        count+=int(a[i])**b
    if count==value:
        return True
    else:
        return False
    
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