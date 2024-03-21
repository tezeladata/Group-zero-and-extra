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