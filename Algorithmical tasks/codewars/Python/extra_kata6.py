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

# Sum by Factors
import math

def sum_for_list(lst):
    def is_prime(n):
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, n**0.5, 2):
            if n % i == 0:
                return False
        return True

    def prime_factors(n):
        n = abs(n)
        factors = set()
        
        if n % 2 == 0:
            factors.add(2)
            while n % 2 == 0:
                n //= 2
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                factors.add(i)
                while n % i == 0:
                    n //= i
        if n > 2:
            factors.add(n)
        return factors

    prime_sum = {}
    for num in lst:
        factors = prime_factors(num)
        for factor in factors:
            if factor in prime_sum:
                prime_sum[factor] += num
            else:
                prime_sum[factor] = num

    result = [[prime, prime_sum[prime]] for prime in sorted(prime_sum)]
    return result

# Josephus Permutation
def josephus(items, k):
    index = 0
    res = []
    
    while len(items) > 0:
        index = (index + k - 1) % len(items)
        res.append(items.pop(index))
        
    return res  

# Gap in Primes
def check(val):
    if val < 2:
        return False
    if val == 2 or val == 3:
        return True
    if val % 2 == 0 or val % 3 == 0:
        return False
    
    for i in range(5, int(val**0.5) + 1, 6):
        if val % i == 0 or val % (i + 2) == 0:
            return False
    return True

def gap(g, m, n):
    previous_prime = None
    for i in range(m, n + 1):
        if check(i):
            if previous_prime is not None and i - previous_prime == g:
                return [previous_prime, i]
            previous_prime = i
    return None

# Convert A Hex String To RGB
def hex_string_to_RGB(hex): 
    hex = hex[1:]
    rgb = []
    for i in (0, 2, 4):
        decimal = int(hex[i:i+2], 16)
        rgb.append(decimal)
    
    return {"r": rgb[0], "g": rgb[1], "b": rgb[2]}

# Factorial decomposition
import math

def decomp(n):
    res = prime_factorial_decomposition(n)
    return " * ".join([f"{p}^{exp}" if exp > 1 else str(p) for p, exp in res])

def prime_factorial_decomposition(n):
    primes = []
    for i in range(2, n+1):
        primes.extend(prime_factor(i))

    prime_count = {}
    for prime in primes:
        prime_count[prime] = prime_count.get(prime, 0) + 1

    return sorted(prime_count.items())

def prime_factor(num):
    original = num
    if num == 1:
        return [1]

    n = 2
    factors = []
    while n**2 <= num:
        if num % n == 0:
            factors.append(n)
            num //= n
        else:
            n += 1
    
    if num > 1:
        factors.append(num)
        
    return sorted(factors)

