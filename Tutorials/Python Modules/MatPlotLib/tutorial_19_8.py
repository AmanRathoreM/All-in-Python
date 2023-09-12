# Date 19-06-2021

import matplotlib.pyplot as plt
import numpy as np


def x(max_value=9999, i=30):
    arr = np.random.randint(max_value, size=i)
    arr.sort()
    return arr


def y(max_value=9999, i=30): return np.random.randint(max_value, size=i)


plt.subplot(4, 2, 1)
plt.plot(x(1000), y(1000), color='g', alpha=.6)
plt.title('Subplot 1')

plt.subplot(4, 2, 2)
plt.plot(x(2000), y(2000), color='y')
plt.title('Subplot 2')

plt.subplot(4, 2, 3)
plt.plot(x(4000), y(4000), color='m', alpha=.6)
plt.title('Subplot 3')

plt.subplot(4, 2, (4, 6))
plt.plot(x(5000), y(5000), color='teal')
plt.title('Subplot 4')

plt.subplot(4, 2, 5)
plt.plot(x(5000), y(5000), color='deepskyblue')
plt.title('Subplot 5')

plt.subplot(4, 1, 4)
plt.plot(x(3000), y(3000), color='r', alpha=.6)
plt.title('Subplot 6')

plt.tight_layout(pad=.6)

plt.show()
