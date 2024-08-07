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