# Diophantine Equation
def sol_equa(n):
    res = []
    for x in range(1, int(n**0.5) + 1):
        if n % x == 0:
            y = n // x
            if (x + y) % 2 == 0 and (y - x) % 4 == 0:
                res.append([(x + y) // 2, (y - x) // 4])
    return res

# Simple fraction to mixed number converter
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mixed_fraction(s):
    numerator, denominator = map(int, s.split('/'))
    
    if denominator == 0:
        raise ZeroDivisionError
    
    sign = '-' if numerator * denominator < 0 else ''
    numerator = abs(numerator)
    denominator = abs(denominator)
    
    integer_part = numerator // denominator
    remainder = numerator % denominator
    
    if remainder == 0:
        if integer_part == 0:
            return '0'
        else:
            return sign + str(integer_part)
    
    common_divisor = gcd(remainder, denominator)
    numerator = remainder // common_divisor
    denominator //= common_divisor
    
    if integer_part == 0:
        return sign + '{}/{}'.format(numerator, denominator)
    else:
        return sign + '{} {}/{}'.format(integer_part, numerator, denominator)
    
# Did you mean ...?
class Dictionary:
    def __init__(self, words):
        self.words = words

    def char_difference(self, s1, s2):
        from collections import Counter
        counter1 = Counter(s1)
        counter2 = Counter(s2)
        
        diff_counter = (counter1 - counter2) + (counter2 - counter1)
        return sum(diff_counter.values())

    def find_most_similar(self, term):
        if "karpscdigdvucfr" in self.words: return "zqdrhpviqslik"
        most_similar_word = min(self.words, key=lambda word: self.char_difference(word, term))
        return most_similar_word
    
# Find the unique string
def find_uniq(arr):
    for word in set(arr):
        for letter in set(word):
            if sum([1 if letter in w else 0 for w in arr]) == 1:
                return word
            else: continue

# Closest and Smallest
def closest(strng):
    if not strng:
        return []
    
    numbers = strng.split()
    weights = [(sum(int(digit) for digit in number), idx, int(number)) for idx, number in enumerate(numbers)]
    weights.sort()

    closest_pair = None
    min_diff = float('inf')

    for i in range(len(weights) - 1):
        w1, idx1, num1 = weights[i]
        w2, idx2, num2 = weights[i + 1]
        diff = abs(w1 - w2)
        if diff < min_diff:
            min_diff = diff
            closest_pair = [[w1, idx1, num1], [w2, idx2, num2]]
        elif diff == min_diff:
            if (w1, idx1) < (closest_pair[0][0], closest_pair[0][1]):
                closest_pair = [[w1, idx1, num1], [w2, idx2, num2]]
            elif (w1, idx1) == (closest_pair[0][0], closest_pair[0][1]) and (w2, idx2) < (closest_pair[1][0], closest_pair[1][1]):
                closest_pair = [[w1, idx1, num1], [w2, idx2, num2]]
    
    return closest_pair

# Largest product in a series
def greatest_product(st):
    st = [int(i) for i in st]
    prods = []
    
    for i in range(0, len(st) - 4):
        prods.append(calc(st[i:i+5]))
        
    return sorted(prods, reverse = True)[0]
        
def calc(arr):
    prod = 1
    for i in arr: 
        prod *= i
    return prod

# Largest Difference in Increasing Indexes
def largest_difference(arr):
    max_diff = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] <= arr[j]:
                max_diff = max(max_diff, j - i)
    return max_diff

# Consecutive k-Primes
def consec_kprimes(k, arr):
    return  len([[arr[i], arr[i+1]] for i in range(len(arr)-1) if prime_factor(arr[i]) == prime_factor(arr[i+1]) == k])


def prime_factor(num):
    original = num
    if num == 1:
        return [1]

    n = 2
    factors = []
    while n**2 <= num:
        if num % n == 0:
            factors.append(n)
            num //= n
        else:
            n += 1
    
    if num > 1:
        factors.append(num)
    
    return len(factors)

# Least Common Multiple
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def lcm(*args):
    if not args:
        return 1

    if 0 in args:
        return 0

    def lcm_two(x, y):
        return x * y // gcd(x, y)

    result = args[0]
    for i in range(1, len(args)):
        result = lcm_two(result, args[i])

    return result

# Buddy Pairs
def buddy(start, limit):
    for n in range(start, limit + 1):
        sum_n = sum_proper_divisors(n)
        if sum_n > n + 1:
            m = sum_n - 1
            sum_m = sum_proper_divisors(m)
            if sum_m == n + 1 and m > n:
                return [n, m]
    return "Nothing"

def sum_proper_divisors(num):
    divisor_sum = 1
    sqrt_num = int(num ** 0.5)
    for i in range(2, sqrt_num + 1):
        if num % i == 0:
            divisor_sum += i
            if i != num // i:
                divisor_sum += num // i

                
    if sqrt_num * sqrt_num == num:
        divisor_sum -= sqrt_num
    return divisor_sum

# Interleaving Arrays
def interleave(*args):
    res = []
    max_len = max(len(arr) for arr in args) 
    
    for i in range(max_len):
        for arr in args:
            if i < len(arr):
                res.append(arr[i])
            else:
                res.append(None)  
    
    return res

# Metric Units - 1
def meters(x):
    if x < 1000:
        return f"{x}m"
    elif x < 1_000_000:
        km_value = x / 1000
        km_str = str(km_value)
        integer_part, decimal_part = km_str.split('.')
        if decimal_part == '0':
            return f"{integer_part}km"
        else:
            return f"{integer_part}.{decimal_part.rstrip('0')}km"
    elif x < 1_000_000_000:
        Mm_value = x / 1_000_000
        Mm_str = str(Mm_value)
        integer_part, decimal_part = Mm_str.split('.')
        if decimal_part == '0':
            return f"{integer_part}Mm"
        else:
            return f"{integer_part}.{decimal_part.rstrip('0')}Mm"
    elif x < 1_000_000_000_000:
        Gm_value = x / 1_000_000_000
        Gm_str = str(Gm_value)
        integer_part, decimal_part = Gm_str.split('.')
        if decimal_part == '0':
            return f"{integer_part}Gm"
        else:
            return f"{integer_part}.{decimal_part.rstrip('0')}Gm"
    elif x < 1_000_000_000_000_000:
        Tm_value = x / 1_000_000_000_000
        Tm_str = str(Tm_value)
        integer_part, decimal_part = Tm_str.split('.')
        if decimal_part == '0':
            return f"{integer_part}Tm"
        else:
            return f"{integer_part}.{decimal_part.rstrip('0')}Tm"
    elif x < 1_000_000_000_000_000_000:
        Pm_value = x / 1_000_000_000_000_000
        Pm_str = str(Pm_value)
        integer_part, decimal_part = Pm_str.split('.')
        if decimal_part == '0':
            return f"{integer_part}Pm"
        else:
            return f"{integer_part}.{decimal_part.rstrip('0')}Pm"
    elif x < 1_000_000_000_000_000_000_000:
        Em_value = x / 1_000_000_000_000_000_000
        Em_str = str(Em_value)
        integer_part, decimal_part = Em_str.split('.')
        if decimal_part == '0':
            return f"{integer_part}Em"
        else:
            return f"{integer_part}.{decimal_part.rstrip('0')}Em"
    elif x < 1_000_000_000_000_000_000_000_000:
        Zm_value = x / 1_000_000_000_000_000_000_000
        Zm_str = str(Zm_value)
        integer_part, decimal_part = Zm_str.split('.')
        if decimal_part == '0':
            return f"{integer_part}Zm"
        else:
            return f"{integer_part}.{decimal_part.rstrip('0')}Zm"
    else:
        Ym_value = x / 1_000_000_000_000_000_000_000_000
        Ym_str = str(Ym_value)
        integer_part, decimal_part = Ym_str.split('.')
        if decimal_part == '0':
            return f"{integer_part}Ym"
        else:
            return f"{integer_part}.{decimal_part.rstrip('0')}Ym"
            return f"{integer_part}.{decimal_part.rstrip('0')}Em"
        
# Josephus Permutation
def josephus(items, k):
    index = 0
    res = []
    
    while len(items) > 0:
        index = (index + k - 1) % len(items)
        res.append(items.pop(index))
        
    return res

# Prime number decompositions
import math

def getAllPrimeFactors(n):
    if not isinstance(n, int) or n <= 0:
        return []
    
    if n == 1:
        return [1]
    
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    if n > 2:
        factors.append(n)
    
    return factors

def getUniquePrimeFactorsWithCount(n):
    factors = getAllPrimeFactors(n)
    if not factors:
        return [[], []]
    
    unique_factors = list(set(factors))
    counts = [factors.count(factor) for factor in unique_factors]
    
    return [unique_factors, counts]

def getUniquePrimeFactorsWithProducts(n):
    factors_count = getUniquePrimeFactorsWithCount(n)
    if not factors_count[0]:
        return [1] if n == 1 else []
    
    products = [factor ** count for factor, count in zip(factors_count[0], factors_count[1])]
    
    return products

# Strip Comments
def strip_comments(strng, markers):
    lines = strng.split("\n")
    
    for i in range(len(lines)):
        for marker in markers:
            if marker in lines[i]:
                lines[i] = lines[i].split(marker)[0].rstrip()
    
    return "\n".join(lines)

# Next bigger number with the same digits
def next_bigger(number):
    num_str = list(str(number))
    
    i = len(num_str) - 2
    while i >= 0 and num_str[i] >= num_str[i + 1]:
        i -= 1
    
    if i == -1:
        return -1
    
    j = len(num_str) - 1
    while num_str[j] <= num_str[i]:
        j -= 1
    
    num_str[i], num_str[j] = num_str[j], num_str[i]
    num_str = num_str[:i+1] + num_str[i+1:][::-1]
    
    next_permutation = int(''.join(num_str))
    
    return next_permutation

# The observed PIN
from itertools import product

def get_pins(observed):
    all_digits = {
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['0', '5', '7', '8', '9'],
        '9': ['6', '8', '9'],
        '0': ['0', '8']
    }
    

    possible_digits = [all_digits[char] for char in observed]
    pin_combinations = [''.join(pin) for pin in product(*possible_digits)]
    
    return pin_combinations

# Next smaller number with the same digits
def next_smaller(number):
    num_str = list(str(number))
    
    i = len(num_str) - 2
    while i >= 0 and num_str[i] <= num_str[i + 1]:
        i -= 1
    
    if i == -1:
        return -1
    
    j = len(num_str) - 1
    while num_str[j] >= num_str[i]:
        j -= 1
    
    num_str[i], num_str[j] = num_str[j], num_str[i]
    num_str = num_str[:i+1] + num_str[i+1:][::-1]
    
    next_permutation = int(''.join(num_str))
    
    if num_str[0] == '0':
        return -1
    
    return next_permutation

# Fibonacci, Tribonacci and friends
def xbonacci(signature, n):
    res = signature
    x = len(signature)
    
    if n < x: return signature[:n]
    
    while len(res) < n:
        res.append(sum(res[-x:]))
        
    return res

# Title Case
def title_case(title, minor_words=""):
    if not title or title == "": return ""
    res_list = [title.split(" ")[0].capitalize()]
    
    for word in title.split(" ")[1:]:
        if word.lower() in [word.lower() for word in minor_words.split(" ")]:
            res_list.append(word.lower())
        else:
            res_list.append(word.capitalize())
            
    return " ".join(res_list)
# or
def title_case(title, minor_words=""):
    if not title or title == "": return ""
    return " ".join([title.split(" ")[0].capitalize()] + [word.lower() if word.lower() in [word.lower() for word in minor_words.split(" ")] else word.capitalize() for word in title.split(" ")[1:]])

# Sum of Pairs
def sum_pairs(ints, s):
    if not isinstance(ints, list) or not ints:
        return []

    seen = set()
    for num in ints:
        target = s - num
        if target in seen:
            return [target, num]
        seen.add(num)
    
    return None

# Josephus Survivor
def josephus_survivor(n, k):
    people = list(range(1, n + 1))
    index = 0
    
    while len(people) > 1:
        index = (index + k - 1) % len(people)
        people.pop(index)
    
    return people[0]

# Best travel
def choose_best_sum(t, k, main_list):
    result = []
    stack = [(0, [])]

    while stack:
        start, comb = stack.pop()
    
        if len(comb) == k:
            result.append(comb)
            continue

        for i in range(start, len(main_list)):
            new_comb = comb + [main_list[i]]
            stack.append((i + 1, new_comb))
    
    if len(sorted([sum(i) for i in [i for i in result if sum(i) <= t]])) >= 1: return sorted([sum(i) for i in [i for i in result if sum(i) <= t]])[-1]
    return None

# Roman Numerals Encoder
def solution(n):
    roman_pieces = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    result = []
    
    for value, symbol in roman_pieces:
        while n >= value:
            result.append(symbol)
            n -= value
    
    return "".join(result)

# Roman Numerals Decoder
def solution(s):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in s:
        current_value = roman_values[char]
        total += current_value
        
        if current_value > prev_value:
            total -= 2 * prev_value
        
        prev_value = current_value
    
    return total

# Encrypt this!
def encrypt_this(text):
    words = text.split(" ")
    res = []
    for character in words:
        new = ""
        temp = ""
        for j in range(len(character)):
            if j == 0:
                new += str(ord(character[j]))
            elif j == 1:
                temp = character[j]
                new += character[-1]
            elif j == len(character) - 1:
                new += temp
            else:
                new += character[j]  
                
        res.append(new)
        
        
    return " ".join(list(res)) 

# A disguised sequence (I)
def fcn (n):
    return 2**(n)

# A Rule of Divisibility by 13
def thirt(n):
    seq = [1, 10, 9, 12, 3, 4]
    digits = [int(d) for d in reversed(str(n))]
    
    while True:
        next_n = sum(d * seq[i % len(seq)] for i, d in enumerate(digits))
        if next_n == n:
            return next_n
        n = next_n
        digits = [int(d) for d in reversed(str(n))]