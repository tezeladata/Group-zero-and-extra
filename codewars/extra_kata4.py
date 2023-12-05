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

#Capitalization and Mutability
def capitalize_word (word):
    return word[0].upper() + word[1:]

#What's the real floor?
def get_real_floor(n):
    if n==0:
        return 0
    elif n==1:
        return 0
    elif 2<=n<13:
        return n-1
    elif n<0:
        return n
    else:
        return n-2
    
#Grasshopper - If/else syntax debug
def check_alive(health):
    if health <= 0:
        return False
    else:
        return True
    
#Name Shuffler
def name_shuffler(str_):
    name=str_.split(" ")
    return name[1] + " " + name[0]

#Find numbers which are divisible by given number
def divisible_by(numbers, divisor):
    answer=[]
    for i in numbers:
        if i%divisor==0:
            answer.append(i)
    return answer

#How many lightsabers do you own?
def how_many_light_sabers_do_you_own(name=""):
    if name=="Zach":
        return 18
    else:
        return 0
    
#Stringy Strings
def stringy(size):
    answer=""
    for i in range(size):
        if i%2==0:
            answer+="1"
        else:
            answer+="0"
    return answer

#Plural
def plural(n):
    if n==0:
        return True
    elif n==1:
        return False
    else:
        return True

#Training JS #7: if..else and ternary operator
def sale_hotdogs(n):
    if n==0:
        return 0
    elif n<5:
        return n*100
    elif 5<=n<10:
        return n*95
    else:
        return n*90

#Grasshopper - Basic Function Fixer
def add_five(num):
    total = num + 5
    return total

#Lario and Muigi Pipe Problem
def pipe_fix(nums):
    new=[]
    for i in range(nums[0], nums[-1]+1):
        new.append(i)
    return new

#Multiplication table for number
def multi_table(number):
    table=''
    for i in range(1, 11):
        z=i*number
        table+= "{} * {} = {}\n".format(i, number, z)
    return table.strip("\n")