def multiply(a, b):
    return a * b

def even_or_odd(number):
    if number%2==0:
        return "Even"
    else:
        return "Odd"

def number_to_string(num):
    return str(num)

def opposite(number):
    return -1*number

def solution(string):
    return string[::-1]

def make_negative( number ):
    if number>0:
        return -1*number
    else:
        return number

def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"
    
def positive_sum(arr):
    sum=0
    for num in arr:
        if num>0:
            sum+=num
    return sum

def repeat_str(repeat, string):
    return repeat*string

def remove_char(s):
    return s[1:-1]

def square_sum(numbers):
    return sum([num*num for num in numbers])

def find_smallest_int(arr):
    return min(arr)

def summation(num):
    total=0
    for x in range(0, num):
        total+=x+1
    return total

def greet():
    return "hello world!"