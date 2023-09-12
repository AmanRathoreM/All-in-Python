# Date 16-06-2021

import matplotlib.pyplot as plt

x = [1,  2,  3,  4,   5, 6, 7]
y = [1,  2,  3,  4,   5, 6, 7]


x2 = [1,  2,  3,  4,   5, 6, 7]
y2 = [0,  1,  2,  3,   4, 5, 6]


plt.plot(x, y, label='First Plot')
plt.plot(x2, y2, label='Second Plot')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('This is a title\nSub title')
plt.legend()
plt.show()
