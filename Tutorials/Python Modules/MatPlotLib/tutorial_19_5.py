# Date 19-06-2021

import matplotlib.pyplot as plt
import numpy as np


def x(max_value=9999, i=30):
    arr = np.random.randint(max_value, size=i)
    arr.sort()
    return arr


def y(max_value=9999, i=30): return np.random.randint(max_value, size=i)


plt.subplot(2, 2, 1)
plt.plot(x(1000), y(1000), color='r', alpha=.6)
plt.title('Subplot 1')
plt.subplot(2, 2, 3)
plt.plot(x(2000), y(2000), color='y', alpha=.6)
plt.title('Subplot 2')
plt.subplot(1, 2, 2)
plt.plot(x(3000), y(3000), color='g', alpha=.6)
plt.title('Subplot 3')

plt.show()
