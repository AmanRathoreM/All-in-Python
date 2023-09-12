# Date 24-06-2021

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('dataset_tips.csv', usecols=['tip'])

sns.displot(data['tip'], kind='hist', rug=True, kde=True,
            color='#FF668F', aspect=2.5, label='Tips Given by Customers')
plt.legend()

plt.show()
