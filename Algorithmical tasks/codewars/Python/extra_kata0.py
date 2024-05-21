#maps
def maps(a):
    b=[]
    for num in a:
        a=num*2
        b.append(a)
    return b

#clock
def past(h, m, s):
    milisec=h*3600000 + m*60000 + s*1000
    return milisec

#school paperwork
def paperwork(n, m):
    if n<0 or m<0:
        result=0
        return result
    else:
        return n*m
    
#opposites atract
def lovefunc( flower1, flower2 ):
    if (flower1%2==0 and flower2%2!=0) or (flower1 %2!=0 and flower2 %2==0):
        return True
    return False
    
#simple multiplication
def simple_multiplication(number) :
    if number%2==0:
        return number*8
    elif number%2!=0:
        return number*9
#or
def simple_multiplication(number) :
    if number%2==0:
        return number*8
    else:
        return number*9
    
#MakeUpperCase
def make_upper_case(s):
    return s.upper()

#Sum Arrays
def sum_array(a):
    b=0
    for num in a:
        b+=num
    return b

#Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0]=="R" or name[0]=="r":
        return name + " plays banjo" 
    else:
        return name + " does not play banjo"
    
#Invert values
def invert(lst):
    b=[]
    for num in lst:
        num=num*(-1)
        b.append(num)
    return b

#Calculate average
def find_average(numbers):
    if len(numbers)!=0:
        return sum(numbers) / len(numbers)
    else:
        return 0
    
#Is he gonna survive?
def hero(bullets, dragons):
    if bullets/2 >= dragons:
        return True
    else:
        return False

#How good are you really?
def better_than_average(class_points, your_points):
    class_avg=sum(class_points) / len(class_points)
    if your_points > class_avg:
        return True
    else:
        return False
    
#Calculate BMI
def bmi(weight, height):
    your_bmi=(weight)/(height**2)
    if your_bmi<=18.5:
        return "Underweight"
    if your_bmi<=25.0:
        return "Normal"
    if your_bmi<=30.0:
        return "Overweight"
    if your_bmi>30:
        return "Obese"
    
#Fake Binary
def fake_bin(x):
    result=""
    for num in x:
        if int(num)<5:
            result+="0"
        else:
            result+="1"
    return result

#Find Maximum and Minimum Values of a List
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)

#Beginner - Reduce but Grow
def grow(arr):
    result=1
    for num in arr:
        result*=num
    return result
        
#Count of positives / sum of negatives
def count_positives_sum_negatives(arr):
    result=[]
    pos=0
    neg=0
    for num in arr:
        if num>0:
            pos+=1
        else:
            neg+=num
        result=[pos, neg]
    return result

#Century From Year
def century(year):
    century=(year+99) // 100
    return century

#You only need one - Beginner
def check(seq, elem):
    if elem in seq:
        return True
    else:
        return False
    
#Convert number to reversed array of digits
def digitize(n):
    result=[]
    for num in str(n):
        result.insert(0, int(num))
    return result


#Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg*fuel_left >= distance_to_pump:
        return True
    else:
        return False
    
#DNA to RNA Conversion
def dna_to_rna(dna):
    rna=dna
    return rna.replace("T", "U")

#Is n divisible by x and y?
def is_divisible(n,x,y):
    return n%x==0 and n%y==0

#Count by X
def count_by(x, n):
    result=[]
    for i in range(1, n+1):
        a=x*i
        result.append(a)
    return result
    
#Abbreviate a Two Word Name
def abbrev_name(name):
    first=name[0]
    for letter in range(len(name)):
        if name[letter]==" ":
            last=name[letter+1]
    return (first.upper() + "." + last.upper())

#A Needle in the Haystack
def find_needle(haystack):
    position=haystack.index("needle")
    return "found the needle at position {}".format(position)

#Sentence Smash
def smash(words):
    sentence=""
    for i in range(len(words)):
        sentence+=(words[i])
        sentence+=" "
    return sentence.strip()

#Convert a string to an array
def string_to_array(s):
    a=[]
    if s=="":
        a.append(s)
    else:
        a=s.split()
    return a

#Reversed sequence
def reverse_seq(n):
    sequence=[]
    if n>0:
        for i in range(1, n+1):
            sequence.append(i)
    return sequence[::-1]

#Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)
    
#If you can't sleep, just count sheep!!
def count_sheep(n):
    sentence=""
    for i in range(1, n+1):
        sentence+=(str(i) + " sheep...")
    return sentence

#Quarter of the year
def quarter_of(month):
    if 1<=month<=3:
        return 1
    elif 4<=month<=6:
        return 2
    elif 7<=month<=9:
        return 3
    elif 10<=month<=12:
        return 4
        
#Grasshopper - Personalized Message
def greet(name, owner):
    if name==owner:
        return 'Hello boss'
    else:
        return 'Hello guest'
    
#Rock Paper Scissors!
def rps(p1, p2):
    if p1=="scissors" and p2=="scissors":
        return "Draw!"
    elif p1=="paper" and p2=="paper":
        return "Draw!"
    elif p1=="rock" and p2=="rock":
        return "Draw!"
    elif p1=="rock" and p2=="paper":
        return "Player 2 won!"
    elif p1=="paper" and p2=="scissors":
        return "Player 2 won!"
    elif p1=="scissors" and p2=="rock":
        return "Player 2 won!"
    elif p1=="rock" and p2=="scissors":
        return "Player 1 won!"
    elif p1=="paper" and p2=="rock":
        return "Player 1 won!"
    elif p1=="scissors" and p2=="paper":
        return "Player 1 won!"
    
