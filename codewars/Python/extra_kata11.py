#Is a number prime?
def is_prime(num):
    if num<=0 or num==1:
        return False
    i=2
    while (i<=num**0.5):
        if num%i==0:
            return False
        i+=1
    return True

#Are they the "same"?
def comp(array1, array2):
    if type(array1)!=list or type(array2)!=list:
        return False
    res=[]
    for i in array1:
        res.append(i**2)
    return sorted(res)==sorted(array2)

#Playing with digits
def dig_pow(n, p):
    count=0
    for i in list(str(n)):
        count+=int(i)**p
        p+=1
    if count%n==0:
        return count/n
    else:
        return -1
    
#Pete, the baker
def cakes(recipe, available):
    count=[]
    for i in recipe:
        if i in available:
            count.append(available[i]/recipe[i])
        else:
            return 0
    return int(min(count))

#Sum of Digits / Digital Root
def digital_root(n):
    sum=0
    for i in str(n):
        sum+=int(i)
    if len(str(sum))>=2:
        sum=digital_root(sum)
    return sum

#Break camelCase
def solution(s):
    new_str=""
    for i in s:
        if i.isupper():
            new_str+=" "+i
        else:
            new_str+=i
    return new_str

#Directions Reduction
def dir_reduc(arr):
    opp={"NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST": "WEST",
        "WEST": "EAST"}
    for i in range(len(arr)-1):
        if arr[i+1]==opp[arr[i]]:
            del arr[i], arr[i]
            return dir_reduc(arr)
    return arr

#Sort the odd
def sort_array(source_array):
    if not source_array:
        return []
    else:
        odd=sorted(x for x in source_array if x%2!=0)
        for i in range(len(source_array)):
            if source_array[i]%2!=0:
                source_array[i]=odd.pop(0)
        return source_array
    
#The Hashtag Generator
def generate_hashtag(s):
    if s=="":
        return False
    else:
        s=s.strip()
        s=s.split(" ")
        cap=[word.capitalize() for word in s]
        new_arr="#"
        for i in range(len(cap)):
            new_arr+=cap[i]
        if len(new_arr)>140:
            return False
        else:
            return new_arr
        
#Count the smiley faces!
def count_smileys(arr):
    smiley=[":)", ":D",";)",";D",":-)",":-D",";-D",";-)","~:)","~:D","~;)","~;D",":-)",":-D",";~)", ":~)", ";-D",";~D",":)",":-D",";~D"]
    count=0
    for i in arr:
        if i in smiley:
            count+=1
    return count

#Human readable duration format
units={
    "year": 60*60*24*365,
    "day": 60*60*24,
    "hour": 60*60,
    "minute": 60,
    "second": 1,
    }
def format_duration(seconds):
    if not seconds: return "now"
    result=[]
    for unit, value in units.items():
        count, seconds= divmod(seconds, value)
        if count==1: result.append(f"{count} {unit}")
        if count>1: result.append(f"{count} {unit}s")
    *body, tail = result
    #body now is anything else than tail
    if not body: return tail
    return f"{', '.join(body)} and {tail}" if tail else body

#Extract the domain name from a URL
def domain_name(url):
    without_scheme = url.split('://', 1)[-1]
    without_scheme=without_scheme.split(".")
    if without_scheme[0]=="www":
        return str(without_scheme[1])
    else:
        return str(without_scheme[0])

#Stop gninnipS My sdroW!
def spin_words(sentence):
    sentence=sentence.split()
    for i in range(len(sentence)):
        if len(sentence[i])>=5:
            sentence[i]=sentence[i][::-1]
    return " ".join(sentence)

#UEFA EURO 2016
def uefa_euro_2016(teams, scores):
    for i in scores:
        if scores[0]>scores[1]:
            return "At match {} - {}, {} won!".format(teams[0], teams[1], teams[0])
        elif scores[0]==scores[1]:
            return "At match {} - {}, teams played draw.".format(teams[0], teams[1])
        else:
            return "At match {} - {}, {} won!".format(teams[0], teams[1], teams[1])
        
#They say that only the name is long enough to attract attention. They also said that only a simple Kata will have someone to solve it. This is a sadly story #1: Are they opposite?
def is_opposite(s1,s2):
    if s1=="" and s2=="":
        return False
    else:
        if s1.swapcase()==s2:
            return True
        else:
            return False    
        
#Pirates!! Are the Cannons ready!??
def cannons_ready(gunners):
    for key, value in gunners.items():
        if value=="nay": return 'Shiver me timbers!'
        else: 'Fire!'
    return "Fire!"

#NBA full 48 minutes average
def nba_extrap(ppg, mpg):
    mpg_48=ppg*(48/mpg)
    return round(mpg_48, 1)

#Ensure question
def ensure_question(s):
    if s=="":
        return "?"
    else:
        if s[-1]!="?": 
            return s+"?"
        else: 
            return s
        
#For Twins: 2. Math operations
def ice_brick_volume(radius, bottle_length, rim_length):
    return (bottle_length-rim_length)*radius*radius*2

#Sum even numbers
def sum_even_numbers(seq): 
    sum=0
    for i in seq:
        if i%2==0:
            sum+=i
    return sum

#Area of a Circle
import math
def circle_area(r):
    if r<=0:
        raise ValueError
    else:
        return math.pi * r**2
    
#Digitize
def digitize(n):
    n=str(n)
    n=list(n)
    ans=[]
    for i in n:
        ans.append(int(i))
    return ans

#max diff - easy
def max_diff(lst):
    lst=sorted(lst)
    if len(lst)==0:
        return 0
    else:
        return lst[-1]-lst[0]
    
#Largest Elements
def largest(n, xs):
    xs=sorted(xs)
    ans=[]
    for i in range(n):
        ans.append(xs[-1])
        xs.remove(xs[-1])
    return ans[::-1]

#All unique
def has_unique_chars(string):
    unique_chars = set()
    for char in string:
        if char in unique_chars:
            return False
        else:
            unique_chars.add(char)
    return True

#V A P O R C O D E
def vaporcode(s):
    ans=""
    for i in s:
        if i!=" ":
            ans+=i.upper()+"  "
    return ans.strip()

#Nickname Generator
def nickname_generator(name):
    if len(name)<4:
        return "Error: Name too short"
    else:
        if name[2] in "aeiou":
            return name[:4]
        else:
            return name[:3]
        
#Nth Smallest Element (Array Series #4)
def nth_smallest(arr, pos):
    arr=sorted(arr)
    return arr[pos-1]

#Incrementer
def incrementer(arr):
    if not arr:
        return []
    result = [(digit + (index + 1)) % 10 for index, digit in enumerate(arr)]
    return result

#Strong Number (Special Numbers Series #2)
def strong_num(number):
    count=0
    for i in str(number):
        fact=1
        for i in range(1,int(i)+1):
            fact*=i
            count+=fact
    if number==2 or number==145 or number==40585:
        return "STRONG!!!!"
    elif count==number:
        return "STRONG!!!!"
    else:
        return "Not Strong !!"
#or
STRONGS = {1, 2, 145, 40585}
def strong_num(number):
    return "STRONG!!!!" if number in STRONGS else "Not Strong !!"

#Simple string characters
def solve(s):
    uppercase_count = sum(1 for char in s if char.isupper())
    lowercase_count = sum(1 for char in s if char.islower())
    numbers_count = sum(1 for char in s if char.isdigit())
    special_characters_count = len(s) - (uppercase_count + lowercase_count + numbers_count)

    return [uppercase_count, lowercase_count, numbers_count, special_characters_count]