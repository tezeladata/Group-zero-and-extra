#Predict your age!
import math
def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    new=[age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    new2=[]
    for num in new:
        num**=2
        new2.append(num)
    a=sum(new2)
    b=a**0.5
    b/=2
    return math.floor(b)

#Row Weights
def row_weights(array):
    team1=0
    team2=0
    for i in range(len(array)):
        if i%2==0:
            team2+=array[i]
        else:
            team1+=array[i]
    return team2, team1

#Sum of numbers from 0 to N
def show_sequence(n):
    ans="0"
    count=0
    for i in range(1, n+1):
        ans+="+{}".format(i)
        count+=i
    ans+=" = {}".format(count)
    if n==0:
        return "0=0"
    elif n<0:
        return "{}<0".format(n)
    else:
        return ans
    
#Greet Me
def greet(name): 
    name=name.lower()
    name=list(name)
    name[0]=name[0].upper()
    new=""
    for i in name:
        new+=i
    return "Hello {}!".format(new)

#Remove duplicate words
def remove_duplicate_words(s):
    s=s.split(" ")
    sentence=[]
    for item in s:
        if item not in sentence:
            sentence.append(item)
    return " ".join(sentence)
    
#Sum of Cubes
def sum_cubes(n):
    new=0
    for i in range(1, n+1):
        new+=i**3
    return new

#Sorted? yes? no? how?
def is_sorted_and_how(arr):
    if arr==sorted(arr):
        return "yes, ascending"
    elif arr==sorted(arr, reverse=True):
        return "yes, descending"
    else:
        return "no"
    
#Digits explosion
def explode(s):
    s=list(s)
    new=""
    for num in s:
        new+=str(num)*int(num)
    return new

#Bumps in the Road
def bumps(road):
    road=list(road)
    bump=road.count("n")
    if bump<=15:
        return "Woohoo!"
    else:
        return "Car Dead"
    
#Love vs friendship
def words_to_marks(s):
    value={
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
    count=0
    s=list(s)
    for char in s:
        count+=value[char]
    return count

#Greatest common divisor
import math
def mygcd(x, y):
    return math.gcd(x, y)
        
#Find the vowels
def vowel_indices(word):
    word = word.lower()
    vowels = ["a", "e", "i", "o", "u", "y"]
    list = []
    for index in range(len(word)):
        if word[index] in vowels:
            list.append(index + 1)
    return list

#Sort the Gift Code
def sort_gift_code(code):
    a=sorted(code)
    b=""
    for i in a:
        b+=i
    return b

#Sort array by string length
def sort_by_length(arr):
    return sorted(arr, key=len)

#Largest 5 digit number in a series
def solution(digits):
    res=0
    for iteration in range(len(digits)):
        if int(digits[iteration:iteration+5]) > res:
            res=int(digits[iteration:5+iteration])
    return res

#Alphabet war
def alphabet_war(fight):
    a={
        "w": 4,
        "p": 3,
        "b": 2,
        "s": 1
    }
    b={
        "m": 4,
        "q": 3,
        "d": 2,
        "z": 1
    }
    fight=list(fight)
    left=0
    right=0
    for e in fight:
        left+=a.get(e, 0)
        right+=b.get(e, 0)
    if left>right:
        return "Left side wins!"
    elif right>left:
        return "Right side wins!"
    elif right==left:
        return "Let's fight again!"
    
#Largest pair sum in array
def largest_pair_sum(numbers): 
    count=0
    count+=max(numbers)
    numbers.remove(max(numbers))
    count+=max(numbers)
    return count

#Switcheroo
def switcheroo(s):
    res=""
    for letter in s:
        if letter=="a":
            letter="b"
        elif letter=="b":
            letter="a"
        res+=letter
    return res

#Sum of Triangular Numbers
def sum_triangular_numbers(n):
    if n<0:
        return 0
    else:
        return (n*(n+1)*(n+2))/6
    
#Even numbers in an array
def even_numbers(arr,n):
    new=[]
    for num in arr:
        if num%2==0:
            new.append(num)
    return new[-n:]

#Filter the number
def filter_string(string):
    new=""
    for i in string:
        if i>="0" and i<="9":
            new+=i
    return int(new)

#Simple beads count
def count_red_beads(n):
    if n<2:
        return 0
    else:
        return (n-1)*2
    
#Boiled Eggs
import math
def cooking_time(eggs):
    a=math.ceil(eggs/8)
    return a*5

#Functional Addition
def add(n):
    return lambda x: x+n

#My Language Skills
def my_languages(results):
    new=[]
    for key, value in results.items():
        if value>=60:
            new.append(key)
    return sorted(new, key=lambda x: results[x], reverse=True)

#Sort arrays - 1
def sortme(names):
    return sorted(names)

#Speed Control
def gps(s, x):
    if len(x)<2:
        return 0
    else:
        numb=max(x[i] - x[i-1] for i in range(1, len(x)))
    return numb*3600.0/s

#Minimize Sum Of Array (Array Series #1)
def min_sum(arr):
    arr=sorted(arr)
    last_num=0
    for i in range(len(arr)//2):
        last_num+=arr[i]*arr[-i-1]
    return last_num

#Odd-Even String Sort
def sort_my_string(s):
    even=""
    odd=""
    for i in range(0, len(s), 2):
        even+=s[i]
    for i in range(1, len(s), 2):
        odd+=s[i]
    return "{} {}".format(even, odd)

#Maximum Triplet Sum (Array Series #7)
def max_tri_sum(numbers):
    numbers=set(numbers)
    numbers=list(numbers)
    a=0
    a+=max(numbers)
    numbers.remove(max(numbers))
    a+=max(numbers)
    numbers.remove(max(numbers))
    a+=max(numbers)
    return a