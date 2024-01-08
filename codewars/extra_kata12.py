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

#Sum of Odd Cubed Numbers
def cube_odd(arr):
    new_arr=[]
    for i in arr:
        if type(i)==int:
            new_arr.append(i**3)
        else:
            return None
    sum=0
    for num in new_arr:
        if num%2!=0:
            sum+=num
    return sum

#How many arguments
def args_count(*args, **kwargs):
    return len(args) + len(kwargs)
    #arg-positional kwarg-keyword

#Debug Sum of Digits of a Number
def get_sum_of_digits(num):
    sum=0
    for i in str(num):
        sum+=int(i)
    return sum

#Find The Duplicated Number in a Consecutive Unsorted List
def find_dup(arr):
    a=set()
    for num in arr:
        if num in a:
            return num
        a.add(num)

#Caffeine Script
def caffeine_buzz(n):
    if n%12==0:
        return "CoffeeScript"
    elif n%6==0:
        return "JavaScript"
    elif n%3==0:
        return "Java"
    return "mocha_missing!"

#Product Of Maximums Of Array (Array Series #2)
def max_product(lst, n_largest_elements):
    new_arr=sorted(lst, reverse=True)[:n_largest_elements]
    res = 1
    for i in new_arr:
        res*=i
    return res

#Disarium Number (Special Numbers Series #3)
def disarium_number(number):
    a=str(number)
    b=len(a)
    disarium_sum = sum(int(a[i]) ** (i + 1) for i in range(b))
    if disarium_sum==number:
        return "Disarium !!"
    else:
        return "Not !!"

#6kyu
#IP Validation
def is_valid_IP(strng):
    ip=strng.split(".")
    for i in ip:
        if i.isdigit()==False or len(ip)!=4:
            return False
        if i.startswith("0") and len(i)>1 or int(i)>255:
            return False
    return True

#CamelCase Method
def camel_case(s):
    s=s.split(" ")
    cap=[word.capitalize() for word in s]
    ans=""
    for word in cap:
        ans+=word
    return ans

#WeIrD StRiNg CaSe
def to_weird_case(words):
    lst=words.split(" ")
    res=[]
    for word in lst:
        modified=""
        for i in range(len(word)):
            if i%2==0:
                modified+=word[i].upper()
            else:
                modified+=word[i].lower()
        res.append(modified)
    return " ".join(res)

#Sums of Parts
def parts_sums(ls):
    total=sum(ls)
    partial=[total]
    for num in ls:
        total-=num
        partial.append(total)
    return partial

#Array.diff
def array_diff(a, b):
    for i in b:
        if i in a:
            for x in range(a.count(i)):
                a.remove(i)
    return a

#Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!
def sum_dig_pow(a, b): 
    numbers=[1,2,3,4,5,6,7,8,9,89,135,175,518,598,1306,1676,2427,2646798,12157692622039623539]
    new_arr=[]
    for i in range(a,b+1):
        if i in numbers:
            new_arr.append(i)
    return new_arr
#or
def sum_dig_pow(a, b):
    l = []
    for i in range(a,b+1):
        k = 0
        p = str(i)
        for j in range(len(p)):
            k += int(p[j]) ** (j+1)
        if k == i:
            l.append(i)
    return l

#The Vowel Code
vowels={
        "a": "1",
        "e": "2",
        "i": "3",
        "o": "4",
        "u": "5"
    }
def encode(st):
    for i in vowels:
        st=st.replace(i, vowels[i])
    return st
    
def decode(st):
    for key, value in vowels.items():
        st=st.replace(value, key)
    return st

#Length of missing array
def get_length_of_missing_array(array_of_arrays):
    if not array_of_arrays or any(not arr for arr in array_of_arrays):
        return 0
    sorted_arrays = sorted(array_of_arrays, key=len)
    for i in range(len(sorted_arrays) - 1):
        if len(sorted_arrays[i]) + 1 != len(sorted_arrays[i + 1]):
            return len(sorted_arrays[i]) + 1
    return len(sorted_arrays[-1]) + 1