import matplotlib.pyplot as plt
import numpy as np

x = ["Student1", "Student2", "Student3", "Student4"]
y = np.array([9, 7, 8, 10])

# plt.bar(x, y, color="#157766", width=0.4)

# Instead of vertical bars, we can also use horizontal bars with barh():
# This time, we use height instead of width:
plt.barh(x, y, color="#157766", height=0.2)

dict1 = {"size": 15, "color": "#848221"}
dict2 = {"size": 20, "color": "#198021"}

plt.xlabel("Grades", fontdict=dict1)
plt.ylabel("Student names", fontdict=dict1)
plt.suptitle("Students and their grades")

plt.show()