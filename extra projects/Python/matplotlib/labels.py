import matplotlib.pyplot as plt
import numpy as np

def tribonacci(signature, n):
    if n == 0:
        return []
    elif n == 1:
        return [signature[0]]
    elif n == 2:
        return signature[:2]
    else:
        res_arr = signature[:]
        num1 = signature[0]
        num2 = signature[1]
        num3 = signature[2]
        for i in range(3, n):
            num4 = num1 + num2 + num3
            num1 = num2
            num2 = num3
            num3 = num4
            res_arr.append(num4)
        return res_arr
    
signature = "0 1 1"
final_signature = signature.split(" ")
final_signature = [int(x) for x in final_signature]

def fibonacci(range_for_fib):
    sequence = [0, 1]
    n1 = 0
    n2 = 1
    for i in range(2, range_for_fib):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        sequence.append(n3)
    return sequence
n = int(input("Enter how many elements you want in both sequences: "))

fib_seq = fibonacci(n)

x1 = np.arange(1, n+1)
y1 = np.array(tribonacci(final_signature, n))
x2 = np.arange(1, n+1)
y2 = np.array(fib_seq)
plt.plot(x1, y1, label='Tribonacci Sequence', c="#123456")
plt.plot(x2, y2, label='Fibonacci Sequence',  c="#654321")

# Adding labels and title:
# Also adding font styles for labels
font1 = {"family": "serif", "color": "red", "size": 10}
font2 = {"family": "serif", "color": "green", "size": 15}

plt.xlabel("Index", fontdict=font1)
plt.ylabel("Value", fontdict=font2)



# You can use the loc parameter in title() to position the title.
# Legal values are: 'left', 'right', and 'center'. Default value is 'center'.

plt.title("Fib vs trib", loc="right")
plt.show()