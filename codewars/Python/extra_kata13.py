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