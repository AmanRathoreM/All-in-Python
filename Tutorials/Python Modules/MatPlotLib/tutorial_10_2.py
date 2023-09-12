# Date 17-06-2021

import matplotlib.pyplot as plt

x = [743, 5578, 9135,  196, 9521,  4500, 1382, 1798,  4204, 3460, 7166]
y = [4478, 1642, 5931, 9837, 5631, 2322, 3691, 8593, 8720, 6191,  578]


x.sort()
y.sort()


plt.plot(x, y, label='First Plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Grid Customization in MatPlotLib')
plt.legend()
plt.grid(color='#AC43CC', linestyle='--', linewidth=3)
plt.show()
