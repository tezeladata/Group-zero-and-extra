import string

def generate_line(alphabet, size, i):
    first_half = '-'.join(alphabet[size-1:abs(i):-1])  # First half of the line
    second_half = '-'.join(alphabet[abs(i):size])     # Second half of the line
    return first_half + second_half                  # Combine both halves

def print_rangoli(size):
    alphabet = string.ascii_lowercase

    for i in range(size-1, -size, -1):
        line = generate_line(alphabet, size, i)
        center_length = size*4 - 3  # Length to center the line
        print(line.center(center_length, '-'))

print_rangoli(10)