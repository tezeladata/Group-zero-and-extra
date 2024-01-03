#Char Code Calculation
def calc(x):
    ascii1=""
    for char in x:
        ascii1 += str(ord(char))
    ascii2=""
    for char in ascii1:
        if char!="7":
            ascii2+=char
        else:
            ascii2+="1"
    sum1=0
    sum2=0
    for char in ascii1:
        sum1+=int(char)
    for char in ascii2:
        sum2+=int(char)
    return sum1-sum2

#Find Count of Most Frequent Item in an Array
def most_frequent_item_count(collection):
    if collection==[]:
        return 0
    else:
        a=max(set(collection), key=collection.count)
        return collection.count(a)
    
#Substituting Variables Into Strings: Padded Numbers
def solution(value):
    if len(str(value))==1:
        return 'Value is 0000{}'.format(value)
    elif len(str(value))==2:
        return 'Value is 000{}'.format(value)
    elif len(str(value))==3:
        return 'Value is 00{}'.format(value)
    elif len(str(value))==4:
        return 'Value is 0{}'.format(value)
    else:
        return 'Value is {}'.format(value)
    
#shorter concat [reverse longer]
def shorter_reverse_longer(a,b):
    if len(a)==len(b):
        return "{}{}{}".format(b, a[::-1], b)
    else:
        if len(a)>len(b):
            return "{}{}{}".format(b, a[::-1], b)
        else:
            return "{}{}{}".format(a, b[::-1], a)
        
#Vowel one
def vowel_one(s):
    new_str=""
    vowels=["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    for char in s:
        if char in vowels:
            new_str+="1"
        else:
            new_str+="0"
    return new_str

#Automorphic Number (Special Numbers Series #6)
def automorphic(n):
    square = n**2
    n_str = str(n)
    square_str = str(square)
    
    if square_str.endswith(n_str):
        return "Automorphic"
    else:
        return "Not!!"
    
#Alternate case
def alternate_case(s):
    return s.swapcase()

#Sum of array singles
def repeats(arr):
    count=0
    for num in arr:
        if arr.count(num)==1:
            count+=num
    return count

#Spacify
def spacify(string):
    return " ".join(list(string))

#Averages of numbers
def averages(arr):
    if arr:
        avg=[]
        for i in range(len(arr)-1):
            avg.append((arr[i] + arr[i+1])/2)
        return avg
    else:
        return []
    
#Tidy Number (Special Numbers Series #9)
def tidyNumber(n):
    a=list(str(n))
    a.sort()
    int_a=""
    for i in a:
        int_a+=i
    return int(int_a)==n

#Sort Out The Men From Boys
def men_from_boys(arr):
    even_arr=[]
    for num in sorted(arr):
        if num%2==0:
            even_arr.append(num)
    arr.sort(reverse=True)
    odd_arr=[]
    for num in arr:
        if num%2!=0:
            odd_arr.append(num)
    arr1=[]
    for i in even_arr:
        arr1.append(i)
    for i in odd_arr:
        arr1.append(i)
    res=[]
    for num in arr1:
        if num not in res:
            res.append(num)
    return res

#Return the Missing Element
def get_missing_element(seq): 
    all_elements = set(range(10))
    sequence_set = set(seq)
    missing_element = all_elements.difference(sequence_set).pop()
    return missing_element