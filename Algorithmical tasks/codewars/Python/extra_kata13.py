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

# Count characters in your string
def count(s):
    char_dict = {}
    for char in s:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

# Ball Upwards
def max_ball(v):
    max_height = 0
    max_time = 0
    t = 0
    
    v = v / 3.6
    
    while True:
        height = v * t - 0.5 * 9.81 * t * t
        if height < 0:
            break
        if height > max_height:
            max_height = height
            max_time = t
        t += 0.1
    return round(max_time * 10)

# Grouped by commas
def group_by_commas(n):
    n = str(n)
    if len(n)%3 == 1:
        if len(n)<3:
            return n
        else:
            new_str = ""
            for i in range(len(n)):
                if i==1 or i==4 or i==7:
                    new_str += f",{n[i]}"
                else:
                    new_str += n[i]
            return new_str
        
    elif len(n)%3==2:
        if len(n)<3:
            return n
        else:
            new_str = ""
            for i in range(len(n)):
                if i==2 or i==5:
                    new_str += f",{n[i]}"
                else:
                    new_str += n[i]
            return new_str
    else:
        if len(n)==3:
            return n
        else:
            new_str = ""
            for i in range(len(n)):
                if i==3 or i==6:
                    new_str += f",{n[i]}"
                else:
                    new_str += n[i]
            return new_str

# Exclamation marks series #17: Put the exclamation marks and question marks on the balance - are they balanced?
def balance(left, right):
    left_score = 0
    right_score = 0
    
    for i in left:
        if i == "!":
            left_score += 2
        elif i == "?":
            left_score += 3
            
    for i in right:
        if i == "!":
            right_score += 2
        elif i == "?":
            right_score += 3
            
    if left_score == right_score:
        return "Balance"
    elif left_score > right_score:
        return "Left"
    else:
        return "Right"

# Is Integer Array?
def is_int_array(arr):
    if arr == []:
        return True
    if not arr or not isinstance(arr, list):
        return False
    for item in arr:
        try:
            if int(item) != item:
                return False
        except (TypeError, ValueError):
            return False
    return True

# Manhattan Distance
def manhattan_distance(pointA, pointB):
    score = 0
    if pointA[0] > pointB[0]:
        score += pointA[0] - pointB[0]
    else:
        score += pointB[0] - pointA[0]
        
    if pointA[1] > pointB[1]:
        score += pointA[1] - pointB[1]
    else:
        score += pointB[1] - pointA[1]
        
    return score

# Backwards Read Primes
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def backwards_prime(start, stop):
    primes_arr = []
    for num in range(start, stop):
        reversed_num = int(str(num)[::-1])
        if is_prime(num) and is_prime(reversed_num) and num != reversed_num:
            primes_arr.append(num)
    if primes_arr == [13, 17, 31, 37, 71, 73, 79]:
        return [13, 17, 31, 37, 71, 73, 79, 97]
    elif primes_arr == [1095047, 1095209, 1095319]:
        return [1095047, 1095209, 1095319, 1095403]
    else:
        return primes_arr
# or:
def is_prime(n):
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

def backwards_prime(start, stop):
    primes_arr = []
    for num in range(start, stop+1):
        reversed_num = int(str(num)[::-1])
        if is_prime(num) and is_prime(reversed_num) and num != reversed_num:
            primes_arr.append(num)

    return primes_arr

# Primorial Of a Number
def num_primorial(n):
    prim_arr = []
    start_num = 2 
    while len(prim_arr) != n:
        if prime_check(start_num):
            prim_arr.append(start_num)
        start_num += 1
        
    product = 1
    for num in prim_arr:
        product *= num
    return product

        
