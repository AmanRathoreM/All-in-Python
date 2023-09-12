# Date 16-06-2021

import matplotlib.pyplot as plt

x = [0, -8,  3,  6, -6,  1,  8,  0, -7,  3]
y = [2, -8, -6,  7, -2,  9, 10, -3, -1, -6]
x2 = [8, 2,  1]
y2 = [-9, 5, -1]

# [ 0, -8,  3,  6, -6,  1,  8,  0, -7,  3]
# [ 2, -3, -2, -9,  5,  4,  8,  0, -3, -1]

plt.scatter(x, y, color='#1BE82C', marker=',', s=100)
plt.scatter(x2, y2, color='r', marker='*', s=100)
#! plt.scatter(x, y, lable='skitscat', color='#1BE82C')

plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Scatter Plots')
# plt.legend()
plt.show()
