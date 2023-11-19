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
    else:
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
digitize(123134667634)

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