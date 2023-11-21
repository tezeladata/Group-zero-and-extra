#What is between?
def between(a,b):
    numbers=[]
    for i in range(a, b+1):
        numbers.append(i)
    return numbers

#Do I get a bonus?
def bonus_time(salary, bonus):
    if bonus==True:
        return "$" + str(salary*10)
    else:
        return "$" + str(salary)
    
#Cat years, Dog years
def human_years_cat_years_dog_years(human_years):
    if human_years==1:
        return [human_years, human_years+14, human_years+14]
    elif human_years==2:
        return [human_years, human_years+22, human_years+22]
    else:
        return [human_years, human_years*4+16, human_years*5+14]
    
#altERnaTIng cAsE <=> ALTerNAtiNG CaSe
def to_alternating_case(string):
    sentence=""
    for i in string:
        if i.isupper():
            sentence+=i.lower()
        elif i.islower():
            sentence+=i.upper()
        else:
            sentence+=i
    return sentence
        
#Powers of 2
def powers_of_two(n):
    powers=[]
    for i in range(0, n+1):
        powers.append(2**i)
    return powers

#Correct the mistakes of the character recognition software
def correct(s):
    a=s.replace("5", "S").replace("0", "O").replace("1", "I")
    return a

#Is it a palindrome?
def is_palindrome(s):
    return s.lower()==s[::-1].lower()

#Student's Final Grade
def final_grade(exam, projects):
    if exam>90 or projects>10:
        return 100
    elif exam>75 and projects>=5:
        return 90
    elif exam>50 and projects>=2:
        return 75
    else:
        return 0

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

