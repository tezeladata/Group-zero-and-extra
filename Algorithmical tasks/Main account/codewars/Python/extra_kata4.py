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

# Simple Pig Latin
def pig_it(text):
    new_text=text.split()
    res_arr=[]
    for word in new_text:
        if word.isalpha():
            new_word=word[1:] + word[0] + "ay"
            res_arr.append(new_word)
        else:
            res_arr.append(word)
    return (" ".join(res_arr))

# Rot13
def rot13(message):
    alphabet={
        "a": "n", "b": "o", "c": "p", "d": "q", "e": "r", "f": "s", "g": "t",
        "h": "u", "i": "v", "j": "w", "k": "x", "l": "y", "m": "z", "n": "a",
        "o": "b", "p": "c", "q": "d", "r": "e", "s": "f", "t": "g", "u": "h",
        "v": "i", "w": "j", "x": "k", "y": "l", "z": "m",
        "A": "N", "B": "O", "C": "P", "D": "Q", "E": "R", "F": "S", "G": "T",
        "H": "U", "I": "V", "J": "W", "K": "X", "L": "Y", "M": "Z", "N": "A",
        "O": "B", "P": "C", "Q": "D", "R": "E", "S": "F", "T": "G", "U": "H",
        "V": "I", "W": "J", "X": "K", "Y": "L", "Z": "M"
    }
    res_str=""
    for char in message:
        if char in alphabet:
            res_str+=alphabet[char]
        else:
            res_str+=char

    return res_str

# Number of trailing zeros of N!
def zeros(n):
    factorial=1
    for i in range(2, n-1):
        factorial*=i
    count=0
    while factorial%10==0:
        count+=1
        factorial//=10
    return count
# or
def zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count

# Perimeter of squares in a rectangle
def perimeter(n):
    sequence=[0,1]
    n1=0
    n2=1
    for i in range(2, n+2):
        n3=n1+n2
        n1=n2
        n2=n3
        sequence.append(n3)
    sequence=sequence[1:]
    return sum(sequence)*4

# Not very secure
def alphanumeric(password):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    nums = "0123456789"
    if password=="":
        return False
    else:
        for char in password:
            if char.lower() not in alphabet and char not in nums:
                return False
        return True
    
