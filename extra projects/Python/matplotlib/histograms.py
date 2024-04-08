import matplotlib.pyplot as plt
import numpy as np

x2 = np.array([])
for i in range(100):
    x2 = np.append(x2, i**2)

# Then using hist function for histogram:
plt.hist(x2)

plt.show()