#Reversing Words in a String
def reverse(st):
    st=st.split()
    st.reverse()
    return " ".join(st)

#Pillars
def pillars(num_pill, dist, width):
    if num_pill<=1:
        return 0
    else:
        return (num_pill-2)*width + (num_pill-1)*dist*100
    
#Dollars and Cents
def format_money(amount):
    dollar=int(amount)
    cent=str(int((amount-dollar)*100 +0.1))
    if len(cent)<1:
        cent="00"
    elif len(cent)<2:
        cent+="0"
    return "$" + str(dollar) + "." + cent

#Return to Sanity
def mystery():
    results = {
    'sanity': 'Hello'
    }
    return results

#String cleaning
def string_clean(s):
    new=""
    for i in s:
        if i not in "0123456789":
            new+=i
    return new

#Sum of differences in array
def sum_of_differences(arr):
    arr.sort(reverse=True)
    sum=0
    i=1-1
    if len(arr)==0:
        return 0
    else:
        while i!=len(arr)-1:
            sum=sum+(arr[i] - arr[i+1])
            i+=1
    return sum


#Simple Fun #1: Seats in Theater
def seats_in_theater(tot_cols, tot_rows, col, row):
    return ((tot_cols-col+1)*(tot_rows-row))

#Grasshopper - Array Mean
def find_average(nums):
    if len(nums)>=1:
        return sum(nums) / len(nums)
    else:
        return 0