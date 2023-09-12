# Date 20-06-2021

import matplotlib.pyplot as plt
import numpy as np

ax1 = plt.axes(projection='3d')

x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [5, 6, 7, 8, 2, 5, 6, 3, 7, 2]
z1 = np.zeros(10)
x2 = np.ones(10)
y2 = np.ones(10)
z2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ax1.bar3d(x1, y1, z1, x2, y2, z2, color='r', alpha=.6)


plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend(title='3D Bars')

plt.show()
