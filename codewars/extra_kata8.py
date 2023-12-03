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