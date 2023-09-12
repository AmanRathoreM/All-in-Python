# Date 25-06-2021

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data = pd.read_csv('dataset_tips.csv', usecols=['total_bill', 'sex', 'day'])
total_bill = data.total_bill.sort_values()


order = ['Sun', 'Thur', 'Fri', 'Sat']
sns.barplot(x='day',
            y='total_bill',
            hue='sex',
            data=data, capsize=.22,
            order=order,
            hue_order=['Female', 'Male'],
            estimator=np.min,
            ci=100,
            n_boot=100,
            palette='winter_r',
            saturation=20,
            errcolor='#B00B69',
            dodge=False)
plt.title('Bar Graph With Min Bill Values')

plt.show()
