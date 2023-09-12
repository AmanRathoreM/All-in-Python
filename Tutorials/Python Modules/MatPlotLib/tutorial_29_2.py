# Date 19-06-2021


import matplotlib.pyplot as plt
import numpy as np


ax1 = plt.axes(projection='3d')


x = np.linspace(100, 1100, 100)
y = np.cos(x)
z = np.sin(x)

ax1.plot3D(x, y, z, color='r', label='3d Plot')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()

plt.show()
