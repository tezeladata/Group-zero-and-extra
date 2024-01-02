#Factorial
def factorial(n):
    factorial=1
    if 0<n<=12:
        for i in range(1, n+1):
            factorial*=i
        return factorial
    else:
        if n==0:
            return 1
        elif n<0:
            raise ValueError
        else:
            raise ValueError
        
#Find the capitals
def capitals(word):
    word=list(word)
    index=[]
    i=0
    for letter in word:
        if letter.isupper():
            index.append(i)
        i+=1
    return index

#Small enough? - Beginner
def small_enough(array, limit):
    for i in array:
        if max(array)<=limit:
            return True
        else:
            return False
        
#Summing a number's digits
def sum_digits(number):
    if number<0:
        number*=-1
    number=str(number)
    count=0
    for i in number:
        count+=int(i)
    return count

#Leap Years
def is_leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
#Sum of angles
def angle(n):
    return 180*(n-2)

#Two Oldest Ages
def two_oldest_ages(ages):
    new=[]
    new.append(max(ages))
    ages.remove(max(ages))
    new.append(max(ages))
    if new[0]>new[1]:
        new2=[]
        new2.append(new[1])
        new2.append(new[0])
        return new2
    else:
        return new
    
#Find the middle element
def gimme(input_array):
    return input_array.index(sorted(input_array)[1])

#Simple Fun 176: Reverse Letter
def reverse_letter(string):
    new_str=""
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for i in string:
        if i in alphabet:
            new_str+=i
    return new_str[::-1]

#Round up to the next multiple of 5
def round_to_next5(n):
    if n%5==0:
        return n
    else:
        if n%5==1:
            return n+4
        elif n%5==2:
            return n+3
        elif n%5==3:
            return n+2
        elif n%5==4:
            return n+1
        
#Maximum Multiple
def max_multiple(divisor, bound):
    new=[]
    for i in range(divisor, bound+1):
        if i%divisor==0:
            new.append(i)
    return max(new)

#The Coupon Code
def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if not isinstance(entered_code, str) or not isinstance(correct_code, str):
        return False
    months={
        "January": 1,
        "February": 2, 
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6, 
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10, 
        "November": 11,
        "December": 12
    }
    if entered_code==correct_code:
        current=current_date.split(", ")
        expiration=expiration_date.split(", ")
        curyear=int(current[-1])
        expyear=int(expiration[-1])
        if curyear>expyear:
            return False
        elif curyear<expyear:
            return True
        else:
            cm, cd = current[0].split()
            em, ed = expiration[0].split()
            if months[cm]<months[em]:
                return True
            elif months[em]<months[cm]:
                return False
            else:
                return int(cd) <= int(ed)
    else:
        return False

#No oddities here
def no_odds(values):
    if values==[]:
        return []
    else:
        return [x for x in values if x%2==0]
    
#Alternate capitalization
def capitalize(s):
    word=""
    last=[]
    for i in range(0, len(s)):
        if i%2==0:
            word=word+s[i].upper()
        else:
            word=word+s[i]
    last.append(word)
    last.append(word.swapcase())
    return last

#Triangular Treasure
def triangular(n):
    if n<0:
        return 0
    else:
        return n*(n+1)//2
    
#Maximum Length Difference
def mxdiflg(a1, a2):
    max=-1
    for i in a1:
        for x in a2:
            c= abs(len(i) - len(x))
            if c>max:
                max=c
    return max

#Fix string case
def solve(s):
    count_of_lower=0
    count_of_upper=0
    for i in s:
        if i==i.upper():
            count_of_upper+=1
        else:
            count_of_lower+=1
    if count_of_lower==count_of_upper:
        return s.lower()
    elif count_of_lower>count_of_upper:
        return s.lower()
    elif count_of_lower<count_of_upper:
        return s.upper()
    
#Are the numbers in order?
def in_asc_order(arr):
    return arr==sorted(arr)

#Check the exam
def check_exam(arr1,arr2):
    score=0
    for i in range(0, 4):
        if arr2[i]==arr1[i]:
            score+=4
        elif arr2[i]=="":
            pass
        elif arr2[i]!=arr1[i]:
            score-=1
    if score>0:
        return score
    elif score<0:
        return 0
    
#Number of Decimal Digits
def digits(n):
    n=str(n)
    a=len(n)
    return a

#Two fighters, one winner.
def declare_winner(fighter1, fighter2, first_attacker):
    if fighter1.name==first_attacker:
        attacker, defender = fighter1, fighter2
    else:
        attacker, defender = fighter2, fighter1
    while True:
        defender.health-=attacker.damage_per_attack
        if defender.health <=0:
            return attacker.name
        else:
            attacker, defender = defender, attacker

#Deodorant Evaporator
import math
def evaporator(content, evap_per_day, threshold):
    return math.ceil(math.log(threshold/100)/ math.log(1.0 - evap_per_day / 100))

#Flatten and sort an array
def flatten_and_sort(a):
    return sorted([i for s in a for i in s])
#or
def flatten_and_sort(array):
    new=[]
    for element in array:
        new+=element
    return sorted(new)

#Form The Minimum
def min_value(digits):
    new=""
    for number in sorted(digits):
        number=str(number)
        if number not in new:
            new+=number
    return int(new)

#Fizz Buzz
def fizzbuzz(n):
    new=[]
    for i in range(1, n+1):
        if i%3==0 and i%5!=0:
            new.append("Fizz")
        elif i%5==0 and i%3!=0:
            new.append("Buzz")
        elif i%15==0:
            new.append("FizzBuzz")
        else:
            new.append(i)
    return new

#Factorial
def factorial(n):
    ans=1
    for i in range(1, n+1):
        ans*=i
    return ans

#Power of two
def power_of_two(x):
    current_number = 0
    counter = 0
    while current_number <= x:
        current_number = 2**counter
        counter+=1
        if current_number == x:
            return True
    return False   

#Sum of Minimums!
def sum_of_minimums(numbers):
    a=0
    for i in range(len(numbers)):
        a+=min(numbers[i])
    return a