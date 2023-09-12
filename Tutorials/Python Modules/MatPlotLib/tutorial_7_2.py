# Date 17-06-2021

import matplotlib.pyplot as plt
import pandas as pd

# * array([[17, 11, 13, 13, 15, 19,  0,  1,  2, 11],
# *        [14,  7,  5,  8,  9, 15, 16, 13,  5,  9]])

data = pd.read_excel('tutorial_7_2.xlsx', 'Sheet1')

plt.plot(data['x axis'], data['y axis'], label='Line Graph Readed from Excel')
plt.scatter(data['x axis'][0], data['y axis'][0],
            label='Starting Point')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Reading Data from Excel')
plt.legend()
plt.show()
