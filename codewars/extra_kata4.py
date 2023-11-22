#Count Odd Numbers below n
def odd_count(n):
    return int(n/2)

#I love you, a little , a lot, passionately ... not at all
def how_much_i_love_you(nb_petals):
    n=nb_petals % 6
    if n==1:
        return "I love you"
    elif n==2:
        return "a little"
    elif n==3:
        return "a lot"
    elif n==4:
        return "passionately"
    elif n==5:
        return "madly"
    elif n==0:
        return "not at all"
    
#Unfinished Loop - Bug Fixing #1
def create_array(n):
    res=[]
    i=1
    while i<=n: 
        res+=[i]
        i+=1
    return res

#Sort and Star
def two_sort(array):
    sentence=""
    array=sorted(array)
    first=array[0]
    for letter in first:
        sentence+=letter + "***"
    return sentence[:-3]

#My head is at the wrong end!
def fix_the_meerkat(arr):
    return arr[::-1]

#Short Long Short
def solution(a, b):
    if len(a)<len(b):
        c=a+b+a
        return c
    elif len(b)<len(a):
        c=b+a+b
        return c
    
#Find Multiples of a Number
def find_multiples(integer, limit):
    numbers=[]
    for i in range(integer, limit+1, integer):
            numbers.append(i)
    return numbers

#Vowel remover
def shortcut( s ):
    for i in ["a", "e", "i", "o", "u"]:
         if i in s:   
            s=s.replace(i, "")
    return s

#Drink about
def people_with_age_drink(age):
    if age<14:
        return "drink toddy"
    if 14<=age<18:
        return "drink coke"
    if 18<=age<21:
        return "drink beer"
    elif age>=21:
        return "drink whisky"
    
#Filter out the geese
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    not_geese=[]
    for element in birds:
        if element not in geese:
            not_geese.append(element)
    return not_geese