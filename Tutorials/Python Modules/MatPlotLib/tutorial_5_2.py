# Date 16-06-2021

import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]

playing = [7,  9, 14, 9, 13,  4,  7]
eating = [5, 1, 1, 3, 5, 4, 3]
working = [14,  7,  6, 14, 11,  7,  7]
programming = [1, 1, 4, 1, 3, 4, 2]
sleeping = [5,  11,  8,  6, 10, 11,  9]

width = 7

plt.plot([], [], color='#A8FC00', label='programming', linewidth=width)
plt.plot([], [], color='#00C5FC', label='playing', linewidth=width)
plt.plot([], [], color='#EF4AA5', label='eating', linewidth=width)
plt.plot([], [], color='#6BB7EA', label='working', linewidth=width)
plt.plot([], [], color='#48DBAF', label='sleeping', linewidth=width)

plt.stackplot(days, programming, playing, eating, working,
              sleeping, colors=['#A8FC00', '#00C5FC', '#EF4AA5', '#6BB7EA', '#48DBAF'])

plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Stack Plots')
plt.legend()
plt.show()
