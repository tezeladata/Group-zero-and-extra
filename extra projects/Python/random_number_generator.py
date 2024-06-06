def feedback_shift(bits):
    xor_result = (bits[1] + bits[2]) % 2
    output = bits.pop()
    bits.insert(0, xor_result)
    return bits, output

def feedback_shift_list(bits_this):
    bits_output = [bits_this.copy()]
    random_output = []
    bits_next = bits_this.copy()
    
    while len(bits_output) < 2 ** len(bits_this):
        bits_next, next_output = feedback_shift(bits_next)
        bits_output.append(bits_next.copy())
        random_output.append(next_output) 

    return bits_output, random_output

# Example usage
bitslist, random_bits = feedback_shift_list([int(input("Enter 0/1: ")) for _ in range(int(input("How many elements do you want? (Min - 3) ")))])
random_numbers = int(("".join([str(i) for i in random_bits])), 2)

print("Random number:", random_numbers)