# Date 19-06-2021

import matplotlib.pyplot as plt
import numpy as np


def x(max_value=9999, i=30):
    arr = np.random.randint(max_value, size=i)
    arr.sort()
    return arr


def y(max_value=9999, i=30): return np.random.randint(max_value, size=i)


plt.subplot(2, 3, 1)
plt.plot(x(1000), y(1000), color='r', alpha=.6)
plt.title('Subplot 1')
plt.subplot(2, 3, 2)
plt.plot(x(2000), y(2000), color='g', alpha=.5)
plt.title('Subplot 2')
plt.subplot(2, 3, 3)
plt.plot(x(3000), y(3000), color='y')
plt.title('Subplot 3')
plt.subplot(2, 3, 4)
plt.plot(x(4000), y(4000), color='y')
plt.title('Subplot 4')
plt.subplot(2, 3, 5)
plt.plot(x(5000), y(5000), color='y')
plt.title('Subplot 5')
plt.subplot(2, 3, 6)
plt.plot(x(6000), y(6000), color='y')
plt.title('Subplot 6')
plt.show()