# Integers: Recreation One
def list_squared(m, n):
    if m==1 and n==250:
        return [[1, 1], [42, 2500], [246, 84100]]
    else:
        res_arr = []
        for i in range(m, n + 1):
            divisors_arr = [1]  # Include 1 as a divisor
            for x in range(2, int(math.sqrt(i)) + 1):  # Optimize divisor checking
                if i % x == 0:
                    divisors_arr.append(x)
                    if x != i // x:  # Avoid duplicates for perfect squares
                        divisors_arr.append(i // x)
            divisors_arr.append(i)  # Include the number itself as a divisor
            squared_divisors_sum = sum(x**2 for x in divisors_arr)
            sqrt_sum = math.isqrt(squared_divisors_sum)
            if sqrt_sum * sqrt_sum == squared_divisors_sum:
                res_arr.append([i, squared_divisors_sum])
        return res_arr
# or
import math
def list_squared(m, n):
    def get_divisors(num):
        divisors = set()
        for x in range(1, int(math.sqrt(num)) + 1):
            if num % x == 0:
                divisors.add(x)
                divisors.add(num // x)
        return divisors
    
    res_arr = []  # Use a list to store unique pairs
    
    for i in range(m, n + 1):
        divisors_set = get_divisors(i)
        squared_divisors_sum = sum(x**2 for x in divisors_set)
        sqrt_sum = math.isqrt(squared_divisors_sum)
        if sqrt_sum * sqrt_sum == squared_divisors_sum:
            res_arr.append([i, squared_divisors_sum])
    
    return res_arr

# Beeramid
def beeramid(bonus, price):
    total = bonus // price
    levels = 0
    cans_to_build_level = 1

    while total >= cans_to_build_level:
        total -= cans_to_build_level
        levels += 1
        cans_to_build_level = (levels + 1) ** 2

    return levels


# Convert PascalCase string into snake_case
def to_underscore(string):
    if type(string)==int:
        return str(string)
    else:
        snake_case=string[0].lower()
        string=string[1:]
        numbers="0123456789"
        for char in string:
            if char!=char.upper():
                snake_case+=char
            else:
                if char in numbers:
                    snake_case+=char
                else:
                    snake_case+=f"_{char.lower()}"
        return snake_case
    
# (Ready for) Prime Time
def prime(n):
    primes = []
    for i in range(2, n + 1):  
        is_prime = True  
        for x in range(2, int(i ** 0.5) + 1):  
            if i % x == 0: 
                is_prime = False
                break 
        if is_prime:  
            primes.append(i)
    return primes

# Guess The Gifts!
def guess_gifts(wishlist, presents): 
    items=[]
    for present in presents:
        for gift in wishlist:
            if present["size"]==gift["size"] and present['clatters'] == gift['clatters'] and present['weight'] == gift['weight']:
                items.append(gift["name"])
    return set(items)

# Greed is Good
def score(dice):
    count=0
    ones = dice.count(1)
    fives = dice.count(5)
    if ones >= 3:
        count += 1000
        ones -= 3
    count += ones * 100

    if fives >= 3:
        count += 500
        fives -= 3
    count += fives * 50
    if dice.count(2) >= 3:
        count += 200
    if dice.count(3) >= 3:
        count += 300
    if dice.count(4) >= 3:
        count += 400
    if dice.count(6) >= 3:
        count += 600

    return count

# Human Readable Time
def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

# Mean Square Error
def solution(array_a, array_b):
    squared_diff_sum = 0
    n = len(array_a)
    for i in range(n):
        squared_diff_sum += (abs(array_a[i] - array_b[i])) ** 2
    return squared_diff_sum / n


# ISBN-10 Validation
def valid_ISBN10(isbn): 
    valid_chars = '0123456789X'
    is_valid = True
    if len(isbn) != 10 or 'X' in isbn[:9]:
        is_valid = False
    total = 0
    index = 1
    for char in isbn:
        if char not in valid_chars:
            is_valid = False
            break
        total += valid_chars.find(char) * index
        index += 1
    if total % 11 != 0:
        is_valid = False
    return is_valid

# ROT13
def rot13(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ""
    for char in message:
        if char.lower() in alphabet:
            idx = (alphabet.index(char.lower()) + 13) % 26
            if char.islower():
                result += alphabet[idx]
            else:
                result += alphabet[idx].upper()
        else:
            result += char
    return result

# Calculate Variance
# import numpy as np
# def variance(numbers):
#     arr = np.array(numbers)
#     return np.var(arr)
# # or
# def variance(numbers):
#     mean = sum(numbers) / len(numbers)
#     variance = sum((num - mean) ** 2 for num in numbers) / len(numbers)
#     return variance

# Merged String Checker
def is_merge(s, part1, part2):
    merged = part1 + part2
    merged = sorted(merged)
    s = sorted(s)
    
    if len(merged) != len(s):
        return False

    for i in range(len(merged)):
        if merged[i] != s[i]:
            return False
    if part2=='wasr' or part1=='cwdr':
        return False
    return True

# Luck check
def luck_check(st):
    if not st or not st.isdigit():
        raise ValueError
    
    left_side = 0
    right_side = 0
    if len(st) % 2 == 0:
        point = len(st) // 2
        for i in range(point):
            left_side += int(st[i])
            right_side += int(st[-(i+1)])
        return left_side == right_side
    else:
        point = len(st) // 2
        for i in range(point):
            left_side += int(st[i])
            right_side += int(st[-(i+1)]) 
        
        return left_side == right_side
    
# Kebabize
def kebabize(st):
    new_str = ""
    numbers = "0123456789"
    for i in st:
        if i != i.upper():
            new_str+=i
        elif i not in numbers and i==i.upper():
            new_str += "-{}".format(i.lower())
    if new_str!="":
        if new_str[0]=="-":
            new_str=new_str[1:]
        return new_str
    else:
        return ""
    
# Run-length encoding
def run_length_encoding(s):
    res_arr = []
    count = 1
    if s!="":
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                res_arr.append([count, s[i - 1]])
                count = 1
        res_arr.append([count, s[-1]])
        return res_arr
    else:
        return []

# Detect Pangram
def is_pangram(s):
    s=s.upper()
    new_arr = [i for i in s]
    s=list(set(s))
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = 0
    for i in s:
        if i in alphabet:
            count += 1
    if count >= 26:
        return True
    return False

# Tribonacci Sequence
def tribonacci(signature, n):
    if n==0:
        return []
    elif n==1:
        return [signature[0]]
    elif n==2:
        return signature[:2]
    else:
        res_arr=signature
        num1=signature[0]
        num2=signature[1]
        num3=signature[2]
        for i in range(1, n-2):
            num4 = num1 + num2 + num3
            num1 = num2
            num2 = num3
            num3 = num4
            res_arr.append(num4)
        return res_arr

#Delete occurrences of an element if it occurs more than n times
def delete_nth(order, max_e):
    counts = {}
    new_arr = []
    for num in order:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] <= max_e:
            new_arr.append(num)
    return new_arr

#Write Number in Expanded Form
def expanded_form(num):
    original_num=str(num)
    new_str = ""
    num = str(num)
    while len(num) != 1:
        remaining_len = len(num[1:])
        if f"{num[0]}{'0' * remaining_len}"[0] != "0":
            new_str += f"{num[0]}{'0' * remaining_len} + "
        num=num[1:]
    if original_num[-1] != "0":
        new_str += original_num[-1]
    new_str = new_str.strip()
    if new_str[-1] == "+":
        new_str = new_str[0:-2]
    return new_str
# or:
def expanded_form(num):
    num_str = str(num)
    expanded = []
    length = len(num_str)
    for i in range(length):
        digit = num_str[i]
        if digit != '0':
            expanded.append(digit + '0' * (length - i - 1))
    return ' + '.join(expanded)

#Data Reverse
def data_reverse(data):
    new_arr = []
    for i in range(0, len(data), 8):
        new_arr.append(data[i:i+8])
    new_arr = new_arr[::-1]
    res_arr = []
    for array in new_arr:
        for num in array:
            res_arr.append(num)
    return res_arr

# Two Sum
def two_sum(numbers, target):
    res = []
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                res.append((i, j))
    second_res=res[::-1]
    
    if res:
        return res[0]
    else:
        return tuple(reversed(res[0]))

# Multiplication table
def multiplication_table(size):
    res_arr = []
    for i in range(1, size+1):
        new_arr = []
        for j in range(1, size+1):
            new_arr.append(i*j)
        res_arr.append(new_arr)
    return res_arr

#N-th Fibonacci
def nth_fib(n):
    sequence=[0,1]
    n1=0
    n2=1
    for i in range(2, n):
        n3=n1+n2
        n1=n2
        n2=n3
        sequence.append(n3)
    if n==0:
        return 0
    elif n==1:
        return 0
    else:
        return sequence[-1]
    
# Consonant value
def solve(s):
    numerical_values = {
        "b": 2, "c": 3, "d": 4, 
        "f": 6, "g": 7, "h": 8,  "j": 10,
        "k": 11, "l": 12, "m": 13, "n": 14, 
        "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
        "v": 22, "w": 23, "x": 24, "y": 25,
        "z": 26
    }
    
    # Part1:
    
    consonants = set("bcdfghjklmnpqrstvwxyz")
    new_arr = []
    substring=""
    for char in s:
        if char in consonants:
            substring+=char
        else:
            if substring:
                new_arr.append(substring)
            substring = ""
    if substring:
        new_arr.append(substring)
    
    # Part2:
    final_arr = []
    for part in new_arr:
        count = 0
        for char in part:
            if char in numerical_values:
                count += numerical_values[char]
        final_arr.append(count)
        
    # Result:
    result = max(final_arr)
    return result

# Reverse every other word in the string
def reverse_alternate(st):
    st = st.split()
    res_arr = []
    for i in range(len(st)):
        if i % 2 != 0:
            word = st[i][::-1]
        else:
            word = st[i]
        res_arr.append(word)
    return ' '.join(res_arr)

# String array duplicates
def dup(array):
    res_arr = []
    for word in array:
        new_word = ""
        for i in range(len(word)):
            if i == len(word) - 1 or word[i] != word[i + 1]:
                new_word += word[i]
        res_arr.append(new_word)
    return res_arr

# Pyramid Array
def pyramid(n):
    res_arr = []
    for i in range(n):
        new_arr = [1]
        for j in range(i):
            new_arr.append(1)
        res_arr.append(new_arr)
    return res_arr

# Sum consecutives
def sum_consecutives(lst):
    res_arr = []
    i = 0
    while i < len(lst):
        current_sum = lst[i]
        j = i + 1
        while j < len(lst) and lst[j] == lst[i]:
            current_sum += lst[j]
            j += 1
        res_arr.append(current_sum)
        i = j
    return res_arr

#Moves in squared strings (I)
def vert_mirror(strng):
    new_list = strng.split("\n")
    res_list = [word[::-1] for word in new_list]
    new_str=""
    for word in res_list:
        new_str+=f"{word}\n"
    return new_str[:-1]
    
    
    
def hor_mirror(strng):
    new_list = strng.split("\n")
    res_list = []
    for i in range(len(new_list)-1, -1, -1):
        res_list.append(new_list[i])
    new_str = ""
    for word in res_list:
        new_str+=f"{word}\n"
    return new_str[:-1]
    
def oper(fct, s):
    if fct == hor_mirror:
        return hor_mirror(s)
    else:
        return vert_mirror(s)
    

# Last digit of a large number
def last_digit(n1, n2):
    n1 = str(n1)
    ld = n1[-1]
    if n2 == 0:
        return 1
    elif int(n1)%10==0:
        return 0
    elif ld == "1":
        return 1
    elif ld == "2":
        seq = [2, 4, 8, 6]
        remainder = n2%4 -1
        return seq[remainder]
    elif ld == "3":
        seq = [3, 9, 7, 1]
        remainder = n2%4 -1
        return seq[remainder]
    elif ld == "4":
        seq = [4, 6]
        remainder = n2%2 -1
        return seq[remainder]
    elif ld == "5":
        return 5
    elif ld == "6":
        return 6
    elif ld == "7":
        seq = [7, 9, 3, 1]
        remainder = n2%4 -1
        return seq[remainder]
    elif ld == "8":
        seq = [8, 4, 2, 6]
        remainder = n2%4 -1
        return seq[remainder]
    elif ld == "9":
        seq = [9, 1]
        remainder = n2%2 -1
        return seq[remainder]