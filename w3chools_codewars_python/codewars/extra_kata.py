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
    
