#Convert a string to an array
def string_to_array(s):
    if s=="":
        return [""]
    else:
        s=s.split()
        s=list(s)
        return s
    
#Convert a Number to a String!
def number_to_string(num):
    return str(num)

#Sum of positive
def positive_sum(arr):
    new=[]
    for i in arr:
        if i>0:
            new.append(i)
    return sum(new)

#Total amount of points
def points(games):
    count=0
    for i in games:
        if i[0]>i[2]:
            count+=3
        elif i[0]==i[2]:
            count+=1
    return count

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
  
#Counting Duplicates
def duplicate_count(text):
    text=text.lower()
    count={i: text.count(i) for i in set(text)}
    count=sorted(count.values())
    result=0
    for i in count:
        if i>1:
            result+=1
    return result