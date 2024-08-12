import string
# For letter checking

def main(user_num, base_sys, pref_sys):
    '''
    This function will turn any base data into decimal pos. system and then into preferred system.
    '''
    # Convert to decimal
    if base_sys not in [2, 8, 10, 16] or pref_sys not in [2, 8, 10, 16]: return -1
    
    match base_sys:
        case 2 | 8 | 16:
            dec_val = system_to_dec(user_num, base_sys)
        case 10:
            dec_val = user_num

    # Convert to preferred system
    match pref_sys:
        case 2 | 8 | 16:
            return dec_to_system(dec_val, pref_sys)
        case 10:
            return dec_val


# bin, octal or hex into decimal system
def system_to_dec(num, system):
    '''
    system is which system the number is currently written in.
    For example, if the number is in octal, we pass the system argument as 8.
    '''

    num_str = str(num).upper() # uppercase for hexadecimal values
    st_pow = len(num_str) - 1
    res = []
    
    for i in num_str:
        if i in string.ascii_uppercase[:6]:  # A-F
            value = 10 + string.ascii_uppercase.index(i)
        else:
            value = int(i)
        
        res.append(value * system**st_pow)
        st_pow -= 1

    return sum(res)

# decimal to bin, octal or hex
def dec_to_system(num, system):
    if system not in [2, 8, 16]: return -1 

    digits = "0123456789ABCDEF"
    res = ""

    if num == 0: return "0"

    while num > 0:
        res += digits[num % system]
        num //= system
    
    res = res[::-1]
    return res


# run main function and print the output
print(main(user_num=input("Enter your number: "), base_sys=int(input("Which system is number currently written in? 2 | 8 | 10 | 16 - ")), pref_sys=int(input("Which system to convert in? 2 | 8 | 10 | 16 - "))))

# This code does not include error handling, make sure to input correctly