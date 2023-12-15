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