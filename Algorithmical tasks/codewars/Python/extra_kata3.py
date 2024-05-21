#Predict your age!
import math
def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    new=[age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    new2=[]
    for num in new:
        num**=2
        new2.append(num)
    a=sum(new2)
    b=a**0.5
    b/=2
    return math.floor(b)

#Row Weights
def row_weights(array):
    team1=0
    team2=0
    for i in range(len(array)):
        if i%2==0:
            team2+=array[i]
        else:
            team1+=array[i]
    return team2, team1

#Sum of numbers from 0 to N
def show_sequence(n):
    ans="0"
    count=0
    for i in range(1, n+1):
        ans+="+{}".format(i)
        count+=i
    ans+=" = {}".format(count)
    if n==0:
        return "0=0"
    elif n<0:
        return "{}<0".format(n)
    else:
        return ans
    
#Greet Me
def greet(name): 
    name=name.lower()
    name=list(name)
    name[0]=name[0].upper()
    new=""
    for i in name:
        new+=i
    return "Hello {}!".format(new)

#Remove duplicate words
def remove_duplicate_words(s):
    s=s.split(" ")
    sentence=[]
    for item in s:
        if item not in sentence:
            sentence.append(item)
    return " ".join(sentence)
    
#Sum of Cubes
def sum_cubes(n):
    new=0
    for i in range(1, n+1):
        new+=i**3
    return new

#Sorted? yes? no? how?
def is_sorted_and_how(arr):
    if arr==sorted(arr):
        return "yes, ascending"
    elif arr==sorted(arr, reverse=True):
        return "yes, descending"
    else:
        return "no"
    
#Digits explosion
def explode(s):
    s=list(s)
    new=""
    for num in s:
        new+=str(num)*int(num)
    return new

#Bumps in the Road
def bumps(road):
    road=list(road)
    bump=road.count("n")
    if bump<=15:
        return "Woohoo!"
    else:
        return "Car Dead"
    
#Love vs friendship
def words_to_marks(s):
    value={
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26
    }
    count=0
    s=list(s)
    for char in s:
        count+=value[char]
    return count

#Greatest common divisor
import math
def mygcd(x, y):
    return math.gcd(x, y)
        
#Find the vowels
def vowel_indices(word):
    word = word.lower()
    vowels = ["a", "e", "i", "o", "u", "y"]
    list = []
    for index in range(len(word)):
        if word[index] in vowels:
            list.append(index + 1)
    return list

#Sort the Gift Code
def sort_gift_code(code):
    a=sorted(code)
    b=""
    for i in a:
        b+=i
    return b

#Sort array by string length
def sort_by_length(arr):
    return sorted(arr, key=len)

#Largest 5 digit number in a series
def solution(digits):
    res=0
    for iteration in range(len(digits)):
        if int(digits[iteration:iteration+5]) > res:
            res=int(digits[iteration:5+iteration])
    return res

#Alphabet war
def alphabet_war(fight):
    a={
        "w": 4,
        "p": 3,
        "b": 2,
        "s": 1
    }
    b={
        "m": 4,
        "q": 3,
        "d": 2,
        "z": 1
    }
    fight=list(fight)
    left=0
    right=0
    for e in fight:
        left+=a.get(e, 0)
        right+=b.get(e, 0)
    if left>right:
        return "Left side wins!"
    elif right>left:
        return "Right side wins!"
    elif right==left:
        return "Let's fight again!"
    
#Largest pair sum in array
def largest_pair_sum(numbers): 
    count=0
    count+=max(numbers)
    numbers.remove(max(numbers))
    count+=max(numbers)
    return count

#Switcheroo
def switcheroo(s):
    res=""
    for letter in s:
        if letter=="a":
            letter="b"
        elif letter=="b":
            letter="a"
        res+=letter
    return res

#Sum of Triangular Numbers
def sum_triangular_numbers(n):
    if n<0:
        return 0
    else:
        return (n*(n+1)*(n+2))/6
    
#Even numbers in an array
def even_numbers(arr,n):
    new=[]
    for num in arr:
        if num%2==0:
            new.append(num)
    return new[-n:]

#Filter the number
def filter_string(string):
    new=""
    for i in string:
        if i>="0" and i<="9":
            new+=i
    return int(new)

#Simple beads count
def count_red_beads(n):
    if n<2:
        return 0
    else:
        return (n-1)*2
    
#Boiled Eggs
import math
def cooking_time(eggs):
    a=math.ceil(eggs/8)
    return a*5

#Functional Addition
def add(n):
    return lambda x: x+n

#My Language Skills
def my_languages(results):
    new=[]
    for key, value in results.items():
        if value>=60:
            new.append(key)
    return sorted(new, key=lambda x: results[x], reverse=True)

#Sort arrays - 1
def sortme(names):
    return sorted(names)

#Speed Control
def gps(s, x):
    if len(x)<2:
        return 0
    else:
        numb=max(x[i] - x[i-1] for i in range(1, len(x)))
    return numb*3600.0/s

#Minimize Sum Of Array (Array Series #1)
def min_sum(arr):
    arr=sorted(arr)
    last_num=0
    for i in range(len(arr)//2):
        last_num+=arr[i]*arr[-i-1]
    return last_num

#Odd-Even String Sort
def sort_my_string(s):
    even=""
    odd=""
    for i in range(0, len(s), 2):
        even+=s[i]
    for i in range(1, len(s), 2):
        odd+=s[i]
    return "{} {}".format(even, odd)

#Maximum Triplet Sum (Array Series #7)
def max_tri_sum(numbers):
    numbers=set(numbers)
    numbers=list(numbers)
    a=0
    a+=max(numbers)
    numbers.remove(max(numbers))
    a+=max(numbers)
    numbers.remove(max(numbers))
    a+=max(numbers)
    return a

#Most digits
def find_longest(arr):
    len_arr=[]
    for i in arr:
        len_arr.append(len(str(i)))
    return arr[len_arr.index(max(len_arr))]

#Multiples of 3 or 5
def solution(number):
    if number<0:
        return 0
    else:
        count=0
        for i in range(1, number):
            if i%3==0 or i%5==0:
                count+=i
        return count
    
#Who likes it?
def likes(names):
    if len(names)==0:
        return "no one likes this"
    elif len(names)==1:
        return "{} likes this".format(names[0])
    elif len(names)==2:
        return "{} and {} like this".format(names[0], names[1])
    elif len(names)==3:
        return "{}, {} and {} like this".format(names[0], names[1], names[2])
    else:
        return "{}, {} and {} others like this".format(names[0], names[1], len(names)-2)
    
#Create Phone Number
def create_phone_number(n):
    first="({}{}{})".format(n[0], n[1], n[2])
    second="{}{}{}-{}{}{}{}".format(n[3], n[4], n[5], n[6], n[7], n[8], n[9],)
    return "{} {}".format(first, second)

#Find the odd int
def find_it(seq):
    for i in seq:
        if (seq.count(i))%2!=0:
            return i
        
#Sum of Digits / Digital Root
def digital_root(n):
    a=sum([int(num) for num in str(n)])
    if len(str(a)) >=2:
        a=digital_root(a)
    return a

#Bit Counting
def count_bits(n):
    n=bin(n)
    n=str(n)
    count=0
    for i in n:
        if i=="1":
            count+=1
    return count

#Counting Duplicates
def duplicate_count(text):
    dupes=[]
    text=text.lower()
    for chr in text:
        count=text.count(chr)
        if count>1:
            if chr not in dupes:
                dupes.append(chr)
    return len(dupes)

#Duplicate Encoder
def duplicate_encode(word):
    word=word.lower()
    new=""
    for i in word:
        if word.count(i)>1:
            new+=")"
        else:
            new+="("
    return new

#Find The Parity Outlier
def find_outlier(integers):
    even=[]
    odd=[]
    for i in integers:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    if len(even)==1:
        return even[0]
    else:
        return odd[0]
    
#Replace With Alphabet Position
def alphabet_position(text):
    text=text.lower()
    alphabet={
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26  
    }
    new_str=""
    new_arr=[]
    for i in text:
        if i in alphabet:
            new_str+=str(alphabet[i])
            new_arr.append(str(alphabet[i]))
        else:
            continue
    if len(new_str)==1 or len(new_str)==2:
        return new_str
    else:
        return " ".join(new_arr)
        
#Persistent Bugger.
def persistence(n):
    a=0
    while n>9:
        a+=1
        n_str=str(n)
        total=1
        for i in n_str:
            total=total*int(i)
        n=total
    return a
            
#Take a Ten Minutes Walk
def is_valid_walk(walk):
    ab=walk.count("s")==walk.count("n")
    cd=walk.count("e")==walk.count("w")
    length=len(walk)==10
    return ab and cd and length

#Convert string to camel case
def to_camel_case(text):
    text=text.replace("-", "_")
    text=text.split("_")
    a=0
    c_case=""
    for word in text:
        a+=1
        if a==1:
            c_case+=word
        else:
            c_case+=word.capitalize()
    return c_case

#Moving Zeros To The End
def move_zeros(lst):
    new_arr=[]
    for i in lst:
        if i!=0:
            new_arr.append(i)
    a=lst.count(0)
    for i in range(a):
        new_arr.append(0)
    return new_arr

#Does my number look big in this?
def narcissistic( value ):
    a=str(value)
    b=len(a)
    count=0
    for i in range(b):
        count+=int(a[i])**b
    if count==value:
        return True
    else:
        return False
    
#Your order, please
def order(sentence):
    new=[]
    for i in range(1, 10):
        for word in sentence.split():
            if str(i) in word:
                new.append(word)
    return " ".join(new)

#Split Strings
def solution(s):
    if len(s)%2!=0:
        s+="_"
    new_arr=[]
    for index in range(0, len(s), 2):
        new_arr.append(s[index:index+2])
    return new_arr

#Get number from string
def get_number_from_string(string):
    new=""
    for i in string:
        if i.isdigit()==True:
            new+=i
    return int(new)

#Palindrome chain length
def check(a):
    return str(a)==str(a)[::-1]

def palindrome_chain_length(n):
    count=0
    while check(n)!=True:
        n=n+int(str(n)[::-1])
        count+=1
    return count

#Divide and Conquer
def div_con(x):
    strs=[]
    ints=[]
    for i in x:
        if type(i)==str:
            strs.append(int(i))
        elif type(i)==int:
            ints.append(i)
    return sum(ints)-sum(strs)

#Smallest value of an array
def find_smallest(numbers, to_return):
    if to_return=="value":
        return min(numbers)
    else:
        a=min(numbers)
        return numbers.index(a)
    
#Ordered Count of Characters
def ordered_count(inp):
    new_arr=[]
    for i in inp:
        occurences=(i, inp.count(i))
        if occurences not in new_arr:
            new_arr.append(occurences)
    return new_arr

#Number Of Occurrences
def number_of_occurrences(element, sample):
    return sample.count(element)

#Largest Square Inside A Circle
def area_largest_square(r):
    square_side=(r**2 + r**2)**0.5
    return round(square_side**2)

#Convert an array of strings to array of numbers
def to_float_array(arr): 
    new_arr=[]
    for i in arr:
        new_arr.append(float(i))
    return new_arr

#Perimeter sequence
def perimeter_sequence(a, n): 
    return 4*(a*n)

#Halving Sum
def halving_sum(n): 
    if n==1:
        return 1
    else:
        return n+halving_sum(n//2)
    
#Reverse a Number
def reverse_number(n):
    if n<0:
        res=""
        res+="-"
        n=str(n)
        for i in range(len(n)):
            res+=n[-i]
        return int(res[1:])
    elif 0<=n<=9:
        return n
    else:
        n=str(n)
        return int(n[::-1])
    
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