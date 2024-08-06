# Multiply
def multiply(a, b):
    return a * b

# Even or Odd
def even_or_odd(number):
    if number%2 == 0: return "Even"
    return "Odd"

# Convert a Number to a String!
def number_to_string(num):
    return str(num)

# Reversed Strings
def solution(string):
    return string[::-1]

# Opposite number
def opposite(number):
    return number * -1

# Return Negative
def make_negative( number ):
    return number * - 1 if number >= 0 else number

# Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# Sum of positive
def positive_sum(arr):
    return sum([i for i in arr if i > 0])

# String repeat
def repeat_str(repeat, string):
    return string * repeat

# Remove First and Last Character
def remove_char(s):
    return s[1:-1]

# Square(n) Sum
def square_sum(numbers):
    return sum([i**2 for i in numbers])

# Find the smallest integer in the array
def find_smallest_int(arr):
    return min(arr)

# Convert a String to a Number!
def string_to_number(s):
    return int(s)

# Grasshopper - Summation
def summation(num):
    return sum([i for i in range(num+1)])

# Function 1 - hello world
def greet():
    return "hello world!"

# Counting sheep...
def count_sheeps(sheep):
    return sheep.count(1)

# Remove String Spaces
def no_space(x):
    return x.replace(" ", "")

# You Can't Code Under Pressure #1
def double_integer(i):
    return i*2

# Returning Strings
def greet(name):
    return f"Hello, {name} how are you doing today?"

# Convert a Boolean to a String
def boolean_to_string(b):
    return f"{b}"

# Basic Mathematical Operations
def basic_op(operator, value1, value2):
    match operator:
        case "+":
            return value1 + value2
        case "-":
            return value1 - value2
        case "*":
            return value1 * value2
        case "/":
            return value1 / value2
        
# Keep Hydrated!
def litres(time):
    return int(time/2)

# Century From Year
def century(year):
    return year // 100 if year% 100 == 0 else int(year / 100) + 1

# Beginner - Lost Without a Map
def maps(a):
    return [i*2 for i in a]

# Convert number to reversed array of digits
def digitize(n):
    return [int(i) for i in list(reversed([i for i in str(n)]))]

# Sum Arrays
def sum_array(a):
    return sum(a)

# Opposites Attract
def lovefunc( flower1, flower2 ):
    return True if (flower1 + flower2) %2 != 0 else False

# Beginner Series #1 School Paperwork
def paperwork(n, m):
    return n*m if (n > 0 and m > 0) else 0

# Beginner Series #2 Clock
def past(h, m, s):
    return h*3600000 + m*60000 + s*1000

# MakeUpperCase
def make_upper_case(s):
    return s.upper()

# Abbreviate a Two Word Name
def abbrev_name(name):
    return name[0].upper() + "." + name.split()[1][0].upper()

# Simple multiplication
def simple_multiplication(number) :
    return number*8 if number%2==0 else number*9

# Are You Playing Banjo?
def are_you_playing_banjo(name):
    return name + " plays banjo" if (name[0].lower() == "r") else name + " does not play banjo"

# A Needle in the Haystack
def find_needle(haystack):
    return f"found the needle at position {haystack.index('needle')}"

# Invert values
def invert(lst):
    return [i*-1 for i in lst]

# Calculate average
def find_average(numbers):
    return sum(numbers) / len(numbers) if len(numbers) > 0 else 0

# Sentence Smash
def smash(words):
    return " ".join(words)

# Is he gonna survive?
def hero(bullets, dragons):
    return bullets / dragons >= 2

# Beginner - Reduce but Grow
def grow(arr):
    prod = 1
    for i in arr:
        prod *= i
    return prod

# How good are you really?
def better_than_average(class_points, your_points):
    return (sum(class_points) / len(class_points)) < your_points

# Count of positives / sum of negatives
def count_positives_sum_negatives(arr):
    return [len([i for i in arr if i > 0]), sum([i for i in arr if i < 0])] if arr != [] else []

# DNA to RNA Conversion
def dna_to_rna(dna):
    return dna.replace("T", "U")

# Calculate BMI
def bmi(weight, height):
    user_bmi = weight / height**2
    if user_bmi <= 18.5: return "Underweight"
    elif user_bmi <= 25.0: return "Normal"
    elif user_bmi <= 30.0: return "Overweight"
    return "Obese"

# Fake Binary
def fake_bin(x):
    return "".join(["0" if int(i) < 5 else "1" for i in x])

# Find Maximum and Minimum Values of a List
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)

# Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg*fuel_left >= distance_to_pump

# You only need one - Beginner
def check(seq, elem):
    return seq.count(elem) >= 1

# Convert a string to an array
def string_to_array(s):
    return s.split(" ")

# Reversed sequence
def reverse_seq(n):
    return list(range(n, 0, -1))

# Count by X
def count_by(x, n):
    return list(range(x, x*n+1, x))

# Is n divisible by x and y?
def is_divisible(n,x,y):
    return n%x == 0 and n%y == 0

# Rock Paper Scissors!
def rps(p1, p2):
    if p1 == p2: return "Draw!"
    elif p1 == "scissors": return "Player 1 won!" if p2 == "paper" else "Player 2 won!"
    elif p1 == "paper": return "Player 1 won!" if p2 == "rock" else "Player 2 won!"
    elif p1 == "rock": return "Player 1 won!" if p2 == "scissors" else "Player 2 won!"

# If you can't sleep, just count sheep!!
def count_sheep(n):
    return "".join([f"{i} sheep..." for i in range(1, n+1)])

# Grasshopper - Personalized Message
def greet(name, owner):
    return "Hello boss" if name == owner else 'Hello guest'

# Quarter of the year
def quarter_of(month):
    if month <= 3: return 1
    elif month <= 6: return 2
    elif month <= 9: return 3
    return 4

# Transportation on vacation
def rental_car_cost(d):
    if d < 3: return d*40
    elif d < 7: return d*40 - 20
    return d*40 - 50

# Grasshopper - Grade book
def get_grade(s1, s2, s3):
    avg = (s1 + s2 + s3) / 3
    if avg < 60: return "F"
    elif avg < 70: return "D"
    elif avg < 80: return "C"
    elif avg < 90: return "B"
    return "A"

# Remove exclamation marks
def remove_exclamation_marks(s):
    return s.replace("!", "")

# Jenny's secret message
def greet(name):
    if name == "Johnny": return "Hello, my love!"
    return f"Hello, {name}!"

# Total amount of points
def points(games):
    res = 0
    for game in games:
        game = game.split(":")
        if int(game[0]) > int(game[1]): res += 3
        elif int(game[0]) == int(game[1]): res += 1
    return res

