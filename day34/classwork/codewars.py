#Convert a String to a Number!
def string_to_number(s):
    return int(s)

#Opposites Attract
def lovefunc( flower1, flower2 ):
    if flower1%2==0 and flower2%2!=0:
        return True
    elif flower1%2!=0 and flower2%2==0:
        return True
    else:
        return False
#or
def lovefunc( flower1, flower2 ):
    if (flower1+flower2)%2!=0:
        return True
    else:
        return False
    
#Convert a string to an array
def string_to_array(s):
    if s=="":
        return [""]
    else:
        s=s.split()
        return s
    
#Abbreviate a Two Word Name
def abbrev_name(name):
    name=name.split()
    name=list(name)
    return "{}.{}".format(name[0][0].upper(), name[1][0].upper())

#Sum Arrays
def sum_array(a):
    return sum(a)

#You only need one - Beginner
def check(seq, elem):
    return elem in seq