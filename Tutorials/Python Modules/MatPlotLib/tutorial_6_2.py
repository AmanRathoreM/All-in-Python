# Date 16-06-2021

'''
let's make a pie chart of the following data
study           04
sleep           11
programming     05
eating          03
exercise        01
total           24
'''

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

data = [4, 11, 5, 3, 1]
data_is_of_what = ['Study', 'Sleep', 'Programming', 'Eating', 'Exercise']

colours = ['#A8FC00', '#00C5FC', '#EF4AA5', '#6BB7EA', '#48DBAF']

plt.pie(data,
        labels=data_is_of_what,
        colors=colours,
        startangle=90,
        shadow=True,
        autopct='%1.2f%%',
        explode=(0, 0, 0, .09, 0))


plt.title('Pie Chart')
# plt.legend()
plt.show()
