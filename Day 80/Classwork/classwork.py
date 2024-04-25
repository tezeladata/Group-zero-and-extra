# String ends with?
def solution(text, ending):
    return ending == text[-len(ending):]

# Find the stray number
def stray(arr):
    res = 0
    for num in arr:
        if arr.count(num) == 1:
            res+=num
    return res

# Leap Years
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
# Triangular Treasure
def triangular(n):
    if n > 0:
        return n*(n+1) // 2
    else:
        return 0
    
# Find the vowels
def vowel_indices(word):
    word = word.lower()
    vowels = ["a", "e", "i", "o", "u", "y"]
    res_list = []
    
    for i in range(1, len(word)+1):
        if word[i-1] in vowels:
            res_list.append(i)

    return res_list

# Tribonacci Sequence
def tribonacci(signature, n):
    
    if n==0:
        return []
    
    elif n==1:
        return [signature[0]]
    
    elif n==2:
        return signature[:2]
    
    else:
    
        num1 = signature[0]
        num2 = signature[1]
        num3 = signature[2]
    
        res_list = signature
    
        for i in range(1, n-2):
            num4 = num1 + num2 + num3
            num1 = num2
            num2 = num3
            num3 = num4
            res_list.append(num4)
    
        return res_list    
    
# Break camelCase
def solution(s):
    if s=="":
        return ""
    else:
        res_str = ""
        for i in s:
            if i == i.upper():
                res_str += f" {i}"
            else:
                res_str += i
        return res_str
    
# CamelCase Method
def camel_case(s):
    return "".join([word.capitalize() for word in s.split(" ")])

# The Hashtag Generator
def generate_hashtag(s):
    if s == "":
        return False
    else:
        res = "".join([word.capitalize() for word in s.split(" ")])
        res = f"#{res}"
        
        if len(res) > 140:
            return False
        else:
            return res
        
# Simple Pig Latin
def pig_it(text):
    text = text.split(" ")
    res = []
    
    for word in text:
        if word.isalpha():
            new_word = word[1:] + word[0] + "ay"
            res.append(new_word)
        else:
            res.append(word)
        
    return " ".join(res)

# Convert PascalCase string into snake_case
def to_underscore(string):
    if type(string) == int:
        return str(string)
    else:
        
        res_str = ""
    
        for i in string:
            if i == i.upper() and i.isalpha():
                res_str += f"_{i.lower()}"
            else:
                res_str += i
            
        return res_str[1:]
    
# Sort the odd
def sort_array(source_array):
    if source_array == []:
        return []
    else:
        odd = sorted(x for x in source_array if x%2!=0)
        
        for i in range(len(source_array)):
            if source_array[i]%2!=0:
                source_array[i]=odd.pop(0)
                
        return source_array        
    
# Collatz
def collatz(n):
    res = [n]
    
    while n>1:
        if n%2==0:
            n //= 2
        else:
            n = n*3 + 1
        res.append(n)
        
    if len(res) == 1:
        return str(res[0])
    else:
        return "->".join([str(x) for x in res])
    
# WeIrD StRiNg CaSe
def to_weird_case(words):
    res_list = []
    
    words = words.split(" ")
    
    for word in words:
        word_list = []
        for char in range(len(word)):
            if char%2==0:
                word_list.append(word[char].upper())
            else:
                word_list.append(word[char].lower())
        
        res_list.append("".join(word_list))
    return " ".join(res_list)

# Play with two Strings
def work_on_strings(a,b):
    list1 = list(a)
    list2 = list(b)
    
#   part1
    for i in range(len(list1)):
        for x in range(len(list2)):
            if list1[i].upper() == list2[x] or list1[i].lower() == list2[x]:
                list2[x] = list2[x].swapcase()
                
#   part2
    for x in range(len(list2)):
        for i in range(len(list1)):
            if list2[x].upper() == list1[i] or list2[x].lower() == list1[i]:
                list1[i] = list1[i].swapcase()

    return "".join(list1 + list2)