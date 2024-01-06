print("Hello, this is statistics calculator.")
def statistics_calc(user_input):
    number_list = [int(num) for num in user_input.split(",")]
    user_choice=input("Choose one from operations: mean, median, mode, range, variance - ")
    if user_choice=="mean":
        mean=sum(number_list)/len(number_list)
        return f"Mean of {user_input} is: \n{mean}"
    elif user_choice=="median":
        if len(number_list)%2!=0:
            pos=int((len(number_list)+1)/2)
            median=number_list[pos-1] 
            return f"Median of numbers: {user_input} is {median}"
        else:
            pos = len(number_list) // 2
            median = number_list[pos]
            return f"Median of numbers: {user_input} is {median}"
    elif user_choice=="mode":
        number_list.sort()
        l1=[]
        i=0
        while i<len(number_list):
            l1.append(number_list.count(number_list[i]))
            i+=1
        d1=dict(zip(number_list, l1))
        d2={k for (k,v) in d1.items() if v==max(l1)}
        d3=0
        for i in d2:
            d3+=i
        return f"Mode of numbers {user_input} is {d3}"
    elif user_choice=="range":
        range=max(number_list)-min(number_list)
        return f"Range of numbers {user_input} is {range}"
    elif user_choice=="variance" or user_choice=="var":
        average = sum(number_list) / len(number_list)
        variance = sum((x-average)**2 for x in number_list) / len(number_list)
        return f"Variance of numbers {user_input} is {variance}"
    else:
        return "Invalid operation"
print(statistics_calc(user_input=input("Enter numbers (with this way: num1, num2, num3, num4 and etc): ")))