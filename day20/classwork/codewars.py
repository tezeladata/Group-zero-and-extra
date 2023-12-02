#Beginner - Lost Without a Map
def maps(a):
    new=[]
    for num in a:
        new.append(num*2)
    return new

#Keep Hydrated!
def litres(time):
    return int(time*0.5)

#Convert number to reversed array of digits
def digitize(n):
    new_arr=[]
    n=str(n)
    for i in n:
        new_arr.append(int(i))
    new_arr.reverse()
    return new_arr

#Basic Mathematical Operations
def basic_op(operator, value1, value2):
    if operator=="+":
        return value1+value2
    elif operator=="-":
        return value1-value2
    elif operator=="*":
        return value1*value2
    else:
        return value1/value2
    
#Century From Year
def century(year):
    if year%100==0:
        return year//100
    else:
        return year//100+1
    
#Beginner Series #2 Clock
def past(h, m, s):
    total= h * 3600000 + m * 60000 + s * 1000
    return total

#Beginner Series #1 School Paperwork
def paperwork(n, m):
    if n<0 and m<0:
        return 0
    elif n<0 or m<0:
        return 0
    else:
        return m*n
    
#Opposites Attract
def lovefunc( flower1, flower2 ):
    if (flower1%2==0 and flower2%2!=0) or (flower1 %2!=0 and flower2 %2==0):
        return True
    else:
        return False
    
#Abbreviate a Two Word Name
def abbrev_name(name):
    abrev=""
    abrev+=name[0]
    abrev+="."
    for i in range(len(name)):
        if name[i]==" ":
            abrev+=name[i+1]
    return abrev.upper()
#or
def abbrev_name(name):
    words = name.split()
    first_letter = words[0][0]
    first_letter.upper()
    second_letter= words[1][0]
    second_letter.upper()
    return "{}.{}".format(first_letter, second_letter)

#Simple multiplication
def simple_multiplication(number) :
    if number%2==0:
        return number*8
    else:
        return number*9

