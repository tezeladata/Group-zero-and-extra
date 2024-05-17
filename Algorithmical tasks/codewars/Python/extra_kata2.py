#Expressions Matter
def expression_matter(a, b, c):
    cases=[a+b+c]
    cases.append(a*b*c)
    cases.append((a*b)+c)
    cases.append((a+b)*c)
    cases.append(a+(b*c))
    cases.append(a*(b+c))
    return max(cases)

#Grasshopper - Messi Goals
la_liga_goals=43
champions_league_goals=10
copa_del_rey_goals=5

total_goals=la_liga_goals+champions_league_goals+copa_del_rey_goals

#Sum The Strings
def sum_str(a, b):
    if a!="" and b!="":
        c=int(a)+int(b)
        return str(c)
    elif a=="" and b!="":
        return str(b)
    elif a!="" and b=="":
        return str(a)
    else:
        return str(0)
    
#Difference of Volumes of Cuboids
def find_difference(a, b):
    volume_a=1
    volume_b=1
    for element in a:
        volume_a*=element
    for element in b:
        volume_b*=element
    if volume_a>volume_b:
        return volume_a-volume_b
    else:
        return volume_b-volume_a
    
#Welcome!
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
    
#Basic variable assignment
a = "code"
b = "wa.rs"
name = a + b

#Reverse List Order
def reverse_list(l):
    return l[::-1]

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

#Get Nth Even Number
def nth_even(n):
    return n*2-2

#Remove duplicates from list
def distinct(seq):
    answer=[]
    for i in seq:
        if i not in answer:
            answer.append(i)
    return answer

#5 without numbers !!
def unusual_five():
    return len("abcde")

#Merge two sorted arrays into one
def merge_arrays(arr1, arr2):
    a=sorted(set(arr1+arr2))
    return a

#Super Duper Easy
def problem(a):
    if type(a)!=str:
        return a*50+6
    else:
        return "Error"