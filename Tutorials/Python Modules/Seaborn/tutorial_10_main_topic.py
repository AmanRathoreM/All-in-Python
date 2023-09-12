# Date 25-06-2021

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

rows_in_data_frame = 20
max_value_in_data_frame = 100  # use values of more than 11 (refrence arr06)
indeces = np.array(['arr01', 'arr02', 'arr03', 'arr04',
                   'arr05', 'arr06', 'arr07', 'arr08', 'arr09', 'arr10'])
arr01 = np.linspace(12, max_value_in_data_frame-.9, rows_in_data_frame)
arr02 = np.random.uniform(0, max_value_in_data_frame, rows_in_data_frame)
arr03 = np.linspace(.99, max_value_in_data_frame-50.9, rows_in_data_frame)
arr04 = np.random.uniform(0, max_value_in_data_frame, rows_in_data_frame)
arr05 = np.random.uniform(0, max_value_in_data_frame, rows_in_data_frame)
arr06 = np.linspace(.9, max_value_in_data_frame-10.99, rows_in_data_frame)
arr06 = np.sort(arr06)[::-1]
arr07 = np.linspace(.99, max_value_in_data_frame-.9, rows_in_data_frame)
arr08 = np.random.uniform(0, max_value_in_data_frame, rows_in_data_frame)
arr09 = np.random.uniform(0, max_value_in_data_frame, rows_in_data_frame)
arr10 = np.linspace(.99, max_value_in_data_frame-.9, rows_in_data_frame)
arr10 = np.sort(arr10)[::-1]
main_arr = np.vstack((arr01, arr02, arr03, arr04, arr05,
                     arr06, arr07, arr08, arr09, arr10))
data_2 = pd.DataFrame(main_arr).set_index(indeces)

annot_dict = {'fontsize': 12,
              'fontstyle': 'italic',
              'color': "#ff00f2",
              'alpha': 1,
              'rotation': 45,
              'verticalalignment': 'center'}

cbar_dict = dict(shrink=1.2,
                 orientation='horizontal',
                 drawedges=True,
                 ticks=np.linspace(0, max_value_in_data_frame, 30, dtype=int),
                 extend='min',
                 extendfrac=.2,)

plt.figure(figsize=(16, 9))
sns.heatmap(data_2,
            annot=True,
            annot_kws=annot_dict,
            linewidths=5,
            linecolor='#fa52f2',
            cmap='winter_r',
            xticklabels=np.arange(0, 10),
            yticklabels=['arrsekjdsfjhsjdfhsdf', 86254436954362523456],
            cbar_kws=cbar_dict)

plt.show()
