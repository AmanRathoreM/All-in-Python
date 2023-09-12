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

# plt.figure(figsize=(16, 9))
sns.pairplot(dataset_breast_cancer_data_frame,
             hue='target',
             palette='viridis_r')

plt.show()
