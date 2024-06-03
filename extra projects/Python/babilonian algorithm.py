import matplotlib.pyplot as plt
import numpy as np

def square_root(x, error_tolerance=0.0000001):
    y = x / 2
    numbers = [y]
    
    our_error = error_tolerance * 2
    while our_error > error_tolerance:
        z = x / y
        y = (y + z) / 2
        our_error = abs(y**2 - x)

        numbers.append(y) 
    
    return y, numbers

number = int(input("Enter whole number to find its square root: "))
result, numbers_plot = square_root(number)


plt.plot(numbers_plot)
plt.xlabel('Iterations')
plt.ylabel('Value of y')
plt.title('Convergence of square root estimation')
plt.show()

print("Square root:", result)