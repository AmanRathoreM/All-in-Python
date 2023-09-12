# Date 25-06-2021

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('dataset_tips.csv', usecols=['total_bill', 'sex', 'day'])
total_bill = data.total_bill.sort_values()

data = pd.read_csv('dataset_titanic.csv')

plt.figure(figsize=(16, 9))
sns.scatterplot(x='who',
                y='fare',
                hue='alive',
                data=data,
                style='alive',
                size='who',
                sizes=(100, 400),
                palette='coolwarm',
                alpha=.75)

plt.show()
