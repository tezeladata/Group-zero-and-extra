#Sum of odd numbers
def row_sum_odd_numbers(n):
    return n**3

#Money, Money, Money
def calculate_years(principal, interest, tax, desired):
    count=0
    while principal<desired:
        principal+=(interest*principal) * (1-tax)
        count+=1
    return count

#Remove anchor from URL
def remove_url_anchor(url):
    for i in url:
        if "#" in url:
            a=url.index("#")
            return url[0:a]
        else:
            return url
        
#Don't give me five!
def dont_give_me_five(start,end):
    new=[]
    for i in range(start, end+1):
        if "5" not in str(i):
            new.append(i)
        
    return len(new)

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