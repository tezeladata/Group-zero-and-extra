import numpy as np
import matplotlib.pyplot as plt

data = [
    
]

# Extracting individual lists from the data
names = [item[0] for item in data]
coefficients = [item[1] for item in data]
salaries = [item[2] for item in data]

# Plotting
plt.figure(figsize=(12, 8))
plt.barh(names, coefficients, color='#634234')
plt.xlabel('Work Coefficient')
plt.ylabel('Squad Leaders')
plt.title('Work Coefficient by Leader')
plt.suptitle("From best to worst")
plt.gca().invert_yaxis()
plt.grid(axis="x", lw=1)
plt.show()