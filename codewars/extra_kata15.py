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