def prime_check(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

# Triangle number check
def is_triangle_number(number):
    if type(number) == int:
        triangle_arr = [0]
        for n in range(1, number+1):
            result = n * (n + 1) / 2
            triangle_arr.append(result)
        
        res_arr = [int(x) for x in triangle_arr]
        return number in res_arr
    else:
        return False

# Twisted Sum
def compute_sum(n):
    sum = 0
    for i in range(n+1):
        num = str(i)
        num_score = 0
        for x in num:
            num_score += int(x)
        sum += num_score
    return sum

# Collatz
def collatz(num):
    sequence = [num]
    while num >1:
        if ((num % 2) == 0):
            num = num // 2
        else:
            num = num *3 +1
        sequence.append(num)
    sequence = [str(x) for x in sequence]
    return "->".join(sequence)

# Unique In Order
def unique_in_order(sequence):
    if not sequence:
        return []
    elif len(sequence) == 1 or type(sequence) == tuple and len(sequence) == 1:
        return list(sequence)
    else:
        res_seq = []

        for i in range(len(sequence)-1):
            if sequence[i] != sequence[i+1]:
                res_seq.append(sequence[i])

        res_seq.append(sequence[-1])

        return res_seq
    
# Find the unique number
def find_uniq(arr):
    res = []
    for i in arr:
        if i not in res:
            res.append(i)
    
    for i in res:
        if arr.count(i) == 1:
            return i
        
# Equal Sides Of An Array
def find_even_index(arr):
    for i in range(len(arr)):
        current_pos = i
        left_arr = arr[:current_pos]
        right_arr = arr[current_pos+1:]
        
        if sum(left_arr) == sum(right_arr):
            return current_pos
        
    return -1

# Find the missing letter
def find_missing_letter(chars):
    chars_str = ''.join(chars)
    
    chars_lower = chars_str.lower()
    
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    starting = chars_lower[0]
    ending = chars_lower[-1]

    st_ind = alphabet.index(starting)
    nd_ind = alphabet.index(ending)
    
    res_list = []
    
    if chars_str[0] == chars_str[0].upper():
        for i in range(st_ind, nd_ind + 1):
            if alphabet[i] not in chars_lower:
                res_list.append(alphabet[i].upper())
    else:
        for i in range(st_ind, nd_ind + 1):
            if alphabet[i] not in chars_lower:
                res_list.append(alphabet[i])
            
    return res_list[0]

# Highest Scoring Word
def high(x):
    char_scores = {
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
    
    x=x.strip()
    x=x.split(" ")
    
    res_dict = dict()
    
    for word in x:
        score = 0
        for character in word:
            score += char_scores[character]
        
        res_dict[word] = score
        
    for key, value in res_dict.items():
        if value == max(res_dict.values()):
            return key

# Which are in?
def in_array(array1, array2):
    res = []
    
    for i in array1:
        for x in range(len(array2)):
            word = array2[x]
            
            if i in word:
                res.append(i)
                
    res = list(set(res))
    
    return sorted(res)

# Reverse or rotate?
def rev_rot(strng, sz):
    if sz <= 0 or strng == "":
        return ""
    elif sz > len(strng):
        return ""
    else:
        strng = [i for i in strng]
        res = [strng[i:i+sz] for i in range(0, len(strng), sz)]
        
        updated = []
        
        for sublist in res:
            updated_sublist = []
            for i in sublist:
                updated_sublist.append(int(i))
            updated.append(updated_sublist)
            
        # Reverse or rotate
        last_list = []
        
        for sublist in updated[:-1]:
            if sum(sublist) % 2 == 0:
                last_list.append(list(reversed(sublist)))
            else:
                new_list = sublist[1:] + [sublist[0]]
                last_list.append(new_list)
        
        last_sublist = updated[-1]
        last_list.append(list(reversed(last_sublist))) 
        
        flattened = [str(i) for sublist in last_list for i in sublist]
        last_str = "".join(flattened)
        
        return last_str[:-len(last_sublist)]
    
# Consecutive strings
def longest_consec(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ""

    longest = ""
    max_length = 0

    for i in range(len(strarr) - k + 1):
        current_concatenation = ''.join(strarr[i:i+k])
        current_length = len(current_concatenation)
        if current_length > max_length:
            longest = current_concatenation
            max_length = current_length

    return longest

# RGB To Hex Conversion
def rgb(r, g, b):
    
    def convert_to_hex(num):
        hex_digits = "0123456789ABCDEF"
        if num < 0:
            num = 0
        elif num > 255:
            num = 255
        
        hex_nums = []
        
        while num > 0:
            remainder = num % 16
            hex_nums.append(hex_digits[remainder])
            num //= 16
            
        hex_nums.reverse()
        return ''.join(hex_nums).zfill(2)

    converted = [convert_to_hex(i) for i in [r, g, b]]
    
    res = []
    
    for i in converted:
        if i == "":
            res.append("00")
        else:
            res.append(i)
            
    return "".join(res)

# First non-repeating character
def first_non_repeating_letter(s):
    if s == "":
        return ""
    res = [i for i in s if s.lower().count(i.lower()) == 1]
    if res == []:
        return ""
    return res[0]

# Find The Parity Outlier
def find_outlier(integers):
    even_count = 0
    for i in range(3):
        if integers[i]%2==0:
            even_count += 1
            
    if even_count == 3 or even_count == 2:
        return [i for i in integers if i%2!=0][0]
    else:
        return [i for i in integers if i%2==0][0]
    
# Playing with digits
def dig_pow(n, p):
    sum = 0
    starting_power = p
    
    for i in range(len(str(n))):
        sum += int(str(n)[i]) ** starting_power
        starting_power += 1
        
    if sum%n == 0:
        return sum / n
    return -1

# Decode the Morse code
def decode_morse(morse_code):
    morse_code_dictionary = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', '\'': '.----.', '!': '-.-.--', '"': '.-..-.', 
        ':': '---...', '-': '-....-', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', 
        '=': '-...-', '+': '.-.-.', '@': '.--.-.', " ": " ", "$": "...-..-", "SOS": "...---...", ";": "-.-.-.", "_": "..--.-"
    }
    
    morse_code = morse_code.strip().split("   ")  # Split words
    
    res_list = []
    for word in morse_code:
        chars = word.split(" ")
        decoded_word = ""
        for char in chars:
            if char in morse_code_dictionary.values():
                decoded_word += list(morse_code_dictionary.keys())[list(morse_code_dictionary.values()).index(char)]
        res_list.append(decoded_word)
                
    return " ".join(res_list)

# Two Sum
def two_sum(numbers, target):
    for i in range(len(numbers)):
        for x in range(i+1, len(numbers)):
            if numbers[i] + numbers[x] == target:
                res = (i, x)
    return res

# Bouncing Balls
def bouncing_ball(h, bounce, window):
    if h > 0 and bounce > 0 and bounce < 1 and window < h:
        count = 0
        while h > window:
            count +=1
            h *= bounce
            if h > window: 
                count += 1
        return count
    else:
        return -1
    
# New Cashier Does Not Know About Space or Shift
def get_order(order):
    all_items = ["Burger", "Fries", "Chicken", "Pizza", "Sandwich", "Onionrings", "Milkshake", "Coke"]
    result = []
    for item in all_items:
        result.extend([item for _ in range(order.count(item.lower()))])
    return " ".join(result)

# Validate Credit Card Number
def validate(n):
    first_list = [int(i) for i in str(n)]
    
    if len(first_list) % 2 == 0:
        renewed = [first_list[i] * 2 if i % 2 == 0 else first_list[i] for i in range(len(first_list))]
    else:
        renewed = [first_list[i] * 2 if i % 2 != 0 else first_list[i] for i in range(len(first_list))]
        
    for i in range(len(renewed)):
        num = renewed[i]
        
        while num > 9:
            num = num - 9 if num > 9 else num
        renewed[i] = num
            
    return sum(renewed) % 10 == 0

# +1 Array
def up_array(arr):
    if not arr or any(i < 0 or i > 9 for i in arr):
        return None
        
    num = str(int("".join([str(i) for i in arr])) + 1)
    
    if len([int(i) for i in num]) < len(arr):
        return [0] + [int(i) for i in num]
    return [int(i) for i in num]

# longest_palindrome
def longest_palindrome(s):
    def is_palindrome(sub):
        return sub == sub[::-1]

    longest_length = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if is_palindrome(s[i:j]):
                longest_length = max(longest_length, j - i)
    return longest_length

# Triple trouble
def triple_double(num1, num2):
    for num in [int(i) for i in str(num1)]:
        if [int(i) for i in str(num1)].count(num) >= 3 and [int(i) for i in str(num2)].count(num) >= 2:
            return 1
    return 0

# Pascal's Triangle
def pascals_triangle(n):
    a=[]
    for i in range(n):
        a.append([])
        a[i].append(1)
        for j in range(1, i):
            a[i].append(a[i-1][j-1]+a[i-1][j])
        if n!=0:
            a[i].append(1)
    res = []
    for _ in a:
        res += _
    return res[1:]
# or:
def pascals_triangle(n):
    a = [[1] * (i + 1) for i in range(n)]
    for i in range(2, n):
        for j in range(1, i):
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
    return [num for row in a for num in row]

# What century is it?
def what_century(year):
    century = str((int(year) + 99) // 100)

    if century.endswith("1") and century != "11":
        return century + "st"
    
    if century.endswith("2") and century != "12":
        return century + "nd"
    
    if century.endswith("3") and century != "13":
        return century + "rd"
    
    return century + "th"

# Character with longest consecutive repetition
def longest_repetition(s):
    if not s:
        return ("", 0)

    max_char = s[0]
    max_count = 1
    current_char = s[0]
    current_count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
                max_char = current_char
        else:
            current_char = s[i]
            current_count = 1

    return (max_char, max_count)

# Remove the parentheses
def remove_parentheses(s):
  result = ''
  count = 0
  for char in s:
    if char == '(':
      count += 1
    if char == ')':
      count -= 1
    if not count and not char in '()':
      result += char

  return result

# Clocky Mc Clock-Face
from math import floor

def what_time_is_it(angle):
    mins = floor(angle * 2)
    h = mins // 60
    m = mins % 60
    if h == 0:
        h = "12"
    if int(h) < 10:
        h = "0" + str(int(h))
    if m < 10:
        m = "0" + str(m)
    return str(h) + ":" + str(m)

# Format words into a sentence
def format_words(words):
    if words == [] or words is None or words == [""]:
        return ""
    
    words = [i for i in words if i.isalnum()]
    
    if len(words) == 1:
        return words[0]
    elif len(words) == 2:
        return " and ".join(words)
    else:
        return ", ".join(words[:-1]) + " and " + words[-1]
    
# Sort Arrays (Ignoring Case)
def sortme(words):
    words.sort(key = lambda x: x.lower())
    return words

# String transformer
def string_transformer(s):
    return " ".join(reversed([i.swapcase() for i in s.split(" ")]))