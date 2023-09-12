# Date 25-06-2021

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data = pd.read_csv('dataset_tips.csv', usecols=['total_bill'])
total_bill = data.total_bill.sort_values()

bins = np.linspace(1, 55, 12, dtype=int)

customization = dict(color='deepskyblue', edgecolor='r',
                     lw=20, ls='--', alpha=.91)
sns.displot(total_bill, aspect=2.5, bins=bins, kde=True, **customization)
plt.xticks(bins)

plt.show()
