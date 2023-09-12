# Date 25-06-2021

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('dataset_tips.csv', usecols=['total_bill', 'sex', 'day'])
total_bill = data.total_bill.sort_values()


fontdict = dict(c='#7408BB',
                fontsize=50,
                rotation=356,
                alpha=.5)

plt.figure(figsize=(16, 9),
           facecolor='#FFA3BB',
           edgecolor='#82B272')

sns.barplot(x='day',
            y='total_bill',
            hue='sex',
            data=data, capsize=.22,
            hue_order=['Female', 'Male'],
            ci=100,
            n_boot=100,
            palette='winter_r',
            saturation=20,
            errcolor='#B00B69',
            dodge=False)
plt.title('More in Bar Plot', fontdict=fontdict)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.show()
