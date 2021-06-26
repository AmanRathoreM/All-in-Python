## <h1 style="text-align:center; font-size:360%; font-family:verdana;color:#4A3E76;"><em>Seaborn</em></h1>

# These tutorials are watched from [**_Indian AI Production_**](https://www.youtube.com/channel/UCNzs7V6xG5GO0i_i6Grojyw "Clike here to checkout his channel") YouTube channel from [**_Seaborn Playlist_**](https://youtube.com/playlist?list=PLfP3JxW-T70HaBYwsSDadlS3v2VeALgYh "Clike here to check out his Seaborn tutorials Playlist")

---

---

---

---

---

## Tutorial 2

## In this tutorial we will deal with [**_Seaborn Line Plot_**](tutorial_2.ipynb "Clike here to see full Jupyter file")

```
# Date 24-06-2021

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('dataset_tips.csv', usecols=['total_bill', 'size'])

sns.lineplot(x='size', y='total_bill', data=data)

plt.show()
```

## Output of the above code is

## ![Introduction and Line](tutorial_2_main_topic.svg "This is an example of line graph in Seaborn")

---

---

---

## Tutorial 3

## In this tutorial we will deal with [**_Seaborn Line Plot_**](tutorial_3.ipynb "Clike here to see full Jupyter file")

```
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
```

## Output of the above code is

## ![Introduction and Line](tutorial_3_main_topic.svg "This is an example of line graph in Seaborn")

---

---

## Tutorial 4

## In this tutorial we will deal with [**_Seaborn Line Plot_**](tutorial_4.ipynb "Clike here to see full Jupyter file")

```
# Date 24-06-2021

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('dataset_tips.csv', usecols=['tip'])

sns.displot(data['tip'], kind='hist', rug=True, kde=True,
            color='#FF668F', aspect=2.5, label='Tips Given by Customers')
plt.legend()

plt.show()
```

## Output of the above code is

## ![Introduction and Line](tutorial_4_main_topic.svg "This is an example of line graph in Seaborn")

---

---

## Tutorial 5

## In this tutorial we will deal with [**_Seaborn Line Plot_**](tutorial_5.ipynb "Clike here to see full Jupyter file")

```
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
```

## Output of the above code is

## ![Introduction and Line](tutorial_5_main_topic.svg "This is an example of line graph in Seaborn")

---

---

## Tutorial 6

## In this tutorial we will deal with [**_Seaborn Line Plot_**](tutorial_6.ipynb "Clike here to see full Jupyter file")

```
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
```

## Output of the above code is

## ![Introduction and Line](tutorial_6_main_topic.svg "This is an example of line graph in Seaborn")

---

---

## Tutorial 7

## In this tutorial we will deal with [**_Seaborn Line Plot_**](tutorial_7.ipynb "Clike here to see full Jupyter file")

```
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
```

## Output of the above code is

## ![Introduction and Line](tutorial_7_main_topic.svg "This is an example of line graph in Seaborn")

---

---

## Tutorial 8

## In this tutorial we will deal with [**_Seaborn Line Plot_**](tutorial_8.ipynb "Clike here to see full Jupyter file")

```
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
```

## Output of the above code is

## ![Introduction and Line](tutorial_8_main_topic.svg "This is an example of line graph in Seaborn")

---

---

## Tutorial 9

## In this tutorial we will deal with [**_Seaborn Line Plot_**](tutorial_9.ipynb "Clike here to see full Jupyter file")

```
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

plt.figure(figsize=(16, 9))
sns.heatmap(data_2, cmap='hot', annot=True)

plt.show()
```

## Output of the above code is

## ![Introduction and Line](tutorial_9_main_topic.svg "This is an example of line graph in Seaborn")

---

---

## Tutorial 10

## In this tutorial we will deal with [**_Seaborn Line Plot_**](tutorial_10.ipynb "Clike here to see full Jupyter file")

```
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
```

## Output of the above code is

## ![Introduction and Line](tutorial_10_main_topic.svg "This is an example of line graph in Seaborn")

---

## Tutorial 11

## In this tutorial we will deal with [**_Seaborn Line Plot_**](tutorial_11.ipynb "Clike here to see full Jupyter file")

```
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
```

## Output of the above code is

## ![Introduction and Line](tutorial_11_main_topic.svg "This is an example of line graph in Seaborn")

---

## Tutorial 12

## In this tutorial we will deal with [**_Seaborn Line Plot_**](tutorial_12.ipynb "Clike here to see full Jupyter file")

```
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
```

## Output of the above code is

![Introduction and PairPlots/SubPlots](tutorial_12_main_topic.svg "This is an example of line graph in Seaborn")

## [**_Click here to see Image_**](tutorial_12_main_topic.svg "Clike here to see full image; if image is not able to render file")
