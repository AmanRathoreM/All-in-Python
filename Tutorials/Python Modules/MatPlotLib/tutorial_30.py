# Date 20-06-2021


import matplotlib.pyplot as plt
import numpy as np


ax1 = plt.axes(projection='3d')


def x(max_value=9999, i=30):
    arr = np.random.randint(max_value, size=i)
    arr.sort()
    return arr


def y_and_z(max_value=9999, i=30): return np.random.randint(
    max_value, size=i)


ax1.scatter3D(x(), y_and_z(), y_and_z(), color='teal',
              label='3d Scatter Plot 1', marker='$@$', s=302)

ax1.scatter3D(x(), y_and_z(), y_and_z(), color='deepskyblue',
              label='3d Scatter Plot 2', marker='*', s=302)

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend(title='3D ScatterPlots', labelspacing=2)

plt.show()
