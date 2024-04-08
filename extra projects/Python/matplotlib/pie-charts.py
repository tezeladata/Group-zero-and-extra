import matplotlib.pyplot as plt
import numpy as np

arr1 = np.array([10, 20, 30, 30])

# adding labels
arr2 = ["Item1", "Item2", "Item3", "Item4"]

# Adding wedge - items will stand out
arr3 = [0.2, 0.2, 0.2, 0.2]

# Manually adding colors
arr4 = ["#039304", "#232543", "#345345", "#234232"]

# Using pie() to have pie chart
# Also adding startangle
# To use wedge, we write explode
# We can also add shadows
plt.pie(arr1, labels=arr2, startangle=90, explode=arr3, shadow=True, colors=arr4)

# Adding legend, also title to it
plt.legend(title="items")

plt.show()