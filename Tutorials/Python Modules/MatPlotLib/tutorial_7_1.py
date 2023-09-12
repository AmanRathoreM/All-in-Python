# Date 17-06-2021

import matplotlib.pyplot as plt


def seperate_x_y(file):

    file = str(file).replace('\'', '').replace(
        '\\n,', '|').replace(' ', '').replace('\n,', '|')

    file = file[:len(file)-3]
    file = file[1:len(file)].split('|')

    i = 0
    while (i < len(file)):
        x.append(int(str(file[i]).split(',')[0]))
        y.append(int(str(file[i]).split(',')[1]))
        i += 1


x = []
y = []

with open('tutorial_7_1.txt', 'r')as txt_file:
    file = txt_file.readlines()

seperate_x_y(file)


plt.plot(x, y,
         label='Line Graph Readed from \'.txt\' file')
plt.scatter(x[0], y[0],
            label='Starting Point')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Reading Data from txt file')
plt.legend()
plt.show()
