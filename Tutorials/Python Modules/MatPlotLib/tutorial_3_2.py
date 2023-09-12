# Date 16-06-2021

import matplotlib.pyplot as plt

ages = [84,  40,  23,  44,  91,  36,  60,  94,  72,  39,  32,   5, 119,
        61, 127,  76,  61,  92,  41,  18,  12,  55, 117,  90,  47,  70,
        108,  97,   8,  40,  34,  43, 130, 109, 129, 115,  64, 113,  99,
        61,  10,   7,  38,  53, 124,  80,  46,  60,  48,  61, 102,  31,
        4, 100,  30,  99, 115, 114,  19, 9]


how_many_people_exists_of_that_age = [
    0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

plt.hist(ages, how_many_people_exists_of_that_age,
         histtype='bar', rwidth=0.9, color='#BC0786')

plt.xlabel('Ages')
plt.ylabel('People Exists')
plt.title('Histogram')
# plt.legend()
plt.show()
