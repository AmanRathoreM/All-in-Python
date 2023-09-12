# Date 17-06-2021

import matplotlib.pyplot as plt

x = [743, 5578, 9135,  196, 9521,  4500, 1382, 1798,  4204, 3460, 7166]
y = [4478, 1642, 5931, 9837, 5631, 2322, 3691, 8593, 8720, 6191,  578]


x.sort()
y.sort()


plt.plot(x, y, label='First Plot', color='b')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Fill color under plot Customization in MatPlotLib')
# plt.tight_layout()
plt.fill_between(x, y, color='#BAAAE6')
# plt.legend()
plt.show()
