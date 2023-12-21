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