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

#Human readable duration format
units={
    "year": 60*60*24*365,
    "day": 60*60*24,
    "hour": 60*60,
    "minute": 60,
    "second": 1,
    }
def format_duration(seconds):
    if not seconds: return "now"
    result=[]
    for unit, value in units.items():
        count, seconds= divmod(seconds, value)
        if count==1: result.append(f"{count} {unit}")
        if count>1: result.append(f"{count} {unit}s")
    *body, tail = result
    #body now is anything else than tail
    if not body: return tail
    return f"{', '.join(body)} and {tail}" if tail else body

#Extract the domain name from a URL
def domain_name(url):
    without_scheme = url.split('://', 1)[-1]
    without_scheme=without_scheme.split(".")
    if without_scheme[0]=="www":
        return str(without_scheme[1])
    else:
        return str(without_scheme[0])

#Stop gninnipS My sdroW!
def spin_words(sentence):
    sentence=sentence.split()
    for i in range(len(sentence)):
        if len(sentence[i])>=5:
            sentence[i]=sentence[i][::-1]
    return " ".join(sentence)

#UEFA EURO 2016
def uefa_euro_2016(teams, scores):
    for i in scores:
        if scores[0]>scores[1]:
            return "At match {} - {}, {} won!".format(teams[0], teams[1], teams[0])
        elif scores[0]==scores[1]:
            return "At match {} - {}, teams played draw.".format(teams[0], teams[1])
        else:
            return "At match {} - {}, {} won!".format(teams[0], teams[1], teams[1])
        
#They say that only the name is long enough to attract attention. They also said that only a simple Kata will have someone to solve it. This is a sadly story #1: Are they opposite?
def is_opposite(s1,s2):
    if s1=="" and s2=="":
        return False
    else:
        if s1.swapcase()==s2:
            return True
        else:
            return False    
        
#Pirates!! Are the Cannons ready!??
def cannons_ready(gunners):
    for key, value in gunners.items():
        if value=="nay": return 'Shiver me timbers!'
        else: 'Fire!'
    return "Fire!"

#NBA full 48 minutes average
def nba_extrap(ppg, mpg):
    mpg_48=ppg*(48/mpg)
    return round(mpg_48, 1)

#Ensure question
def ensure_question(s):
    if s=="":
        return "?"
    else:
        if s[-1]!="?": 
            return s+"?"
        else: 
            return s
        
#For Twins: 2. Math operations
def ice_brick_volume(radius, bottle_length, rim_length):
    return (bottle_length-rim_length)*radius*radius*2