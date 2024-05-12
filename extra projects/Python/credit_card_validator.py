def validate(n):
    first_list = [int(i) for i in str(n)]
    
    if len(first_list) % 2 == 0:
        renewed = [first_list[i] * 2 if i % 2 == 0 else first_list[i] for i in range(len(first_list))]
    else:
        renewed = [first_list[i] * 2 if i % 2 != 0 else first_list[i] for i in range(len(first_list))]
        
    for i in range(len(renewed)):
        num = renewed[i]
        
        while num > 9:
            num = num - 9 if num > 9 else num
        renewed[i] = num
            
    return sum(renewed) % 10 == 0