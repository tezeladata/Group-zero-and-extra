# Difference of 2
def twos_difference(list): 
    res = []
    
    list.sort()
    for i in range(len(list)-1):
        for x in range(i+1, len(list)):
            if list[i] +2 == list[x]:
                res.append((list[i], list[x]))
                
    return res
# or:
def twos_difference(lst):
    lst.sort()
    return [(lst[i], lst[j]) for i in range(len(lst)) for j in range(i + 1, len(lst)) if lst[j] - lst[i] == 2]

# Find the Mine!
def mine_location(field):
    res = [[field.index(arr), arr.index(1)] for arr in field if 1 in arr]
    return [res[0][0], res[0][1]]

# Transform To Prime
def minimum_number(numbers):
    return sorted([i for i in range(sum(numbers), sum(numbers) + 35) if is_prime(i)])[0] - sum(numbers)
    
def is_prime(val):
    is_prime = True
    
    for i in range(2, int(val**0.5) + 1):
        if val % i == 0:
            is_prime = False
    
    return is_prime

# Moves in squared strings (II)
def rot(string):
    words = string.replace("\n", " ").split()
    reversed_words = [word[::-1] for word in words]
    return "\n".join(reversed(reversed_words))
    
    return string

def selfie_and_rot(string):
    words = string.replace("\n", " ").split()
    selfie = "\n".join([word + "." * len(word) for word in words])
    
    rotated_words = rot(string).split("\n")
    selfie_rotated = "\n".join(["." * len(word) + word for word in rotated_words])
    
    return selfie + "\n" + selfie_rotated
    
def oper(fct, s):
    return fct(s)
# or:
def rot(string):
    return "\n".join(reversed([word[::-1] for word in string.replace("\n", " ").split()]))

def selfie_and_rot(string):
    return "\n".join([word + "." * len(word) for word in string.replace("\n", " ").split()]) + "\n" + "\n".join(["." * len(word) + word for word in rot(string).split("\n")])
    
def oper(fct, s):
    return fct(s)
# or:
def rot(string):
    return string[::-1]

def selfie_and_rot(string):
    return "\n".join([word + "." * len(word) for word in string.replace("\n", " ").split()]) + "\n" + "\n".join(["." * len(word) + word for word in rot(string).split("\n")])
    
def oper(fct, s):
    return fct(s)

# Hamming Distance
def hamming(a,b):
    return len([1 for i in range(len(a)) if a[i] != b[i]])

# All Star Code Challenge #15
def rotate(s):
    if not s:
        return []
    
    res = []
    length = len(s)
    
    for i in range(length):
        rotated = s[i:] + s[:i]
        res.append(rotated)
        
    return res[1:] + [res[0]]

# How many pages in a book?
def amount_of_pages(summary):
    res = ""
    
    original = 1
    while len(res) != summary:
        res += str(original)
        original += 1
        
    return original - 1

# Paginating a huge book
def page_digits(pages):
    digits = 0
    length = len(str(pages))
    
    for i in range(1, length):
        digits += i * 9 * 10**(i-1)
    
    digits += length * (pages - 10**(length-1) + 1)
    
    return digits

# Throwing Darts
def score_throws(radii):
    if radii == []:
        return 0
    
    plus_points = True
    for i in radii:
        if i >= 5:
            plus_points = False
            
    res = 0
    if plus_points:
        res += 100
        
    for i in radii:
        if i >= 5 and i <= 10:
            res += 5
        elif i < 5:
            res += 10
            
    return res

# String average
def average_string(s):
    # Dictionary mapping string numbers to their integer values
    res = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4, 
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    for word in s.split(" "):
        if word not in res:
            return "n/a"
    
    avg = sum(res[word] for word in s.split(" ")) // len(s.split(" "))
    
    for key, value in res.items():
        if value == avg:
            return key
        
# Tank Truck
import math

def tankvol(h, d, vt):
    r = d / 2
    l = vt / (math.pi * r**2)
    
    segment_area1 = (r**2) * math.acos((r - h) / r)
    segment_area2 = (r - h) * math.sqrt((2 * r * h) - h**2)
    final_area = segment_area1 - segment_area2
    
    volume = final_area * l
    
    return int(volume)

# Weight for weight
def order_weight(strng):
    if not strng.strip():
        return ""

    def weight_and_value(num):
        weight = sum(int(digit) for digit in num)
        return (weight, num)

    numbers = strng.strip().split()
    sorted_numbers = sorted(numbers, key=weight_and_value)

    return ' '.join(sorted_numbers)

# Product of consecutive Fib numbers
def product_fib(prod):
    res = [0, 1]
    
    while res[-1] * res[-2] < prod:
        res.append(res[-1] + res[-2])
        
    if res[-1] * res[-2] == prod: return [res[-2], res[-1], True]
    return [res[-2], res[-1], False]

# Scramblies
def scramble(s1, s2):
    if len(s2) > len(s1): return False 
    
    res1, res2 = {i: s1.count(i) for i in set(s1)}, {i: s2.count(i) for i in set(s2)}
    
    for char, count in res2.items():
        if char not in res1 or res1[char] < count: return False
    
    return True

# Primes in numbers
from math import floor

def prime_factors(n):
    result = []
    for i in range(2,n+1):
        s = 0;
        while n/i == floor(n/float(i)): # if n/i an integer
            n = n/float(i)
            s += 1
        if s > 0:
            for k in range(s):
                result.append(i)
            if n == 1:          
                res_str = ""
                for num in sorted(list(set(result))):
                    if result.count(num) > 1:
                        res_str += f"({num}**{result.count(num)})"
                    else:
                        res_str += f"({num})"
                
                return res_str
            
# Pick peaks
def pick_peaks(arr):
    pos = []
    peaks = []
    peak_candidate = None

    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1]:
            peak_candidate = i
        elif arr[i] < arr[i - 1] and peak_candidate is not None:
            pos.append(peak_candidate)
            peaks.append(arr[peak_candidate])
            peak_candidate = None

    if peak_candidate is not None and arr[-1] < arr[peak_candidate]:
        pos.append(peak_candidate)
        peaks.append(arr[peak_candidate])

    return {'pos': pos, 'peaks': peaks}

# Count IP Addresses
def ips_between(start, end):
    start, end = [int(i) for i in start.split(".")], [int(i) for i in end.split(".")]
    
    total = 0
    for i in range(4):
        total += (end[i] - start[i]) * (256 ** (3 - i))
    
    return total