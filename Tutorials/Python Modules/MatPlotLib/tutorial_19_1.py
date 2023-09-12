# Date 19-06-2021

import matplotlib.pyplot as plt
import numpy as np


def x(max_value=9999, i=30):
    arr = np.random.randint(max_value, size=i)
    arr.sort()
    return arr


def y(max_value=9999, i=30): return np.random.randint(max_value, size=i)


plt.subplot(3, 1, 1)
plt.plot(x(500), y(500), color='r', alpha=.6)
plt.title('Subplot 1')
plt.subplot(3, 1, 2)
plt.plot(x(5000), y(5000), color='g', alpha=.5)
plt.title('Subplot 2')
plt.subplot(3, 1, 3)
plt.plot(x(50000), y(50000), color='y')
plt.title('Subplot 3')
plt.show()