#Transportation on vacation
def rental_car_cost(d):
    total=0
    if d<3:
        total=d*40
        return total
    elif d<7:
        total=d*40 - 20
        return total
    elif d>=7:
        total=d*40 - 50
        return total
    
#Grasshopper - Grade book
def get_grade(s1, s2, s3):
    score=(s1+s2+s3)/3
    if 90 <= score <= 100:
        return "A"
    if 80 <= score <= 90:
        return "B"
    if 70 <= score <= 80:
        return "C"
    if 60 <= score <= 70:
        return "D"
    if 0 <= score <= 60:
        return "F"
    
#Volume of a Cuboid
def get_volume_of_cuboid(length, width, height):
    return length * width * height

#Remove exclamation marks
def remove_exclamation_marks(s):
    return s.replace("!", "")

#Third Angle of a Triangle
def other_angle(a, b):
    c=180 - (a+b)
    return c

#Thinkful - Logic Drills: Traffic light
def update_light(current):
    if current=="green":
        return "yellow"
    elif current=="yellow":
        return "red"
    elif current=="red":
        return "green"

#Total amount of points  
def points(games):
    pts = 0
    for i in games:
      if i[0] > i[2]:
        pts += 3
      elif i[0] == i[2]:
        pts += 1
    return pts
        
#Area or Perimeter
def area_or_perimeter(l , w):
    if l==w:
        return l*w
    else:
        return (l+w)*2
    
#Square Every Digit
def square_digits(num):
    second_num=""
    for i in str(num):
        second_num+=str(int(i)**2)
    return int(second_num)

#L1: Set Alarm
def set_alarm(employed, vacation):
    if employed==True and vacation==False:
        return True
    else:
        return False
    
#Sum Mixed Array
def sum_mix(arr):
    sum=0
    for x in arr:
        sum+=int(x)
    return sum

#Grasshopper - Messi goals function
def goals(laLiga, copaDelRey, championsLeague):
    all_goals = laLiga + copaDelRey + championsLeague
    return all_goals

#Reversed Words
def reverse_words(s):
    reversed=[]
    for word in s.split():
        reversed.append(word)
    reversed.reverse()
    return " ".join(reversed)

#Get the mean of an array
import math
def get_average(marks):
    avg=sum(marks) / len(marks)
    avg=math.floor(avg)
    return avg
#or
def get_average(marks):
    avg=sum(marks) // len(marks)
    return avg

#Sum without highest and lowest number
def sum_array(arr):
    if arr and len(arr)>1:
        return sum(arr) - min(arr) - max(arr)
    else:
        return 0
    
#Double Char
def double_char(s):
    double=""
    for char in s:
        char=char*2
        double+=char
    return double

#Array plus array
def array_plus_array(arr1,arr2):
    return sum(arr1) + sum(arr2)

#The Feast of Many Beasts
def feast(beast, dish):
    if beast[0]==dish[0] and beast[-1]==dish[-1]:
        return True
    else:
        return False
    
#Parse nice int from char problem
def get_age(age):
    return int(age[0])

#Beginner Series #4 Cockroach
import math
def cockroach_speed(s):
    return math.floor(s*27.778)

#Grasshopper - Check for factor
def check_for_factor(base, factor):
    if base%factor==0:
        return True
    else:
        return False
    
#Switch it Up!
def switch_it_up(number):
    if number==0:
        return "Zero"
    elif number==1:
        return "One"
    elif number==2:
        return "Two"
    elif number==3:
        return "Three"
    elif number==4:
        return "Four"
    elif number==5:
        return "Five"
    elif number==6:
        return "Six"
    elif number==7:
        return "Seven"
    elif number==8:
        return "Eight"
    else:
        return "Nine"
    
#Function 2 - squaring an argument
def square(n):
    return n**2

#Twice as old
def twice_as_old(dad_years_old, son_years_old):
    a=dad_years_old-(son_years_old*2)
    if a<0:
        return a*-1
    else:
        return a
    
#Get Planet Name By ID
def get_planet_name(id):
    if id==1:
        return "Mercury"
    elif id==2:
        return "Venus"
    elif id==3:
        return "Earth"
    elif id==4:
        return "Mars"
    elif id==5:
        return "Jupiter"
    elif id==6:
        return "Saturn"
    elif id==7:
        return "Uranus"
    else:
        return "Neptune"
        
#Keep up the hoop
def hoop_count(n):
    if n<10:
        return "Keep at it until you get it"
    else:
        return "Great, now move on to tricks"
    
#Removing Elements
def remove_every_other(my_list):
    new_list=[]
    for i in range(len(my_list)):
        if i%2==0:
            new_list.append(my_list[i])
    return new_list

#Will there be enough space?
def enough(cap, on, wait):
    if cap> on+wait:
        return 0
    else:
        return wait+on-cap
    
#Count the Monkeys!
def monkey_count(n):
    count=[]
    for i in range(n):
        count.append(i+1)
    return count

#Find the first non-consecutive number
def first_non_consecutive(arr):
    for i in range(len(arr)):
        if arr[i] - arr[i-1] > 1:
            return arr[i]
        
#Grasshopper - Debug sayHello
def say_hello(name):
    a= "Hello,", name
    return " ".join(a)

#Grasshopper - Terminal game move function
def move(position, roll):
    return position+roll*2

#Is the string uppercase?
def is_uppercase(inp):
    cap=inp.upper()
    if cap==inp:
        return True
    else:
        return False
    
#All Star Code Challenge #18
def str_count(strng, letter):
    count=0
    for i in range(len(strng)):
        if letter==strng[i]:
            count+=1
    return count

#Is it even?
def is_even(n): 
    if n%2==0:
        return True
    else:
        return False
    
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