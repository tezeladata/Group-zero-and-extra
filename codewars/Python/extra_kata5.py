#Triple Trouble
def triple_trouble(one, two, three):
    new=""
    for i in range(len(one)):
        new+=one[i]
        new+=two[i]
        new+=three[i]
    return new

#How old will I be in 2099?
def calculate_age(year_of_birth, current_year):
    if year_of_birth-1>current_year:
        return "You will be born in {} years.".format(year_of_birth-current_year)
    elif year_of_birth==current_year:
        return "You were born this very year!"
    elif year_of_birth-1 == current_year:
        return "You will be born in {} year.".format(year_of_birth-current_year)
    elif current_year-1 == year_of_birth:
        return "You are {} year old.".format(current_year-year_of_birth)
    else:
        return "You are {} years old.".format(current_year-year_of_birth)

#Regex count lowercase letters
def lowercase_count(strng):
    count=0
    for i in strng:
        if i!=i.upper():
            count+=1
    return count

#USD => CNY
def usdcny(usd):
    chn=str(usd*6.75)
    if "." in chn:
        if chn[-2]==".":
            chn+="0"
    else:
        chn+="00"
    return "{} Chinese Yuan".format(chn)

#Formatting decimal places #0
def two_decimal_places(n):
    return round(n*100)/100

#Name on billboard
def billboard(name, price=30):
    new=0
    for i in name:
        new+=price
    return new

#How many stairs will Suzuki climb in 20 years?
def stairs_in_20(stairs):
    total=0
    for day in stairs:
        for stair in day:
            total+=stair
    return total*20

#OOP: Object Oriented Piracy
class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    def is_worth_it(self):
        return self.draft - self.crew *1.5 > 20
    
#Miles per gallon to kilometers per liter
def converter(mpg):
    return round(mpg * 1.609344 / 4.54609188, 2)

#Incorrect division method
def divide_numbers(x,y):
    return x / y

#Holiday VI - Shark Pontoon
def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin==True:
        shark_speed=shark_speed*0.5
    my_time=pontoon_distance / you_speed
    shark_time=shark_distance / shark_speed
    if my_time>shark_time:
        return "Shark Bait!"
    else:
        return "Alive!"
    
#Define a card suit
def define_suit(card):
    if card[-1]=="C":
        return "clubs"
    elif card[-1]=="D":
        return "diamonds"
    elif card[-1]=="H":
        return "hearts"
    else:
        return "spades"
    
#Do you speak "English"?
def sp_eng(sentence): 
    return "english" in sentence.lower()

#SpeedCode #2 - Array Madness
def array_madness(a,b):
    new_arr1=[]
    new_arr2=[]
    for i in a:
        new_arr1.append(i**2)
    for x in b:
        new_arr2.append(x**3)
    return sum(new_arr1) > sum(new_arr2)

#No Loops 2 - You only need one
def check(a, x): 
    return x in a

#Grasshopper - Combine strings
def combine_names(first_name, last_name):
    return "{} {}".format(first_name, last_name)

#Find the Difference in Age between Oldest and Youngest Family Members
def difference_in_ages(ages):
    new=(min(ages), max(ages), max(ages)-min(ages))
    return new

#The falling speed of petals
def sakura_fall(v):
    if v>0:
        return 400/v
    else:
        return 0
    
#Remove the time
def shorten_to_date(long_date):
    numb=long_date.index(",")
    return long_date[0:numb]

#Exclamation marks series #2: Remove all exclamation marks from the end of sentence
def remove(s):
    while s[-1]=="!":
        s=s[:-1]
    return s

#Is it a number?
def is_digit(s):
    if len(s)==0 or s[0] not in "-+.0123456789":
        return False
    for char in s[1:]:
        if char not in ".0123456789":
            return False
    return True

#Regexp Basics - is it a digit?
def is_digit(n):
    return n in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

#Smallest unused ID
def next_id(arr):
    for i in range(len(arr)+1):
        if i not in arr:
            return i

#Fundamentals: Return
def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def mod(a,b):
    return a%b
def exponent(a,b):
    return a**b
def subt(a,b):
    return a-b

#Fix your code before the garden dies!
def rain_amount(mm):
    if mm < 40:
        return "You need to give your plant " + str(40-mm) + "mm of water"
    else:
         return "Your plant has had more than enough water for today!"
    
#get ascii value of character
def get_ascii(ch : str) -> int:
    return ord(ch)

#CSV representation of array
def to_csv_text(array):
    new=[]
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j]=str(array[i][j])
        new.append(",".join(array[i]))
    return "\n".join(new)

#Contamination #1 -String-
def contamination(text, char):
    new=""
    if text=="":
        return ""
    elif char=="":
        return ""
    else:
        for i in range(len(text)):
            new+=char
    return new

#Closest elevator
def elevator(left, right, call):
    l=abs(left-call)
    r=abs(right-call)
    if l<r:
        return "left"
    else:
        return "right"
    
#A Strange Trip to the Market
def is_lock_ness_monster(string):
    if "tree fiddy" in string or "three fifty" in string or "3.50" in string:
        return True
    else:
        return False
    
#Pythagorean Triple
def pythagorean_triple(integers):
    a, b, c = sorted(integers)
    if a**2 + b**2 == c**2:
        return True
    else:
        return False
    
#Exclamation marks series #4: Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string
def remove(s):
    new=""
    for i in s:
        if i!="!":
            new+=i
    return new+"!"

#Geometry Basics: Distance between points in 2D
import math
def distance_between_points(a, b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

#Leonardo Dicaprio and Oscars
def leo(oscar):
    if oscar>88:
        return "Leo got one already!"
    elif oscar==88:
        return "Leo finally won the oscar! Leo is happy"
    elif oscar==86:
        return "Not even for Wolf of wallstreet?!"
    else:
        return "When will you give Leo an Oscar?"
    
#Exclamation marks series #6: Remove n exclamation marks in the sentence from left to right
def remove(s, n):
    return s.replace("!", "", n)

#Tip Calculator
import math
def calculate_tip(amount, rating):
    rating=rating.lower()
    tip={
        "terrible": 0,
        "poor": 0.05,
        "good": 0.1,
        "great": 0.15,
        "excellent": 0.2
    }.get(rating)
    if tip==None:
        return 'Rating not recognised'
    return int(math.ceil(amount*tip))

#Are arrow functions odd?
def odds(values):
    return [x for x in values if x%2==1]

#Compare within margin
def close_compare(a, b, margin=0):
    if a-b>margin:
        return 1
    elif b-a>margin:
        return -1
    else:
        return 0
    
#BASIC: Making Six Toast.
def six_toast(num):
    if num>6:
        return num-6
    elif num==6:
        return 0
    else:
        return 6-num