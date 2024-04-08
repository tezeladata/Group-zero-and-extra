import matplotlib.pyplot as plt
import numpy as np


def num_pow(n, decision):
    res_arr = np.array([])
    if decision == "increase":
        for i in range(n+1):
            res_arr = np.append(res_arr, 2**i)
    elif decision == "decrease":
        for i in range(n, -1, -1):
            res_arr = np.append(res_arr, 2**i)
    else:
        return "Incorrect decision"
    return res_arr

arr1 = num_pow(4, "increase")
arr2 = num_pow(4, "decrease")
arr3 = num_pow(6, "increase")
arr4 = num_pow(6, "decrease")
arr5 = num_pow(8, "increase")
arr6 = num_pow(8, "decrease")

plt.plot(arr1, '.--k', ms=20, mec="c", mfc="g", c="#123")
plt.plot(arr2, '.--c', ms=10, mec="c", mfc="g", c="#277")
plt.plot(arr3, '.--k', ms=20, mec="c", mfc="g", c="#123")
plt.plot(arr4, '.--c', ms=10, mec="c", mfc="g", c="#277")
plt.plot(arr5, '.--k', ms=20, mec="c", mfc="g", c="#123")
plt.plot(arr6, '.--c', ms=10, mec="c", mfc="g", c="#277")

dict1 = {"family": "sans", "color": "#999555", "size": 25}
dict2 = {"family": "sans", "color": "#555999", "size": 25}

plt.xlabel("Power", fontdict=dict1)
plt.ylabel("Value", fontdict=dict2)
plt.title("Powers of two")

# With Pyplot, you can use the grid() function to add grid lines to the plot.
# plt.grid()
# You can use the axis parameter in the grid() function to specify which grid lines to display.
# plt.grid(axis="x")
# plt.grid(axis="y")

# We can also set line properties for grid lines
plt.grid(color="#123234", ls="--", lw="1")
plt.show()