# Volume of a Cuboid
def get_volume_of_cuboid(length, width, height):
    return length * width * height

# Third Angle of a Triangle
def other_angle(a, b):
    return 180 - (a + b)

# Thinkful - Logic Drills: Traffic light
def update_light(current):
    lights = {
        "green": "yellow",
        "yellow": "red",
        "red": "green"
    }
    return lights[current]

# Area or Perimeter
def area_or_perimeter(l , w):
    return l**2 if l==w else 2*(l+w)

# L1: Set Alarm
def set_alarm(employed, vacation):
    if employed == True:
        if vacation != True: return True
        return False
    return False

# Sum Mixed Array
def sum_mix(arr):
    return sum([int(i) for i in arr])

# Sum without highest and lowest number
def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr else 0

# Grasshopper - Messi goals function
def goals(*args):
    return sum(args)

# Double Char
def double_char(s):
    return "".join([char*2 for char in s])

# The Feast of Many Beasts
def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]

# Get the mean of an array
def get_average(marks):
    return int(sum(marks) / len(marks))

# Parse nice int from char problem
def get_age(age):
    return int(age[0])

# Array plus array
def array_plus_array(arr1,arr2):
    return sum(arr1 + arr2)

# Reversed Words
def reverse_words(s):
    return " ".join(list(reversed(s.split(" "))))

# Grasshopper - Check for factor
def check_for_factor(base, factor):
    return base % factor == 0

# Beginner Series #4 Cockroach
def cockroach_speed(s):
    return int(s*27.777778)

# Keep up the hoop
def hoop_count(n):
    return "Great, now move on to tricks" if n >= 10 else "Keep at it until you get it"

# Switch it Up!
def switch_it_up(number):
    match number:
        case 0: return "Zero"
        case 1: return "One"
        case 2: return "Two"
        case 3: return "Three"
        case 4: return "Four"
        case 5: return "Five"
        case 6: return "Six"
        case 7: return "Seven"
        case 8: return "Eight"
        case 9: return "Nine"

# Function 2 - squaring an argument
def square(n):
    return n**2

# Twice as old
def twice_as_old(dad, son):
    return dad - (son*2) if dad - (son*2) > 0 else (dad - (son*2)) * -1

# Removing Elements
def remove_every_other(my_list):
    return [my_list[i] for i in range(len(my_list)) if i%2 != 1]

# Get Planet Name By ID
def get_planet_name(id):
    name=""
    match id:
        case 1: name = "Mercury"
        case 2: name = "Venus"
        case 3: name = "Earth"
        case 4: name = "Mars"
        case 5: name = "Jupiter"
        case 6: name = "Saturn"
        case 7: name = "Uranus"  
        case 8: name = "Neptune"
    return name

# All Star Code Challenge #18
def str_count(strng, letter):
    return strng.count(letter)

# Is it even?
def is_even(n): 
    return n%2 == 0

# Will there be enough space?
def enough(cap, on, wait):
    return on + wait - cap if (on + wait - cap) > 0 else 0

# Count the Monkeys!
def monkey_count(n):
    return list(range(1, n+1))

# Grasshopper - Terminal game move function
def move(position, roll):
    return position + roll*2

# What is between?
def between(a,b):
    return list(range(a, b+1))

# Grasshopper - Debug sayHello
def say_hello(name):
    return f"Hello, {name}"

# Is the string uppercase?
def is_uppercase(inp):
    return inp == inp.upper()

# Find the first non-consecutive number
def first_non_consecutive(arr):
    i = 1
    for x in arr:
        if i < len(arr) and arr[i] - arr[i-1] != 1:
            return arr[i]
        i += 1
    return None


# Powers of 2
def powers_of_two(n):
    return [2**i for i in range(n+1)]

# Cat years, Dog years
def human_years_cat_years_dog_years(human_years):
    year_dict = {
        1: [1, 15, 15],
        2: [2, 24, 24]
    }
    
    if human_years in year_dict:
        return year_dict[human_years]
    
    cat, dog = 24, 24
    for i in range(human_years - 2):
        cat += 4
        dog += 5
    return [human_years, cat, dog]

# altERnaTIng cAsE <=> ALTerNAtiNG CaSe
def to_alternating_case(string):
    return " ".join([word.swapcase() for word in string.split(" ")])

# Correct the mistakes of the character recognition software
def correct(s):
    return s.replace("5", "S").replace("0", "O").replace("1", "I")

# Is it a palindrome?
def is_palindrome(s):
    return s.lower() == s.lower()[::-1]

# Do I get a bonus?
def bonus_time(salary, bonus):
    return f"${salary * 10}" if bonus else f"${salary}"

# Student's Final Grade
def final_grade(exam, projects):
    if exam > 90 or projects > 10: return 100
    elif exam > 75 and projects >= 5: return 90
    elif exam > 50 and projects >= 2: return 75
    return 0

# Sum The Strings
def sum_str(a, b):
    if a and b: return str(int(a) + int(b))
    elif a and not b: return a
    elif b and not a: return b
    return "0"

# Expressions Matter
def expression_matter(a, b, c):
    return max([(a * (b + c)), (a * b * c), (a + b * c), ((a + b) * c), (a + b + c)])

# Difference of Volumes of Cuboids
def find_difference(a, b):
    return a[0]*a[1]*a[2] - b[0]*b[1]*b[2] if a[0]*a[1]*a[2] > b[0]*b[1]*b[2] else b[0]*b[1]*b[2] - a[0]*a[1]*a[2]

# I love you, a little , a lot, passionately ... not at all
def how_much_i_love_you(nb_petals):
    user_dict = {
        0: "not at all",
        1: "I love you",
        2: "a little",
        3: "a lot",
        4: "passionately",
        5: "madly",
        6: "not at all"
    }
    return user_dict[nb_petals % 6]

# Reverse List Order
def reverse_list(l):
    return list(reversed(l))

# Welcome!
def greet(language):
    if language=="english":
        return "Welcome"
    if language=="czech":
        return "Vitejte"
    if language=="danish":
        return "Velkomst"
    if language=="dutch":
        return "Welkom"
    if language=="estonian":
        return "Tere tulemast"
    if language=="finnish":
        return "Tervetuloa"
    if language=="flemish":
        return "Welgekomen"
    if language=="french":
        return "Bienvenue"
    if language=="german":
        return "Willkommen"
    if language=="irish":
        return "Failte"
    if language=="italian":
        return "Benvenuto"
    if language=="latvian":
        return "Gaidits"
    if language=="lithuanian":
        return "Laukiamas"
    if language=="polish":
        return "Witamy"
    if language=="spanish":
        return "Bienvenido"
    if language=="swedish":
        return "Valkommen"
    if language=="welsh":
        return "Croeso"
    else:
        return "Welcome"
    
