# Date 16-06-2021

import matplotlib.pyplot as plt

x = [8,   0,   2,  5,   7]
y = [3,   6,   2,  5,  10]

x2 = [8,  10,   5,  6,   3]
y2 = [8,  4,   6,  2, 4]


plt.bar(x, y, label='Graph 1', color='g')
plt.bar(x2, y2, label='Graph 2', color='r')

plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Bar Graphs')
plt.legend()
plt.show()
