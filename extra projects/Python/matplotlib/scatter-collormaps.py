import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

# At this instance, numbers represent values in collormap
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap="viridis")

# You can include the colormap in the drawing by including the plt.colorbar() statement
plt.colorbar()

plt.show()


# Best colormaps:
# viridis
# cividis
# cividis_r
# inferno
# Greens 
# Reds
# YlGn
# OrRd
# Greys
# nipy_spectral