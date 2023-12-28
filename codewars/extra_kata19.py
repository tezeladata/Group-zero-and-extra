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