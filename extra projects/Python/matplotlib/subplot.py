import matplotlib.pyplot as plt
import numpy as np

arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])

def add_items(array, n):
    if n%2==0:
        for i in range(n+1):
            array = np.append(array, 5*i)
    else:
        for i in range(2*(n-1)):
            array = np.append(array, -1*(3*i))
    return array

arr1 = add_items(arr1, 10)
arr2 = add_items(arr2, 3)
arr3 = add_items(arr3, 5)
arr4 = add_items(arr4, 8)

dict1 = {"family": "sans", "size": "15", "color": "#123987"}

# With the subplot() function you can draw multiple plots in one figure:
plt.subplot(1, 2, 1)
# Main figure has 1 row, 2 columns, this plot is first
plt.plot(arr1, '.--k', ms=10, mec="c", mfc="g", c="#124599", lw="2")
plt.plot(arr2, '.--k', ms=10, mec="c", mfc="g", c="#848484", lw="2")

plt.xlabel("Multiply by", fontdict=dict1)
plt.ylabel("Multiples of five", fontdict=dict1)
plt.title("Simple arrays", loc="left")

# Second subplot
plt.subplot(1, 2, 2)
# Last 2 is index of this plot
plt.plot(arr3, '.--k', ms=10, mec="c", mfc="g", c="#155555", lw="2")
plt.plot(arr4, '.--k', ms=10, mec="c", mfc="g", c="#645364", lw="2")


plt.xlabel("Multiply by", fontdict=dict1)
plt.ylabel("Multiples of five", fontdict=dict1)
plt.title("Simple arrays", loc="right")


# You can add a title to the entire figure with the suptitle() function
plt.suptitle("Some graphs")


# plt.show is only called once:
plt.show()