# Vowel Count
def get_count(sentence):
    return len([i for i in sentence if i in "aeiou"])

# Disemvowel Trolls
def disemvowel(s):
    return "".join([i for i in s if i not in "aeiouAEIOU"])

# Square Every Digit
def square_digits(num):
    return int("".join([str(int(i)**2) for i in str(num)]))

# Highest and Lowest
def high_and_low(numbers):
    return str(max([int(i) for i in numbers.split(" ")])) + " " + str(min([int(i) for i in numbers.split(" ")]))

# List Filtering
def filter_list(l):
    return [i for i in l if type(i) != str]

# Descending Order
def descending_order(num):
    return int("".join(str(i) for i in list(reversed(list(sorted([int(i) for i in str(num)]))))))

# You're a square!
def is_square(n):  
    return int(n**0.5) * int(n**0.5) == n if type(n) == int and n >= 0 else False

# Get the Middle Character
def get_middle(s):
    return s[int(len(s)/2)] if len(s)%2!= 0 else s[int(len(s)/2)-1]+ s[int(len(s)/2)]

# Isograms
def is_isogram(string):
    return len(string.lower()) == len(set(string.lower()))

# Exes and Ohs
def xo(s):
    return s.replace("X", "x").replace("O", "o").count("x") == s.replace("X", "x").replace("O", "o").count("o")

# Jaden Casing Strings
def to_jaden_case(string):
    return " ".join([i.capitalize() for i in string.split(" ")])

# Shortest Word
def find_short(s):
    return min([len(i) for i in s.split(" ")])

# Mumbling
def accum(st):
    return "-".join([((i+1)*st[i]).capitalize() for i in range(len(st))])

# String ends with?
def solution(text, ending):
    return text.endswith(ending)

# Complementary DNA
def DNA_strand(dna):
    return "".join([{ "A": "T", "T": "A", "C": "G", "G": "C"}[i] for i in dna])

# Sum of two lowest positive integers
def sum_two_smallest_numbers(numbers):
    return min(numbers) + list(sorted(numbers))[1]

# Beginner Series #3 Sum of Numbers
def get_sum(a,b):
    return sum(list(range(min(a,b), max(a,b)+1)))

# Friend or Foe?
def friend(x):
    return [i for i in x if len(i) == 4]

# Credit Card Mask
def maskify(cc):
    return "#"*(len(cc)-4) +cc[-4:] if len(cc) > 4 else cc

# Binary Addition
def add_binary(a,b):
    return str(bin(a+b))[2:]

# Is this a triangle?
def is_triangle(a, b, c):
    return a+b > c and b+c > a and c+a > b

# Regex validate PIN code
def validate_pin(pin):
    return (len(pin) == 4 or len(pin) == 6) and [i.isdigit() for i in pin].count(True) == len(pin)

# Two to One
def longest(a1, a2):
    return "".join(list(sorted(list(set(a1+a2)))))

# Categorize New Member
def open_or_senior(data):
    return ["Senior" if i[0]>=55 and i[1]>7 else "Open" for i in data]

# Find the next perfect square!
def find_next_square(sq):
    return (int(sq**0.5)+1)**2 if int(sq**0.5)*int(sq**0.5)==sq else -1

# Sum of odd numbers
def row_sum_odd_numbers(n):
    return n**3

# Growth of a Population
def nb_year(p0, percent, aug, p):
    start = p0
    y = 0
    while start < p:
        start += int((percent / 100) * start) + aug
        y += 1
    return y

# Printer Errors
def printer_error(s):
    return f"{len([i for i in s if i in 'nopqrstuvwxyz'])}/{len(s)}"

# Ones and Zeros
def binary_array_to_number(arr):
    return binaryToDecimal("".join([str(i) for i in arr]))

def binaryToDecimal(n):
    num = n
    dec_value = 0
    base1 = 1
     
    len1 = len(num)
    for i in range(len1 - 1, -1, -1):
        if (num[i] == '1'):     
            dec_value += base1
        base1 = base1 * 2
        
    return dec_value

# Number of People in the Bus
def number(bus_stops):
    return sum(bus_stops[i][0] - bus_stops[i][1] for i in range(len(bus_stops)))

# Reverse words
def reverse_words(text):
    return " ".join([i[::-1] for i in text.split(" ")])

# Odd or Even?
def odd_or_even(arr):
    return "odd" if sum(arr)%2==1 else "even"

# The highest profit wins!
def min_max(lst):
    return [list(sorted(lst))[0], list(sorted(lst))[-1]]

# Sum of the first nth term of Series
def series_sum(n):
    res, start, val = 0, 1, 4
    for i in range(1, n + 1): res, start, val = res+start, 1/val, val+3
    return "{:.2f}".format(res)

# Find the divisors!
def divisors(integer):
    return [i for i in range(2, integer) if integer%i==0] if len([i for i in range(2, integer) if integer%i==0]) > 0 else f"{integer} is prime"

# Remove the minimum
def remove_smallest(n):
    return n[:n.index(min(n))] + n[n.index(min(n)) + 1:] if n != [] else []

# Testing 1-2-3
def number(lines):
    return [f"{i}: {lines[i-1]}" for i in range(1, len(lines)+1)]

# Count the divisors of a number
def divisors(n):
    return len([i for i in range(1, n+1) if n%i == 0])

# Find the stray number
def stray(arr):
    return int("".join([str(i) for i in arr if arr.count(i) == 1]))

# Sort Numbers
def solution(nums):
    return list(sorted(nums)) if nums else []

# Make a function that does arithmetic!
def arithmetic(a, b, operator):
    match operator:
        case "add": return a+b
        case "subtract": return a-b
        case "multiply": return a*b
        case "divide": return a/b

# Breaking chocolate problem
def break_chocolate(n, m):
    return n*m - 1 if n*m - 1 > 0 else 0

# Count the Digit
def nb_dig(n, d):
    return sum([str(i).count(str(d)) for i in [str(i**2) for i in range(0, n+1)]])

# Sum of a sequence
def sequence_sum(beg, end, step):
    return sum(list(range(beg, end+1, step)))

# Anagram Detection
def is_anagram(test, original):
    return list(sorted([i for i in test.lower()])) == list(sorted([i for i in original.lower()]))

# Sort array by string length
def sort_by_length(arr):
    return list(sorted(arr, key=len))

# Remove anchor from URL
def remove_url_anchor(url):
    return url[:url.index("#")] if "#" in url else url

# Money, Money, Money
def calculate_years(principal, interest, tax, desired):
    y = 0
    while principal < desired:
        principal += principal * interest * (1 - tax)
        y += 1
    return y

# Factorial
def factorial(n):
    if n < 0 or n > 20: raise ValueError("Factorial is not defined for negative numbers")
    return 1 if n == 0 else n * factorial(n - 1)