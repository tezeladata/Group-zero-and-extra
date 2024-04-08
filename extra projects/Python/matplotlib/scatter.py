import matplotlib.pyplot as plt
import numpy as np

# With Pyplot, you can use the scatter() function to draw a scatter plot.

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.scatter(x, y, c= "#678910")

# We can also color each dot
colors = np.array(['#123456', '#3F7E82', '#B64F5A', '#8C9D40', '#7261AB', '#E3853C', '#549C8A', '#C17F4D', '#A0A136', '#4E6F8E', '#D16B7B', '#097343', '#239047', '#937492', '#433434'])

# We can also adjust sizes of markers:
sizes = np.array([10, 20, 30, 100, 200, 300, 150, 15, 250, 25, 350, 35, 50, 60, 80])

# c for colors and s for marker sizes
# We adjust transparency of colors with alpha
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)

dict1 = {"size": 15, "color": "red"}
dict2 = {"size": 20, "color": "red"}



plt.xlabel("Age of car", fontdict=dict1)
plt.ylabel("Speed of car", fontdict=dict1)
plt.title("Car speed dependence of it's age", fontdict=dict2)
plt.show()