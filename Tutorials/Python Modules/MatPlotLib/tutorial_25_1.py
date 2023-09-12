# Date 19-06-2021

import matplotlib.pyplot as plt
import numpy as np


def x(max_value=9999, min_value=0, i=200):
    arr = np.random.randint(min_value, max_value, size=i)
    arr.sort()
    return arr


def y(max_value=9999, min_value=0,  i=200): return np.random.randint(
    min_value, max_value, size=i)


plt.plot(x(1000), y(500), color='g', alpha=.6, label='0-500')
plt.plot(x(1000), y(1000, 500), color='m', alpha=.6, label='500-1000')
plt.plot(x(1000), y(1500, 1000), color='y', alpha=.6, label='1000-1500')
plt.plot(x(1000), y(2000, 1500), color='deepskyblue',
         alpha=.6, label='1500-2000')
plt.title('Custimizing Lengends')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.legend(loc='upper center', ncol=4, title='Legend Title',
           labelspacing=2)

plt.show()
