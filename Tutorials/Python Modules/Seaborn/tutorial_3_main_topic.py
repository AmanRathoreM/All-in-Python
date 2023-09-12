# Date 24-06-2021

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('dataset_tips.csv', usecols=['total_bill', 'size', 'sex'])

plt.figure(figsize=(16, 9))
sns.lineplot(x='size', y='total_bill', data=data, hue='sex',
             style='sex', palette='hot', dashes=False, markers=['o', 'v'])
plt.xlabel('X Axis', size=20, rotation=45, c='deepskyblue')
plt.ylabel('Y Axis')
plt.title('Line Plot')

plt.show()
