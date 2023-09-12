# Date 17-06-2021

import matplotlib.pyplot as plt

x = [743, 5578, 9135,  196, 9521,  4500, 1382, 1798,  4204, 3460, 7166]
y = [4478, 1642, 5931, 9837, 5631, 2322, 3691, 8593, 8720, 6191,  578]


x.sort()
y.sort()


plt.figure(facecolor='#94F008')
plt.gca().set_facecolor('#D98B8B')
plt.plot(x, y, label='First Plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Filling Background colors in MatPlotLib')
plt.legend()
plt.show()
