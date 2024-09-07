# All of these operators share something in common -- they are "bitwise" operators.
# That is, they operate on numbers (normally), but instead of treating that number as if it were a single value, they treat it as if it were a string of bits, written in twos-complement binary.
# A two's complement binary is same as the classical binary representation for positve integers but is slightly different for negative numbers.
# Negative numbers are represented by performing the two's complement operation on their absolute value.

x = 7
y = 8
print(x << y)
# 7 * 2**8 = 1792

x = 10
y = 3
print(x << y)
# 10 * 2**3 = 80

# Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.


x = 200
y = 4
print(x >> y)
# 200 // 2**4 = 200 // 16 = 12

x = 10
y = 2
print(x >> y)

# Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.


x = 100
y = 10
print(x & y)
# None of corresponding bits are same and equal to 1 at the same time, so 0

x = 20
y = 20
print(x & y)
# both are same, so 20 again

# Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.


# x | y
# Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.
# ~ x
# Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.
# x ^ y
# Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.