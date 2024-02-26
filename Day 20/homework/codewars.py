#A Needle in the Haystack
def find_needle(haystack):
    return "found the needle at position {}".format(haystack.index("needle"))
#or
def find_needle(haystack):
    i=0
    while i<len(haystack):
        if haystack[i]=="needle":
            return "found the needle at position " + str(i)
        i+=1

#MakeUpperCase
def make_upper_case(s):
    return s.upper()

#Sum Arrays
def sum_array(a):
    total=0
    for i in a:
        total+=i
    return total
#or
def sum_array(a):
    return sum(a)

#Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0]=="r" or name[0]=="R":
        return "{} plays banjo".format(name)
    else:
        return "{} does not play banjo".format(name)
    
#Invert values
def invert(lst):
    new_lst=[]
    for num in lst:
        new_lst.append(num*-1)
    return new_lst

#Calculate average
def find_average(numbers):
    if len(numbers)!=0:
        return sum(numbers) / len(numbers)
    else:
        return 0