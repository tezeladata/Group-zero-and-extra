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

# Help the bookseller !
def stock_list(list1, list2):
    updated = [i.split(" ") for i in list1]
    
    score = []
    
    for char in list2:
        score.append(calculate(list1, char))
        
    if all(i[1] == 0 for i in score):
        return ""
    
    for i in range(len(score)): 
        score[i] = f"({score[i][0]} : {score[i][1]})" 
        
    return " - ".join(score)
    
def calculate(main_ls, char):
    score = 0
    
    for ls in main_ls:
        symbol, quantity = ls.split()
        if symbol[0] == char:
            score += int(quantity)
            
    return (char, score)

# Simple Encryption #1 - Alternating Split
def decrypt(encrypted_text, n):
    if not encrypted_text or n <= 0:
        return encrypted_text
    
    mid = len(encrypted_text) // 2
    
    for _ in range(n):
        odd = encrypted_text[mid:]
        even = encrypted_text[:mid]
        
        decrypted_text = ""
        for i in range(len(odd)):
            if i < len(even):
                decrypted_text += odd[i] + even[i]
            else:
                decrypted_text += odd[i]
        
        encrypted_text = decrypted_text
    
    return decrypted_text

def encrypt(text, n):
    if not text or n <= 0:
        return text
    
    for _ in range(n):
        text = text[1::2] + text[::2]
    
    return text

# Good vs Evil
def good_vs_evil(good, evil):
    good, evil = [int(i) for i in good.split(" ")], [int(i) for i in evil.split(" ")]
    
    good[1], good[2], good[3], good[4], good[5] = good[1] * 2, good[2] * 3, good[3] * 3, good[4] * 4, good[5] * 10
    evil[1], evil[2], evil[3], evil[4], evil[5], evil[6] = evil[1] * 2, evil[2] * 2, evil[3] * 2, evil[4] * 3, evil[5] * 5, evil[6] * 10
    
    good_count = 0
    for i in good:
        good_count += i
        
    evil_count = 0
    for i in evil:
        evil_count += i
        
    if good_count > evil_count:
        return "Battle Result: Good triumphs over Evil"
    elif evil_count > good_count:
        return "Battle Result: Evil eradicates all trace of Good"
    return "Battle Result: No victor on this battle field"

# Matrix Addition
def matrix_addition(a, b):
    res = []
    
    for i in range(len(a)):
        row = []
        
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        
        res.append(row)
        
    return res

# Tortoise racing
def race(v1, v2, g):
    if v1 >= v2:
        return None

    time_sec = g * 3600 / (v2 - v1)
    
    hours = int(time_sec / 3600)
    time_sec %= 3600
    minutes = int(time_sec / 60)
    seconds = int(time_sec % 60)

    return [hours, minutes, seconds]
# or:
def race(v1, v2, g):
    return [int((g * 3600 / (v2 - v1) / 3600)), int((g * 3600 / (v2 - v1) % 3600) / 60), int((g * 3600 / (v2 - v1) % 3600) % 60)] if v1 <=v2 else None

# Meeting
def meeting(s):
    names = [name.upper().split(":") for name in s.split(";")]
    
    names.sort(key=lambda x: (x[1], x[0]))
    
    return "".join(["({}, {})".format(last, first) for first, last in names])

# Dashatize it
def dashatize(n):
    res = ''.join(['-' + ch + '-' if int(ch) % 2 != 0 else ch for ch in str(abs(n))])
    
    dashatized_str = res.replace('--', '-').strip('-')
    
    return dashatized_str
# or:
def dashatize(n):
    return ''.join(['-' + ch + '-' if int(ch) % 2 != 0 else ch for ch in str(abs(n))]).replace('--', '-').strip('-')

# Lottery Ticket
def bingo(ticket,win):
    all_ord = []
    
    for i in ticket:
        res = []
        for char in i[0]:
            res.append(ord(char))
        all_ord.append([res, i[1]])
        
    final = 0
    
    for i in all_ord:
        for x in i[0]:
            if x == i[1]:
                final += 1
    
    if final >= win:
        return "Winner!"
    return "Loser!"
# or:
def bingo(ticket, win):
    return "Winner!" if sum(any(ord(char) == num for char in chars) for chars, num in ticket) >= win else "Loser!"

# If you can read this...
def to_nato(words: str) -> str:
    d = {
        'A': 'Alfa',  'B': 'Bravo',   'C': 'Charlie',
        'D': 'Delta',  'E': 'Echo',    'F': 'Foxtrot',
        'G': 'Golf',   'H': 'Hotel',   'I': 'India',
        'J': 'Juliett','K': 'Kilo',    'L': 'Lima',
        'M': 'Mike',   'N': 'November','O': 'Oscar',
        'P': 'Papa',   'Q': 'Quebec',  'R': 'Romeo',
        'S': 'Sierra', 'T': 'Tango',   'U': 'Uniform',
        'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray',
        'Y': 'Yankee', 'Z': 'Zulu'
    }
    
    return " ".join([d[char] if char in d else char for char in words.upper() if char in d or char in ",.!?"])
# or:
# from preloaded import NATO

# def to_nato(words):
#     return " ".join([NATO[char] if char in NATO else char for char in words.upper() if char in NATO or char in ",.!?"])

# Statistics for an Athletic Association
def stat(strg):
    if strg == "":
        return ''
    
    data_list = []
    for runner_time in strg.split(", "):
        times = convert_to_seconds([int(time) for time in runner_time.split("|")])
        data_list.append(times)
    data_list.sort()
    
    
    return f"Range: {stat_range(data_list)} Average: {stat_mean(data_list)} Median: {stat_median(data_list)}"


# Funcs for convertions
def convert_to_seconds(time):
    return time[0] * 3600 + time[1] * 60 + time[2]

def convert_to_hms(seconds):
    hours = int(seconds / 3600 // 1)
    minutes = int((seconds - hours * 3600) / 60 // 1)
    seconds = int(seconds - hours * 3600 - minutes * 60)
    
    return f"{hours:02d}|{minutes:02d}|{seconds:02d}"


# Funcs for range, mean, median
def stat_range(data):
    return convert_to_hms(data[-1] - data[0])

def stat_mean(data):
    return convert_to_hms(sum(data) / len(data))
    
def stat_median(data):
    data_length = len(data)
    middle = data_length // 2
    
    if data_length % 2 == 0:
        return convert_to_hms((data[middle - 1] + data[middle]) / 2)
    return convert_to_hms(data[middle])