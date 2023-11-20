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