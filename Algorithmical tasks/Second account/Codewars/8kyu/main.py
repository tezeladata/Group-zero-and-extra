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