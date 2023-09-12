# Date 24-06-2021

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('dataset_tips.csv', usecols=['total_bill', 'size'])

sns.lineplot(x='size', y='total_bill', data=data)

plt.show()
