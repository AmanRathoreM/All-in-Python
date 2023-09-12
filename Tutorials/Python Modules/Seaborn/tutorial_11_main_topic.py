# Date 26-06-2021

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
# * You will need a internet connection to do the following line so
from sklearn.datasets import load_breast_cancer
dataset_breast_cancer = load_breast_cancer()


dataset_breast_cancer_data_frame = pd.DataFrame(np.c_[dataset_breast_cancer['data'], dataset_breast_cancer['target']],
                                                columns=np.append(dataset_breast_cancer['feature_names'], ['target']))

dataset_breast_cancer_data_frame_corelation = dataset_breast_cancer_data_frame.corr()

plt.figure(figsize=(16, 9))
sns.heatmap(dataset_breast_cancer_data_frame_corelation,
            annot=True, cmap='CMRmap_r', lw=2)
plt.title('Corelation Heat Map', size=40)

plt.xticks(rotation=50, size=7.2)

plt.show()
