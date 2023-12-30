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

#Directions Reduction
def dir_reduc(arr):
    opp={"NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST": "WEST",
        "WEST": "EAST"}
    for i in range(len(arr)-1):
        if arr[i+1]==opp[arr[i]]:
            del arr[i], arr[i]
            return dir_reduc(arr)
    return arr

#Sort the odd
def sort_array(source_array):
    if not source_array:
        return []
    else:
        odd=sorted(x for x in source_array if x%2!=0)
        for i in range(len(source_array)):
            if source_array[i]%2!=0:
                source_array[i]=odd.pop(0)
        return source_array
    
#The Hashtag Generator
def generate_hashtag(s):
    if s=="":
        return False
    else:
        s=s.strip()
        s=s.split(" ")
        cap=[word.capitalize() for word in s]
        new_arr="#"
        for i in range(len(cap)):
            new_arr+=cap[i]
        if len(new_arr)>140:
            return False
        else:
            return new_arr
        
#Count the smiley faces!
def count_smileys(arr):
    smiley=[":)", ":D",";)",";D",":-)",":-D",";-D",";-)","~:)","~:D","~;)","~;D",":-)",":-D",";~)", ":~)", ";-D",";~D",":)",":-D",";~D"]
    count=0
    for i in arr:
        if i in smiley:
            count+=1
    return count