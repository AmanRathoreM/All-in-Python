# Date 17-06-2021

import matplotlib.pyplot as plt

x = [196, 743, 1382, 1798, 3460, 4204, 4500, 5578, 7166, 9135, 9521]
y = [578, 1642, 2322, 3691, 4478, 5631, 5931, 6191, 8593, 8720, 9837]


plt.plot(x, y, label='First Plot', color='b')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Borders Customization')
# plt.tight_layout()
plt.gca().spines['left'].set_color('#D35CDB')
plt.gca().spines['left'].set_linewidth(16)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_color('#0AD11B')
plt.gca().spines['bottom'].set_color('#C9BD0A')

plt.fill_between(x, y, 6500, color="#BAAAE6", alpha=0.25)
# plt.legend()
plt.show()
