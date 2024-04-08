# Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias
import matplotlib.pyplot as plt

# We also use numpy for data
import numpy as np

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])

# Plot
# plt.plot(xpoints, ypoints)
# plt.show()

# The plot() function is used to draw points (markers) in a diagram.
# Draw line from (3, 10) to (8, 20)
# x_row = np.array([3, 8])
# y_row = np.array([10, 20])
# plt.plot(x_row, y_row)

# To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.
# plt.plot(x_row, y_row, "o")

# If we want multiple marks, we can add xpoints to one array and ypoints to other
# x_row = np.array([0, 1, 2, 3, 4, 5, 6, 7])




# x_row = np.array(["Janezashvili", "Giorgelashvili", "Khoperia", "Zabakhidze", "Vanishvili", "Tinikashvili", "Grdzelishvili", "Vakhtangashvili"])
# y_row = np.array([65, 29.5, 13, 15, 15.5, 33.5, 24, 29])

# res_arr = []
# for i in range(len(x_row)):
#     new_arr = []
#     new_arr.append(x_row[i])
#     new_arr.append(y_row[i])
#     res_arr.append(new_arr)

# res_arr.sort(key=lambda x: x[1])

# sorted_x_row = np.array([])
# sorted_y_row = np.array([])

# for i in range(len(res_arr)):
#     sorted_x_row = np.append(sorted_x_row, res_arr[i][0])
#     sorted_y_row = np.append(sorted_y_row, res_arr[i][1])

# Better way to sort:
# indices = np.argsort(y_row)
# x_row = x_row[indices]
# y_row = y_row[indices]


# If we do not include x-axis, it will automaticly increase by one
y_row = np.array([10, 15, 10, 15, 10, 15])
plt.plot(y_row)
plt.show()