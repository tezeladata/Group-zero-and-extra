import math

def continued_fraction(x,y,length_tolerance):
    output = []
    big = max(x,y)
    small = min(x,y)

    while small > 0 and len(output) < length_tolerance:
        quotient = math.floor(big/small)
        output.append(quotient)
        new_small = big % small
        big = small
        small = new_small

    return output

# We can also implement function to get number from fraction array
def get_number(continued_fraction):
    index = -1
    number = continued_fraction[index]

    while abs(index) < len(continued_fraction):
        next = continued_fraction[index - 1]
        number = 1/number + next
        index -= 1

    return number

print(get_number(continued_fraction(105, 33, 20)))