# Grasshopper - Messi Goals
la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5

total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals

# Count Odd Numbers below n
def odd_count(n):
    return int(n/2)

# Short Long Short
def solution(a, b):
    return a + b + a if len(a) < len(b) else b + a + b

# My head is at the wrong end!
def fix_the_meerkat(arr):
    return list(reversed(arr))

# Sort and Star
def two_sort(array):
    return "".join([i+"***" for i in sorted(array)[0]])[:-3]

# Find Multiples of a Number
def find_multiples(integer, limit):
    return [i for i in range(integer, limit+1) if i%integer == 0]

# Drink about
def people_with_age_drink(age):
    if age < 14: return "drink toddy"
    elif age < 18: return "drink coke"
    elif age < 21: return "drink beer"
    return "drink whisky"

# Vowel remover
def shortcut( s ):
    return "".join([i for i in s if i not in "aeiou"])

# Unfinished Loop - Bug Fixing #1
def create_array(n):
    res=[]
    i=1
    while i<=n: 
        res+=[i]
        i += 1
    return res

# get character from ASCII Value
def get_char(c):
    return chr(c)

# What's the real floor?
def get_real_floor(n):
    if n <= 0: return n
    elif n >= 13: return n-2
    return n - 1

# Filter out the geese
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    return [i for i in birds if i not in geese]

# Exclusive "or" (xor) Logical Operator
def xor(a,b):
    return True if a != b else False

# Find numbers which are divisible by given number
def divisible_by(numbers, divisor):
    return [i for i in numbers if i%divisor == 0]

# Name Shuffler
def name_shuffler(str):
    return str.split(" ")[1] + " " + str.split(" ")[0]

# Capitalization and Mutability
def capitalize_word (word):
    return word[0].upper() + word[1:]

# Training JS #7: if..else and ternary operator
def sale_hotdogs(n):
    if n < 5: return n*100
    elif n >= 5 and n < 10: return n*95
    return n*90

# Lario and Muigi Pipe Problem
def pipe_fix(nums):
    return [i for i in range(nums[0], nums[-1] + 1)]

# Grasshopper - If/else syntax debug
def check_alive(health):
    return health > 0

# Plural
def plural(n):
    return n > 1 or n == 0

# How many lightsabers do you own?
def how_many_light_sabers_do_you_own(*args):
    if args: return 18 if args[0] == "Zach" else 0
    return 0

# Stringy Strings
def stringy(size):
    return "".join(["1" if i%2 != 0 else "0" for i in range(1,size+1)])

# Grasshopper - Basic Function Fixer
def add_five(num):
    return num + 5

# Super Duper Easy
def problem(a):
    try:
        return a * 50 + 6
    except:
        return "Error"
    
# Multiplication table for number
def multi_table(number):
    return "\n".join([f"{i} * {number} = {i*number}" for i in range(1, 11)])

# Merge two sorted arrays into one
def merge_arrays(arr1, arr2):
    return sorted(list(set(arr1 + arr2)))

# Well of Ideas - Easy Version
def well(x):
    if x.count("good") == 0: return "Fail!"
    elif x.count("good") <= 2: return "Publish!"
    return "I smell a series!"

# 5 without numbers !!
def unusual_five():
    return len("hello")

# Get Nth Even Number
def nth_even(n):
    return n*2 -2

# A wolf in sheep's clothing
def warn_the_sheep(queue):
    return f"Oi! Sheep number {len(queue) - queue.index('wolf') - 1}! You are about to be eaten by a wolf!" if queue[-1] != "wolf" else 'Pls go away and stop eating my sheep'

# Gravity Flip
def flip(d, a):
    return sorted(a) if d == "R" else list(reversed(sorted(a)))

# Regular Ball Super Ball
class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

# Remove duplicates from list
def distinct(seq):
    res = []
    for i in seq:
        if i not in res:
            res.append(i)
    return res

# Grasshopper - Terminal game combat function
def combat(health, damage):
    return health - damage if health - damage > 0 else 0

# Determine offspring sex based on genes XX and XY chromosomes
def chromosome_check(chromosome):
    return 'Congratulations! You\'re going to have a son.' if chromosome == "XY" else 'Congratulations! You\'re going to have a daughter.'

# The Wide-Mouthed frog!
def mouth_size(animal): 
    return "small" if animal.lower() == "alligator" else "wide"

# Add Length
def add_length(str):
    return [f"{i} {len(i)}" for i in str.split(" ")]

# To square(root) or not to square(root)
def square_or_square_root(arr):
    return [int(i**0.5) if int(i**0.5)**2 == i else i * i for i in arr]

# Convert to Binary
def to_binary(n):
    return int(bin(n)[2:])

# Bin to Decimal
def bin_to_decimal(inp):
    return int(inp, 2)

# Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence
def replace_exclamation(st):
    return "".join(["!" if i.lower() in "aeiou" else i for i in st])

# The 'if' function
def _if(bool, func1, func2):
    if bool: func1()
    else: func2()

# Hello, Name or World!
def hello(*args):
    if not args or args[0] == "": return "Hello, World!"
    return f"Hello, {args[0].capitalize()}!"

# Holiday VIII - Duty Free
def duty_free(price, discount, holiday_cost):
    return int(holiday_cost / (price * discount/100))

# FIXME: Replace all dots
def replace_dots(s):
    return s.replace(".", "-")

# No zeros for heros
def no_boring_zeros(n):
    if not n or n == "": return 0
    while str(n)[-1] == "0": n = int(str(n)[:-1])
    return n

# Grasshopper - Function syntax debugging
def main(verb, noun): return verb + noun

# Exclamation marks series #1: Remove an exclamation mark from the end of string
def remove(n):
    if not n or n == "": return ""
    return n[:-1] if n[-1] == "!" else n

# Hex to Decimal
def hex_to_dec(s):
    return int(s, 16)

# Welcome to the City
def say_hello(name, city, state):
    return f"Hello, {' '.join(name)}! Welcome to {city}, {state}!"

# Enumerable Magic #25 - Take the First N Elements
def take(arr,n):
    return arr[:n]

# Find the position!
def position(alphabet):
    return f'Position of alphabet: {"abcdefghijklmnopqrstuvwxyz".index(alphabet.lower()) + 1}'

# Is this my tail?
def correct_tail(body, tail):
    return body[-1] == tail

