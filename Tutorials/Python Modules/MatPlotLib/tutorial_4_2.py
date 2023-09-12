# Date 16-06-2021


import matplotlib.pyplot as plt
from random import shuffle
from random import randint as rd


def rd_color():

    random_number = rd(0, 16777215)
    hex_number = str(hex(random_number))
    hex_number = '#' + hex_number[2:]
    return hex_number


def sh():
    global x, y
    x_y_for_function = [1, -2, 3, -4, 5, -6, 7, -8,
                        9, -10, -1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
    shuffle(x_y_for_function)
    x = x_y_for_function[:10]
    shuffle(x_y_for_function)
    y = x_y_for_function[:10]


x = []
y = []


sh()
plt.scatter(x, y, color=rd_color(), marker='>', s=rd(30, 45))

sh()
plt.scatter(x, y, color=rd_color(), marker='<', s=rd(30, 45))

sh()
plt.scatter(x, y, color=rd_color(), marker='X', s=rd(30, 45))

sh()
plt.scatter(x, y, color=rd_color(), marker='x', s=rd(30, 45))

sh()
plt.scatter(x, y, color=rd_color(), marker='1', s=rd(30, 45))

sh()
plt.scatter(x, y, color=rd_color(), marker='4', s=rd(30, 45))

sh()
plt.scatter(x, y, color=rd_color(), marker='8', s=rd(30, 45))

sh()
plt.scatter(x, y, color=rd_color(), marker='s', s=rd(30, 45))

sh()
plt.scatter(x, y, color=rd_color(), marker='p', s=rd(30, 45))

sh()
plt.scatter(x, y, color=rd_color(), marker='$a$', s=rd(30, 45))

sh()
plt.scatter(x, y, color=rd_color(), marker='$Q$', s=rd(30, 45))

plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Scatter Plots')
#! plt.legend()
plt.show()
