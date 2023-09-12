# Date 18-06-2021

import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([6326, 1061, 5255, 9910, 4032, 5036, 1182, 6432, 8997, 3161, 9249,
               1871, 6866, 6700,  798, 5905,  690, 1571,  740,  720, 5629, 3075,
               6868, 4888, 4418, 1278, 9617, 6777, 1809, 3898])
y1 = np.array([9699, 7403, 3863, 9333,  154, 5663, 6085, 9799, 3294, 8701, 3536,
               6394, 4080, 1099, 2709, 6328, 1252, 6028,  105, 5719, 9252, 3958,
               4282, 5450, 2109, 9304, 4491, 7527, 7671, 5623])

x2 = np.array([313, 2647, 7225, 2046, 4713, 6821, 8139, 3050, 2013, 3015, 6815,
               4368, 3230, 7745, 7966, 4053, 4717, 4016, 1376,  653, 4085,  480,
               7399, 5362,  653, 1794, 7507, 5403, 9313, 9741])
y2 = np.array([7971, 4700, 5357, 7873, 2221, 3902, 2987, 3787, 5352, 4755,  952,
               4267, 3203, 9733, 8905, 8131, 6948,  303, 3423, 9987, 1383, 2936,
               4932, 2743, 3779,  322, 3930,  468, 6119, 1695])

x1.sort()
x2.sort()

font_dict = {
    'size': 15,
    'family': 'serif',
    'color': '#6b665e',
    'rotation': 45
}

plt.text(x2[1]-500, y2[1]-300, 'A text', fontdict=font_dict)
plt.text(-1000, 0, 'A Copyright', fontdict=font_dict,
         alpha=.38, size=200, rotation=20)

plt.style.use('fivethirtyeight')
plt.plot(x1, y1, label='First Plot')
plt.plot(x2, y2, label='Second Plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Basic Annonation in MatPlotLib')
plt.legend()
plt.show()