# Price of Mangoes
def mango(quantity, price):
    return (quantity - quantity//3) * price

# Surface Area and Volume of a Box
def get_size(w,h,d):
    return [2*(w*d + w*h + d*h), w*h*d]

# Find the Remainder
def remainder(a,b):
    maximum = max(a, b)
    minimum = min(a, b)
    
    if minimum == 0: return None
    return maximum % minimum

# Pillars
def pillars(num_pill, dist, width):
    return 0 if num_pill == 1 else (num_pill - 1) * (dist * 100) + (num_pill - 2) * width

# 101 Dalmatians - squash the bugs, not the dogs!
def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    
    if n <= 10:
        respond = dogs[0]
    elif n <= 50:
        respond = dogs[1]
    elif n == 101:
        respond = dogs[3]
    else:
        respond = dogs[2]
  
    return respond

# Find out whether the shape is a cube
def cube_checker(volume, side):
    return volume == side ** 3 if side > 0 else 0

# Alan Partridge II - Apple Turnover
def apple(x):
    return "It's hotter than the sun!!" if int(x) ** 2 > 1000 else "Help yourself to a honeycomb Yorkie for the glovebox."

# Grasshopper - Array Mean
def find_average(nums):
    return sum(nums) / len(nums)

# Printing Array elements with Comma delimiters
def print_array(arr):
    return ",".join([str(i) for i in arr])

# Sum of differences in array
def sum_of_differences(arr):
    return sum([i*-1 for i in [list(reversed(sorted(arr)))[i+1] - list(reversed(sorted(arr)))[i] for i in range(len(arr) - 1)]])

# Reversing Words in a String
def reverse(st):
    return " ".join(reversed(st.split()))

# Generate range of integers
def generate_range(start, stop, step):
    return list(range(start, stop+1, step))

# Grasshopper - Debug
def weather_info (temp):
    c = convert_to_celsius(temp)
    if (c < 0):
        return (str(c) + " is freezing temperature")
    else:
        return (str(c) + " is above freezing temperature")
    
def convert_to_celsius (temperature):
    celsius = (temperature - 32) * (5/9)
    return celsius

# Remove First and Last Character Part Two
def array(string):
    return " ".join(string.split(",")[1:-1]) if len(string.split(",")) > 2 else None

# Dollars and Cents
def format_money(amount):
    if type(amount) == int: return f"${amount}.00"
    return f"${amount}0" if len(f"${amount}".split(".")[-1]) == 1 else f"${amount}"

# String cleaning
def string_clean(s):
    return "".join([i for i in s if i not in "0123456789"])

# Enumerable Magic - Does My List Include This?
def include(arr, item):
    return item in arr

# Check same case
def same_case(a, b): 
    if a.isupper() and b.isupper(): return 1
    elif a.islower() and b.islower(): return 1
    elif (a.islower() and b.isupper()) or (a.isupper() and b.islower()): return 0
    return -1

# Find Nearest square number
def nearest_sq(n):
    return min([int(n**0.5)**2, (int(n**0.5) + 1)**2], key=lambda x: abs(n - x))

# Swap Values
def swap_values(args): 
    args[0], args[1] = args[1], args[0]

# Simple validation of a username with regex
def validate_usr(username):
    return len([i for i in username if i in "abcdefghijklmnopqrstuvwxyz0123456789_"]) == len(username) and len(username) >= 4 and len(username) <= 16

# Sum of Multiples
def sum_mul(n, m):
    if n <= 0 or m <= 0: return "INVALID"
    if n >= m: return 0
    return sum(i for i in range(n, m, n))

# Simple Fun #1: Seats in Theater
def seats_in_theater(tot_cols, tot_rows, col, row):
    return (tot_cols - col + 1) * (tot_rows - row)

# Multiple of index
def multiple_of_index(arr):
    return [arr[i] for i in range(1, len(arr)) if arr[i]%i == 0] if arr[0] != 0 else [0] + [arr[i] for i in range(1, len(arr)) if arr[i]%i == 0]

# Return the day
def whatday(num):
    match num:
        case 1: return "Sunday"
        case 2: return "Monday"
        case 3: return "Tuesday"
        case 4: return "Wednesday"
        case 5: return "Thursday"
        case 6: return "Friday"
        case 7: return "Saturday"
    return "Wrong, please enter a number between 1 and 7"

# Fundamentals: Return
def add(a, b):
    return a+b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

def mod(a, b):
    return a%b

def exponent(a, b):
    return a**b

def subt(a, b):
    return a-b

# Return to Sanity
def mystery():
    results = {'sanity': 'Hello'}
    return results

# Sleigh Authentication
class Sleigh(object):
    def authenticate(self, name, password):
        self.name = name
        self.password = password
    
        return True if self.name == "Santa Claus" and self.password == "Ho Ho Ho!" else False
    
# Take the Derivative
def derive(coefficient, exponent): 
    return f"{coefficient * exponent}x^{exponent-1}"

# L1: Bartender, drinks!
def get_drink_by_profession(param):
    all = {
        "Jabroni": "Patron Tequila",
        "School Counselor": "Anything with Alcohol",
        "Programmer": "Hipster Craft Beer",
        "Bike Gang Member": "Moonshine",
        "Politician": "Your tax dollars",
        "Rapper": "Cristal"
    }
    return all[" ".join([word.capitalize() for word in param.split(" ")])] if " ".join([word.capitalize() for word in param.split(" ")]) in all else "Beer"

# Kata Example Twist
websites = ["codewars" for _ in range(1000)]

# How old will I be in 2099?
def calculate_age(year_of_birth, current_year):
    if 2099 - (2099 - (current_year - year_of_birth)) > 0: 
        return f"You are {2099 - (2099 - (current_year - year_of_birth))} years old." if 2099 - (2099 - (current_year - year_of_birth)) != 1 else f"You are {2099 - (2099 - (current_year - year_of_birth))} year old."
    elif 2099 - (2099 - (current_year - year_of_birth)) == 0: return 'You were born this very year!'
    return f"You will be born in {(2099 - (2099 - (current_year - year_of_birth))) * -1} years." if (2099 - (2099 - (current_year - year_of_birth))) * -1 != 1 else f"You will be born in {(2099 - (2099 - (current_year - year_of_birth))) * -1} year."

# Basic Training: Add item to an Array
websites.append("codewars")

# Grasshopper - Combine strings
def combine_names(f, l):
    return f + " " + l

# Regex count lowercase letters
def lowercase_count(strng):
    return len([i for i in strng if i in "abcdefghijklmnopqrstuvwxyz"])

# String Templates - Bug Fixing #5
def build_string(*args):
    return "I like {}!".format(", ".join(args))

# USD => CNY
def usdcny(usd):
    cny = usd * 6.750
    return f"{cny:.2f} Chinese Yuan"

# Triple Trouble
def triple_trouble(one, two, three):
    return "".join(f"{one[i]}{two[i]}{three[i]}" for i in range(len(one)))

# Formatting decimal places #0
def two_decimal_places(n):
    return round(n, 2)

# Multiply the number
def multiply(n):
    return n * 5**len(str(n)) if n > 0 else n * 5**(len(str(n))-1)

# OOP: Object Oriented Piracy
class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    
    def is_worth_it(self):
        return self.draft - self.crew * 1.5 > 20
    
# Find the Difference in Age between Oldest and Youngest Family Members
def difference_in_ages(ages):
    return (min(ages), max(ages), max(ages) - min(ages))

# Area of a Square
import math
def square_area(A):
    r = A*4 / (math.pi * 2)
    return round(r**2, 2)

# Never visit a . . . !?
def subtract_sum(number):
    return "apple"

# How many stairs will Suzuki climb in 20 years?
def stairs_in_20(stairs):
    return sum([sum(arr) for arr in stairs]) * 20

# Color Ghost
import random
class Ghost(object):
    def __init__(self): 
        self.color = random.choice(["white", "yellow", "purple", "red"])

# Name on billboard
def billboard(name, price=30):
    return sum([price for char in name])

# CSV representation of array
def to_csv_text(array):
    return "\n".join([",".join([str(i) for i in arr]) for arr in array])

# Define a card suit
def define_suit(card):
    return {"C": "clubs", "S": "spades", "D": "diamonds", "H": "hearts"}[card[-1].upper()]

# Basic subclasses - Adam and Eve
class Human:
    def __init__(self, name):
        self.name = name

class Man(Human):
    def __init__(self, name="Adam"):
        super().__init__(name)

class Woman(Human):
    def __init__(self, name="Eve"):
        super().__init__(name)

def God():
    adam = Man()
    eve = Woman()
    return [adam, eve]

# Classic Hello World
class Solution:
    def main(*args):
        print("Hello World!")

# Do you speak "English"?
def sp_eng(sentence): 
    return "english" in sentence.lower()

# Holiday VI - Shark Pontoon
def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    return "Alive!" if pontoon_distance / you_speed < shark_distance / (shark_speed / 2 if dolphin else shark_speed) else "Shark Bait!"

# Incorrect division method
def divide_numbers(x,y):
    return x / y

# Fix your code before the garden dies!
def rain_amount(mm):
    if mm < 40:
         return "You need to give your plant " + str(40 - mm) + "mm of water"
    else:
         return "Your plant has had more than enough water for today!"
    
# Remove the time
def shorten_to_date(long_date):
    return f"{long_date.split(' ')[0]} {long_date.split(' ')[1]} {long_date.split(' ')[2][:-1]}"

# Quadrants
def quadrant(x, y):
    if x<0 and y>0: return 2
    elif x>0 and y<0: return 4
    return 1 if x*y > 0 and x>0 else 3

# Chuck Norris VII - True or False? (Beginner)
def if_chuck_says_so():
    return bool(0)

# No Loops 2 - You only need one
def check(a, x): 
    return x in a

# Exclamation marks series #2: Remove all exclamation marks from the end of sentence
def remove(st):
    if not st or st == "": return ""
    while st[-1] == "!": st = st[:-1]
    return st

# Contamination #1 -String-
def contamination(text, char):
    if text and char: return "".join([char for _ in range(len(text))])
    elif text and not char: return ""
    return text

# Classy Classes
class Person:
    def __init__(self,name,age):
        self.info=f"{name}s age is {age}"

# Pythagorean Triple
def pythagorean_triple(integers):
    return list(sorted(integers))[0]**2 + list(sorted(integers))[1]**2 == list(sorted(integers))[2]**2

# The falling speed of petals
def sakura_fall(v):
    return 5*80/v if v > 0 else 0

# Regexp Basics - is it a digit?
def is_digit(n):
    return n.isdigit() and len(n) == 1

# SpeedCode #2 - Array Madness
def array_madness(a,b):
    return sum([i**2 for i in a]) > sum([i**3 for i in b])

# Is it a number?
def is_digit(s):
    if not s or s.strip() == "": return False
    try:
        float(s)
        return True
    except: return False

# Leonardo Dicaprio and Oscars
def leo(oscar):
    match oscar:
        case 88: return "Leo finally won the oscar! Leo is happy"
        case 86: return "Not even for Wolf of wallstreet?!"
    return "When will you give Leo an Oscar?" if oscar < 88 else "Leo got one already!"

# Exclamation marks series #6: Remove n exclamation marks in the sentence from left to right
def remove(st, n):
    count = 0
    while count < n:
        ind = st.find("!")
        if ind == -1:
            break
        st = st[:ind] + st[ind+1:]
        count += 1
    return st

# get ascii value of character
def get_ascii(ch : str) -> int:
    return ord(ch)

# Exclamation marks series #4: Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string
def remove(st):
    return st.replace("!", "") + "!"

# A Strange Trip to the Market
def is_loch_ness_monster(string):
    return "three fifty" in string or "3.50" in string or "three fifdy" in string or "tree fiddy" in string

# Smallest unused ID
def next_id(arr):
    sorted_arr = sorted(arr)
    sorted_arr = list(set(sorted_arr))

    new_sorted_arr = []
    for i in range(len(sorted_arr)):
        if (sorted_arr[i] >= 0):
            new_sorted_arr.append(sorted_arr[i])

    for y in range(len(new_sorted_arr)):
        if (new_sorted_arr[y] != y):
            return y
    return len(new_sorted_arr)

# Closest elevator
def elevator(left, right, call):
    return 'right' if abs(call-right) <= abs(call-left) else 'left'

# Compare within margin
def close_compare(a, b, margin=0):
    if abs(a - b) <= margin: return 0
    elif a < b: return -1
    return 1

# Tip Calculator
import math
def calculate_tip(amount, rating):
    rating = rating.lower()
    match rating:
        case "terrible": return 0
        case "poor": return math.ceil(amount*.05)
        case "good": return math.ceil(amount*.1)
        case "great": return math.ceil(amount*.15)
        case "excellent": return math.ceil(amount*.2)
    return 'Rating not recognised'

# Who is going to pay for the wall?
def who_is_paying(name):
    return [name, name[:2]] if [name, name[:2]][0] != [name, name[:2]][1] else [name]

# Geometry Basics: Distance between points in 2D
import math
def distance_between_points(a, b):
    return math.dist([a.x, a.y], [b.x, b.y])

# Are arrow functions odd?
def odds(value):
    return [i for i in value if i%2 == 1]

# Collatz Conjecture (3n+1)
def hotpo(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

# BASIC: Making Six Toast.
def six_toast(num):
    return num - 6 if num >= 6 else 6 - num

# simple calculator
def calculator(x,y,op):
    try:
        x, y = int(x), int(y)
    except:
        return "unknown value"
    
    
    match op:
        case "+": return x+y
        case "-": return x-y
        case "*": return x*y
        case "/": return x/y
    return "unknown value"

# Is there a vowel in there?
def is_vow(inp):
    return [chr(i) if chr(i) in 'aeiou' else i for i in inp]

# Unexpected parsing
def get_status(is_busy):
    return {"status": "busy"} if is_busy else {"status": "available"}

# Thinkful - Number Drills: Blue and red marbles
def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    return (blue_start - blue_pulled) / (blue_start - blue_pulled + red_start - red_pulled)

# Find the Integral
def integrate(coefficient, exponent):
    return f"{int(coefficient / (exponent+1))}x^{int(coefficient / int(coefficient / (exponent+1)))}"

# ASCII Total
def uni_total(s):
    return sum([ord(i) for i in s])

# Did she say hallo?
def validate_hello(greetings):
    greetings = greetings.lower()
    greetings_list = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]  # List of greetings

    for greeting in greetings_list:
        if greeting in greetings:
            return True
    return False

# validate code with simple regex
def validate_code(code):
    return str(code)[0] in "123"

# For UFC Fans (Total Beginners): Conor McGregor vs George Saint Pierre
def quote(fighter):
    return "I'd like to take this chance to apologize.. To absolutely NOBODY!" if fighter.lower() == "conor mcgregor" else "I am not impressed by your performance."

# Duck Duck Goose
def duck_duck_goose(players, goose):
    return players[goose%len(players)-1].name

# Template Strings
def temple_strings(obj, feature): 
    return obj + " are " + feature

# Who ate the cookie?
def cookie(x):
    if type(x) == str: return"Who ate the last cookie? It was Zach!"
    if type(x) == int or type(x) == float: return "Who ate the last cookie? It was Monica!"
    return "Who ate the last cookie? It was the dog!"

# Get number from string
def get_number_from_string(st):
    return int("".join([i for i in st if i in "0123456789"]))

# Quadratic Coefficients Solver
def quadratic(x1, x2):
    return (1, -(x1+x2), x1*x2)

# Localize The Barycenter of a Triangle
def bar_triang(point_a, point_b, point_c): 
    return [round((point_a[0] + point_b[0] + point_c[0]) / 3, 4), round((point_a[1] + point_b[1] + point_c[1]) / 3, 4)]

# Switch/Case - Bug Fixing #6
def eval_object(v):
    match v["operation"]:
        case "+":
            return v["a"] + v["b"]
        case "-":
            return v["a"] - v["b"]
        case "/":
            return v["a"] / v["b"]
        case "*":
            return v["a"] * v["b"]
        case "%":
            return v["a"] % v["b"]
        case "**":
            return v["a"] ** v["b"]
        case _:
            return 1
        
# Draw stairs
def draw_stairs(n):
    start = 1
    res = ""
    
    for i in range(n-1):
        res+=f"I\n{''.join([' ' for _ in range(start)])}"
        start += 1
    res += "I"
    return res
# or
def draw_stairs(n):
    return "\n".join([f"{' ' * i}I" for i in range(n)])

# Count the number of cubes with paint on
def count_squares(n):
    return (n + 1)**3 - (n - 1)**3

# Parse float
def parse_float(string):
    try:
        return float(string)
    except:
        return None
    
# Wilson primes
def am_i_wilson(n):
    return n in [5, 13, 563]

# Power
def number_to_pwr(number, p):
    result = 1
    for _ in range(p): result *= number
    return result

# Flick Switch
def flick_switch(lst):
    res = []
    start = True
    
    for i in lst:
        if i == "flick": 
            start = not start  
        res.append(start) 
    
    return res

# Enumerable Magic #1 - True for All?
def all(sequence, func):
    for element in sequence:
        if not func(element):
            return False
    return True

# Grader
def grader(score):
    if score > 1 or score < 0.6: return "F"
    elif score >= .9: return "A"
    elif score >= .8: return "B"
    elif score >= .7: return "C"
    elif score >= .6: return "D"

# Pirates!! Are the Cannons ready!??
def cannons_ready(gunners):
    for i in gunners.values():
        if i.lower() == "nay": return 'Shiver me timbers!'
    return "Fire!"

# Is your period late?
from datetime import *
def period_is_late(last,today,cycle_length):
    return last + timedelta(days = cycle_length) < today

# 8kyu interpreters: HQ9+
def HQ9(code):
    if code == "H":
        return "Hello World!"
    if code == "Q":
        return "Q"
    if code == "9":
        result = ""
        for n in range(99,2,-1):
            result += f"{n} bottles of beer on the wall, {n} bottles of beer.\nTake one down and pass it around, {n-1} bottles of beer on the wall.\n"
        result += "2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall."
        return result
    return None

# UEFA EURO 2016
def uefa_euro_2016(teams, scores):
    if scores[0] > scores[1]: return f"At match {teams[0]} - {teams[1]}, {teams[0]} won!"
    elif scores[1] > scores[0]: return f"At match {teams[0]} - {teams[1]}, {teams[1]} won!"
    return f"At match {teams[0]} - {teams[1]}, teams played draw."

# Classy Extentions
# from preloaded import Animal

# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} meows."
    
# Barking mad
class Dog ():
    def __init__(self, breed):
        self.breed = breed
    
    def bark(self):
        return "Woof"
    

snoopy = Dog("Beagle")

snoopy.bark = lambda: "Woof"

scoobydoo = Dog("Great Dane")

# They say that only the name is long enough to attract attention. They also said that only a simple Kata will have someone to solve it. This is a sadly story #1: Are they opposite?
def is_opposite(s1,s2):
    return "".join([i.swapcase() for i in s1]) == s2 if s1 else False

# Is the date today
from datetime import datetime

def is_today(date: datetime) -> bool:
    return date.date() == datetime.today().date()

# Training JS #18: Methods of String object--concat() split() and its good friend join()
def split_and_merge(string, sp):
    return ' '.join(sp.join(word) for word in string.split())

# Ensure question
def ensure_question(s):
    if not s: return "?"
    return s+"?" if s[-1]!="?" else s

# pick a set of first elements
def first(*args):
    if len(args) == 2: 
        seq, n = args[0], args[1]
        
        if n==0: return []
        return seq[:n] if len(seq) > n else seq
    return [args[0][0]]

# For Twins: 2. Math operations
def ice_brick_volume(radius, bottle_length, rim_length):
    height = bottle_length - rim_length
    side = 2 * radius
    volume = side * side * height
    
    return volume/2

# Find the Slope
def find_slope(points):
    a, b, c, d = points
    
    if c - a == 0:
        return "undefined"
    
    slope = (d - b) // (c - a)
    return str(int(slope))

# Fix the Bugs (Syntax) - My First Kata
def my_first_kata(a,b):
    if type(a) != int or type(b) != int: return False
    else:
        return a % b + b % a
    
# NBA full 48 minutes average
def nba_extrap(ppg, mpg):
    return round(ppg * (48 / mpg), 1)

# easy logs
import math

def logs(x, a, b):
    return (math.log(a) + math.log(b))/math.log(x);

# Fuel Calculator: Total Cost
def fuel_price(litres, price_per_litre):
    return round(litres * (price_per_litre - min(25, (litres // 2) * 5) / 100), 2)

# Online RPG: player to qualifying stage?
def playerRankUp(pts):
     return "Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up." if pts >= 100 else False

# Points of Reflection
def symmetric_point(p, q):
    return [2 * q[0] - p[0], 2 * q[1] - p[1]]

# Freudian translator
def to_freud(sentence):
    return "" if not sentence or sentence == " " else " ".join(["gender" for _ in range(len(sentence.split(" ")))])

# Grasshopper - Terminal Game #1
class Hero(object):
    def __init__(*args):
        self = args[0]
        if (len(args))==2: self.name = args[1]
        else: self.name = "Hero"
        self.position = "00"
        self.health = 100
        self.damage = 5
        self.experience = 0

# Finish Guess the Number Game
# class Guesser:
#     def __init__(self, number, lives):
#         self.number = number
#         self.lives = lives

#     def guess(self,n):
#         if self.lives == 0:
#             raise Except('Omae wa mo shindeiru')
#         elif n  == self.number:
#             return True
#         self.lives -= 1
#         return False

# Merging sorted integer arrays (without duplicates)
def merge_arrays(first, second): 
    return list(sorted(list(set(first+second))))

# Return Two Highest Values in List
def two_highest(arg1):
    if len(arg1) >= 3: return [list(sorted(list(set(arg1))))[-1], list(sorted(list(set(arg1))))[-2]]
    return [max(arg1)] if arg1 else []

# How do I compare numbers?
def what_is(x):
    if x == 42: return 'everything'
    elif x == 42 * 42: return 'everything squared'
    return 'nothing'

# Safen User Input Part I - htmlspecialchars
def html_special_chars(data): 
    res = ""
    for i in data:
        if i not in '<>"&': res+=i
        else:
            if i == "<": res+= "&lt;"
            elif i == ">": res+= "&gt;"
            elif i == '"': res+= "&quot;"
            else: res += "&amp;"
    return res

# Evil or Odious
def evil(n):
    return "It's Evil!" if str(bin(n)).count("1")%2 != 1 else "It's Odious!"

# Calculate Price Excluding VAT
def excluding_vat_price(price):
    return price/1.15 if price else -1

# Name Your Python!
class Python:
    def __init__(self, name):
        self.name = name

# Crash Override
first_fake_name = {
    "A": "Alpha",
    "B": "Beta",
    "C": "Cache",
    "D": "Data",
    "E": "Energy",
    "F": "Function",
    "G": "Glitch",
    "H": "Half-life",
    "I": "Ice",
    "J": "Java",
    "K": "Keystroke",
    "L": "Logic",
    "M": "Malware",
    "N": "Nagware",
    "O": "OS",
    "P": "Phishing",
    "Q": "Quantum",
    "R": "RAD",
    "S": "Strike",
    "T": "Trojan",
    "U": "Ultraviolet",
    "V": "Vanilla",
    "W": "WiFi",
    "X": "Xerox",
    "Y": "Y",
    "Z": "Zero"
}

sur_fake_name = {
    "A": "Analogue",
    "B": "Bomb",
    "C": "Catalyst",
    "D": "Discharge",
    "E": "Electron",
    "F": "Faraday",
    "G": "Gig",
    "H": "Hacker",
    "I": "IP",
    "J": "Jabber",
    "K": "Killer",
    "L": "Lazer",
    "M": "Mike",
    "N": "n00b",
    "O": "Overclock",
    "P": "Payload",
    "Q": "Quark",
    "R": "Roy",
    "S": "Spy",
    "T": "T-Rex",
    "U": "Unit",
    "V": "Virus",
    "W": "Worm",
    "X": "X",
    "Y": "Yob",
    "Z": "Zombie"
}

def alias_gen(firstname, surname):
    first_letter_of_firstname = firstname[0].upper()
    first_letter_of_surname = surname[0].upper()

    if not first_letter_of_firstname.isdigit() and not first_letter_of_surname.isdigit():
        name = first_fake_name.get(first_letter_of_firstname)
        sur = sur_fake_name.get(first_letter_of_surname)

        if name and sur:
            return f"{name} {sur}"
        else:
            return "Your name must start with a letter from A - Z."
    else:
        return "Your name must start with a letter from A - Z."
    
# Neutralisation
def neutralise(s1, s2):
    res = ""
    for i in range(len(s1)):
        if s1[i] != s2[i]: res += "0"
        else: res += s1[i]
    return res

# Polish alphabet
def correct_polish_letters(st): 
    all = {
        "ą" : "a",
        "ć" : "c",
        "ę" : "e",
        "ł" : "l",
        "ń" : "n",
        "ó" : "o",
        "ś" : "s",
        "ź" : "z",
        "ż" :  "z"
    }
    res = ""
    for i in st:
        if i not in all.keys(): res+=i
        else: res+=all[i]
    return res

# Semi-Optional
def wrap(value):
    wrapper_obj = {}
    wrapper_obj["value"] = value
    return wrapper_obj

# Logical calculator
def logical_calc(array, op):
    if op == "AND": return array.count(True) == len(array)
    elif op == "OR": return True in array
    elif op == "XOR": return array.count(True) % 2 == 1

# Grasshopper - Bug Squashing
# from preloaded import *

# health = 100
# position = 0
# coins = 0

# def main():
#     roll_dice()
#     move()
#     combat()
#     get_coins()
#     buy_health()
#     print_status()

# Age Range Compatibility Equation
def dating_range(age):
    if age <= 14: return f"{int(age - 0.10 * age)}-{int(age + 0.10 * age)}"
    else: return f"{int(age/2 + 7)}-{int((age-7) *2)}"

# Job Matching #1
def match(candidate, job):
    return candidate['min_salary'] * 0.9 <= job['max_salary']

# Grasshopper - Create the rooms
room1 = {"name": "", "description": "", "completed": False}
room2 = {"name": "", "description": "", "completed": False}
room3 = {"name": "", "description": "", "completed": False}

rooms = {0: room1, 1: room2, 2: room3}

# Simple Fun #261: Whose Move
def whose_move(last_player, win):
    if win: return last_player
    else: return "white" if last_player == "black" else "black"

# Days in the year
def year_days(year):
    return f"{year} has 366 days" if check(year) else f"{year} has 365 days"
    
    
def check(y):
    if y%4 == 0:
        if y%100 == 0:
            if y%400 == 0:
                return True
            return False
        return True
    return False

# Enumerable Magic #20 - Cascading Subsets
def each_cons(lst, n):
    return [lst[i:i+n] for i in range(len(lst) - n + 1)]

# Thinkful - Dictionary drills: Order filler
def fillable(stock, merch, n):
    if merch in stock.keys(): return True if stock[merch] >= n else False
    return False

# Be Concise IV - Index of an element in an array
find=lambda a,e:a.index(e) if e in a else "Not found"

# Sort My Textbooks
def sorter(textbooks):
    return sorted(textbooks,key=str.lower)

# Playing with cubes II
class Cube(object):
    def __init__(self, side=0):
        self.__side = side
    
    def get_side(self):
        return self.__side if self.__side > 0 else self.__side * -1

    def set_side(self, new_side):
        self.__side = new_side

# Be Concise I - The Ternary Operator
def describe_age(a): 
    return f"You're a(n) {a<13 and 'kid' or a<18 and 'teenager' or a<65 and 'adult' or 'elderly'}"

# Heads and Legs
def animals(heads, legs):
    if heads < 0 or legs < 0:
        return "No solutions"
    
    cows = (legs - 2 * heads) / 2
    chickens = heads - cows
    
    if cows.is_integer() and chickens.is_integer() and cows >= 0 and chickens >= 0:
        return (int(chickens), int(cows))
    else:
        return "No solutions"
    
# How much water do I need?
def how_much_water(water, load, clothes):
    if clothes < load:
        return 'Not enough clothes'
    if clothes > 2 * load:
        return 'Too much clothes'
    
    water_needed = water * (1.1 ** (clothes - load))
    return round(water_needed, 2)

# For Twins: 1. Types
def type_validation(variable, _type): 
    return _type in str(type(variable))

# Grasshopper - Terminal Game Turn Function
# def do_turn():
#     roll_dice()
#     move()
#     combat()
#     get_coins()
#     buy_health()
#     print_status()

# Floating point comparison
def approx_equals(a, b, tolerance=0.001):
    return abs(a - b) <= tolerance

# Collinearity
def collinearity(x1, y1, x2, y2):
    return x1*y2 == x2*y1

# Are there any arrows left?
def any_arrows(quiver):
    return any(not arrow.get('damaged', False) for arrow in quiver)

# Simple Fun #352: Reagent Formula
def isValid(formula):
    if (1 in formula and 2 in formula):
        return False
    
    if (3 in formula and 4 in formula):
        return False
    
    if (5 in formula) != (6 in formula):
        return False
    
    if not (7 in formula or 8 in formula):
        return False
    
    return True

# What's up next?
from itertools import count

def next_item(sequence, item):
    try:
        iterator = iter(sequence)
        prev_item = None
        for current_item in iterator:
            if prev_item == item:
                return current_item
            prev_item = current_item
    except StopIteration:
        pass
    return None

# Add new item (collections are passed by reference)
def AddExtra(listOfNumbers):
    return listOfNumbers + [1]

# Filtering even numbers (Bug Fixes)
def kata_13_december(lst): 
    return [i for i in lst if i%2!=0]

# Aspect Ratio Cropping - Part 1
import math

def aspect_ratio(x: int, y: int):
    return (math.ceil(y * (16 / 9)), y)

# Total pressure calculation
def solution(M1, M2, m1, m2, V, T_C):
    R = 0.082
    T_K = T_C + 273.15
    n1 = m1 / M1
    n2 = m2 / M2
    P_total = (n1 + n2) * R * T_K / V
    return P_total

# Geometry Basics: Circle Circumference in 2D
import math

def circle_circumference(circle):
    circumference = (circle.radius * 2 * math.pi)
    return circumference

# Up and down, the string grows
STRANGE_STRING = 'ß'

# Fix the loop!
def list_animals(animals):
    lst = ''
    for i in range(len(animals)):
        lst += str(i + 1) + '. ' + animals[i] + '\n'
    return lst

# Byte me!
from sys import getsizeof as total_bytes

# Training JS #32: methods of Math---round() ceil() and floor()
import math

def round_it(n):
    splitted_number = str(n).split(".")
    if len(splitted_number[0]) > len(splitted_number[1]):
        return math.floor(n)
    elif len(splitted_number[0]) < len(splitted_number[1]):
        return math.ceil(n)
    else:
        return round(n)
    
# Invalid Login - Bug Fixing #11
# def validate(username, password):
#     database = Database()
#     return database.login(username, password)

# Geometry Basics: Circle Area in 2D
def circle_area(circle):
    return circle.radius**2 * 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482

# Generate user links
from urllib.parse import quote

def generate_link(user: str) -> str:
    return f"http://www.codewars.com/users/{quote(user)}"

# Pole Vault Starting Marks
def starting_mark(height):
    return round(9.45 + (10.67 - 9.45) / (1.83 - 1.52) * (height - 1.52), 2)

# Greek Sort
def greek_comparator(lhs, rhs):
  greek_alphabet = (
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')
  return greek_alphabet.index(lhs) - greek_alphabet.index(rhs)

# Find the force of gravity between two objects
def solution(arr_val, arr_unit) :
    G = 6.67e-11
    

    weight = {
        "kg": 1,
        "g" : 0.001,
        "mg" : 1e-6,
        "μg" : 1e-9,
        "lb" : 0.453592
    }
    distance = {
        "m" : 1,
        "cm" : .01,
        "mm" : .001,
        "μm" : 1e-6,
        "ft" : 0.3048
    }
    
    M1 = arr_val[0] * weight[arr_unit[0]]
    M2 = arr_val[1] * weight[arr_unit[1]]
    D = arr_val[2] * distance[arr_unit[2]]
    
    return G * M1 * M2 / D**2
    
# Simple Change Machine
def change_me(money): 
    if money == "£5": return ("20p " * 25).strip()
    elif money == "£2": return ("20p " * 10).strip()
    elif money == "£1": return ("20p " * 5).strip()
    elif money == "50p": return (("20p " * 2) + "10p").strip()
    elif money == "20p": return ("10p " * 2).strip()
    else: return money
    
# Enumerable Magic #30 - Split that Array!
def partition(arr, classifier_method):
    return ([x for x in arr if classifier_method(x)],
           [x for x in arr if not classifier_method(x)])

# Vexing Vanishing Values
def mul_by_n(lst, n):
    return [i*n for i in lst]

# Circles in Polygons
import math

def circle_diameter(sides, side_length):
    if sides < 3:
        raise ValueError
    
    return side_length / math.tan(math.pi / sides)