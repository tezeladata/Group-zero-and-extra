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