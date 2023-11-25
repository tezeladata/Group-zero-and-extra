#Find the position!
def position(alphabet):
    alph={
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
    for i in alphabet:
        return "Position of alphabet: {}".format(alph[i])
    
#Alan Partridge II - Apple Turnover
def apple(x):
    if type(x)==int:
        if x**2>1000:
            return "It's hotter than the sun!!"
        else:
            return "Help yourself to a honeycomb Yorkie for the glovebox."
    elif int(x)**2>1000:
        return "It's hotter than the sun!!"
    elif int(x)**2<1000:
        return "Help yourself to a honeycomb Yorkie for the glovebox."
    
#Grasshopper - Debug
def weather_info (temp):
    c = convert_to_celsius(temp)
    if (c < 0):
        return (str(c) + " is freezing temperature")
    else:
        return (str(c) + " is above freezing temperature")
    
def convert_to_celsius (temperature):
    celsius = (temperature - 32) * (5/9)
    return celsius

#Find the Remainder
def remainder(a,b):
    if min(a,b)==0:
        return None
    elif a>b:
        return a%b
    else:
        return b%a
    
#Generate range of integers
def generate_range(min, max, step):
    a=[]
    for i in range(min, max+1, step):
        a.append(i)
    return a

#101 Dalmatians - squash the bugs, not the dogs!
def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"];
    if n <=10:
        respond=dogs[0]
    elif n <=50:
        respond=dogs[1]
    elif n==101:
        respond=dogs[3]
    else:
        respond=dogs[2]
    return respond

#Price of Mangoes
def mango(quantity, price):
    return price * (quantity - (quantity // 3))

#Surface Area and Volume of a Box
def get_size(w,h,d):
    answer=[]
    answer.append(2*(w*h + w*d + h*d))
    answer.append(w*h*d)
    return answer

#Printing Array elements with Comma delimiters
def print_array(arr):
    if arr!=None:
        return ",".join(str(i) for i in arr)
    
#Remove First and Last Character Part Two
def array(string):
    a= string.strip().split(",")
    b= a[1:-1]
    c= " ".join(b)
    if len(c)==0:
        return None
    else:
        return c