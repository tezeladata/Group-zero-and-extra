import matplotlib.pyplot as plt
import numpy as np


y_row = np.array([1, 2, 4, 8, 16, 32, 64])

# You can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line
# plt.plot(y_row, ls = "dotted")
# plt.plot(y_row, ls="dashed")


# linestyle can be written as ls.
# 'solid' (default)	'-'	
# 'dotted'	':'	
# 'dashed'	'--'	
# 'dashdot'	'-.'	
# 'None'	'' or ' '

# You can use the keyword argument color or the shorter c to set the color of the line
# plt.plot(y_row, '.--k', c="c", ls="--", ms=20, mec="c", mfc="g")

# We can use hex values for line color.
# We change line width using lw / linewidth
# plt.plot(y_row, c="#0F5132", lw="5")


# We can use multiple plt.plot()-s to have many lines
# row1 = [1, 2, 3, 4, 5, 6]
# row2 = [6, 5, 4]

# plt.plot(row1, c="#FF5733", lw="4", ls="--")
# plt.plot(row2, c="#FF9733", lw="3", ls=":")


# x1 = np.array([0, 1, 2, 3])
# y1 = np.array([3, 8, 1, 10])
# x2 = np.array([0, 1, 2, 3])
# y2 = np.array([6, 2, 7, 11])
# x3 = np.array([10, 4, 2, 7])
# y3 = np.array([1, 4, 3, 2])
# x4 = np.array([3, 2, 1, 0])
# y4 = np.array([10, 30, 1, 1])

# x and Y are names of variables, so program will work like - x,y   x,y
# plt.plot(x1, y1, x2, y2, x3, y3, x4, y4)
# plt.show()