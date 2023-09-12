# Date 16-06-2021

import matplotlib.pyplot as plt

x = [0,  10,  -4,  -2,   5]
y = [1,   3,  -4, -5,   1]

x2 = [9, -10,   2,  -9,  -1]
y2 = [6,  -8,   7,  -1,  -3]


plt.plot(x, y, label='First Plot')
plt.plot(x2, y2, label='Second Plot')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('This is a title\nSub title')
plt.legend()
plt.show()
