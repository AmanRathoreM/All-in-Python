# Pandas

## These tutorials are watched from [**_Udemy_**](https://www.udemy.com/ "Clike here to checkout Udemy Website") website from [**_Pandas tutorial by Alexander Hagmann_**](https://www.udemy.com/share/101WOgAEcdc1lXQH4B/ "Clike here to check out his Course")

---

---

---

---

---

## tutorial_3_1

### [Creating Data Frame](tutorial_PART_3_1.ipynb "Clike here to see full tutorial file")

<br>

```python
file = pd.read_csv('file_name.csv')
file
```

Output of the above code is
| | survived | pclass | sex | age | sibsp | parch | fare | embarked | deck |
|---------:|-------:|----:|----:|------:|------:|-----:|---------:|-----:|--:|
| 0 | 0 | 3 | male | 22.0 | 1 | 0 | 7.2500 | S | NaN |
| 1 | 1 | 1 | female | 38.0 | 1 | 0 | 71.2833 | C | C |
| 2 | 1 | 3 | female | 26.0 | 0 | 0 | 7.9250 | S | NaN |
| 3 | 1 | 1 | female | 35.0 | 1 | 0 | 53.1000 | S | C |
| 4 | 0 | 3 | male | 35.0 | 0 | 0 | 8.0500 | S | NaN |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 886 | 0 | 2 | male | 27.0 | 0 | 0 | 13.0000 | S | NaN |
| 887 | 1 | 1 | female | 19.0 | 0 | 0 | 30.0000 | S | B |
| 888 | 0 | 3 | female | NaN | 1 | 2 | 23.4500 | S | NaN |
| 889 | 1 | 1 | male | 26.0 | 0 | 0 | 30.0000 | C | C |
| 890 | 0 | 3 | male | 32.0 | 0 | 0 | 7.7500 | Q | NaN |

---

---

---

## tutorial_3_2

### [Some Options and Methods in Pandas](tutorial_PART_3_2.ipynb "Clike here to see full tutorial file")

<br>

```python
pd.options.display.max_rows
```

Output of the above code is

```console
60
```

---

---

<br>

```python
pd.options.display.min_rows
```

Output of the above code is

```console
20
```

---

---

<br>

```python
pd.options.display.min_rows = 40
```

---

---

<br>

```python
titanic_data_csv.head()
```

Output of the above code is
| | survived | pclass | sex | age | sibsp | parch | fare | embarked | deck |
|---------:|-------:|----:|----:|------:|------:|-----:|---------:|-----:|--:|
| 0 | 0 | 3 | male | 22.0 | 1 | 0 | 7.2500 | S | NaN |
| 1 | 1 | 1 | female | 38.0 | 1 | 0 | 71.2833 | C | C |
| 2 | 1 | 3 | female | 26.0 | 0 | 0 | 7.9250 | S | NaN |
| 3 | 1 | 1 | female | 35.0 | 1 | 0 | 53.1000 | S | C |
| 4 | 0 | 3 | male | 35.0 | 0 | 0 | 8.0500 | S | NaN |

---

---

<br>

```python
titanic_data_csv.tail()
```

Output of the above code is
| | survived | pclass | sex | age | sibsp | parch | fare | embarked | deck |
|---------:|-------:|----:|----:|------:|------:|-----:|---------:|-----:|--:|
| 886 | 0 | 2 | male | 27.0 | 0 | 0 | 13.0000 | S | NaN |
| 887 | 1 | 1 | female | 19.0 | 0 | 0 | 30.0000 | S | B |
| 888 | 0 | 3 | female | NaN | 1 | 2 | 23.4500 | S | NaN |
| 889 | 1 | 1 | male | 26.0 | 0 | 0 | 30.0000 | C | C |
| 890 | 0 | 3 | male | 32.0 | 0 | 0 | 7.7500 | Q | NaN |

---

---

<br>

```python
titanic_data_csv.tail(2)
```

Output of the above code is
| | survived | pclass | sex | age | sibsp | parch | fare | embarked | deck |
|---------:|-------:|----:|----:|------:|------:|-----:|---------:|-----:|--:|
| 889 | 1 | 1 | male | 26.0 | 0 | 0 | 30.0000 | C | C |
| 890 | 0 | 3 | male | 32.0 | 0 | 0 | 7.7500 | Q | NaN |

---

---

<br>

```python
titanic_data_csv.head(3)
```

Output of the above code is
Output of the above code is
| | survived | pclass | sex | age | sibsp | parch | fare | embarked | deck |
|---------:|-------:|----:|----:|------:|------:|-----:|---------:|-----:|--:|
| 0 | 0 | 3 | male | 22.0 | 1 | 0 | 7.2500 | S | NaN |
| 1 | 1 | 1 | female | 38.0 | 1 | 0 | 71.2833 | C | C |
| 2 | 1 | 3 | female | 26.0 | 0 | 0 | 7.9250 | S | NaN |

---

---

---

## tutorial_3_3

### [Data Inspection in Pandas](tutorial_PART_3_3.ipynb "Clike here to see full tutorial file")

<br>

```python
titanic_data_csv.info()
```

Output of the above code is

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 9 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   survived  891 non-null    int64
 1   pclass    891 non-null    int64
 2   sex       891 non-null    object
 3   age       714 non-null    float64
 4   sibsp     891 non-null    int64
 5   parch     891 non-null    int64
 6   fare      891 non-null    float64
 7   embarked  889 non-null    object
 8   deck      203 non-null    object
dtypes: float64(2), int64(4), object(3)
memory usage: 62.8+ KB
```

---

---

<br>

```python
titanic_data_csv.describe()
```

Output of the above code is
| | survived | pclass | age | sibsp | parch | fare |
| ----- | ---------: | ---------: | ---------: | ---------: | ---------: | ---------: |
| count | 891.000000 | 891.000000 | 714.000000 | 891.000000 | 891.000000 | 891.000000 |
| mean | 0.383838 | 2.308642 | 29.699118 | 0.523008 | 0.381594 | 32.204208 |
| std | 0.486592 | 0.836071 | 14.526497 | 1.102743 | 0.806057 | 49.693429 |
| min | 0.000000 | 1.000000 | 0.420000 | 0.000000 | 0.000000 | 0.000000 |
| 25% | 0.000000 | 2.000000 | 20.125000 | 0.000000 | 0.000000 | 7.910400 |
| 50% | 0.000000 | 3.000000 | 28.000000 | 0.000000 | 0.000000 | 14.454200 |
| 75% | 1.000000 | 3.000000 | 38.000000 | 1.000000 | 0.000000 | 31.000000 |
| max | 1.000000 | 3.000000 | 80.000000 | 8.000000 | 6.000000 | 512.329200 |

---

---

<br>

```python
titanic_data_csv.describe(include='O')
```

Output of the above code is
| | sex | embarked | deck |
|:------:|:----:|:--------:|:----:|
| count | 891 | 889 | 203 |
| unique | 2 | 3 | 7 |
| top | male | S | C |
| freq | 577 | 644 | 59 |

---

---

---

## tutorial_3_4

### [Build-in Functions and Methods in Pandas](tutorial_PART_3_4.ipynb "Clike here to see full tutorial file")

<br>

```python
round(titanic_data_csv,3)
```

Output of the above code is

|     | survived | pclass |  sex   | age  | sibsp | parch |  fare  | embarked | deck |
| :-: | :------: | :----: | :----: | :--: | :---: | :---: | :----: | :------: | :--: |
|  0  |    0     |   3    |  male  | 22.0 |   1   |   0   | 7.250  |    S     | NaN  |
|  1  |    1     |   1    | female | 38.0 |   1   |   0   | 71.283 |    C     |  C   |
|  2  |    1     |   3    | female | 26.0 |   0   |   0   | 7.925  |    S     | NaN  |
|  3  |    1     |   1    | female | 35.0 |   1   |   0   | 53.100 |    S     |  C   |
|  4  |    0     |   3    |  male  | 35.0 |   0   |   0   | 8.050  |    S     | NaN  |
| ... |   ...    |  ...   |  ...   | ...  |  ...  |  ...  |  ...   |   ...    | ...  |
| 886 |    0     |   2    |  male  | 27.0 |   0   |   0   | 13.000 |    S     | NaN  |
| 887 |    1     |   1    | female | 19.0 |   0   |   0   | 30.000 |    S     |  B   |
| 888 |    0     |   3    | female | NaN  |   1   |   2   | 23.450 |    S     | NaN  |
| 889 |    1     |   1    |  male  | 26.0 |   0   |   0   | 30.000 |    C     |  C   |
| 890 |    0     |   3    |  male  | 32.0 |   0   |   0   | 7.750  |    Q     | NaN  |

---

---

<br>

```python
titanic_data_csv.shape
```

Output of the above code is

```
(891, 9)
```

---

---

<br>

```python
titanic_data_csv.size
```

Output of the above code is

```
8019
```

---

---

<br>

```python
titanic_data_csv.index
```

Output of the above code is

```
RangeIndex(start=0, stop=891, step=1)
```

---

---

<br>

```python
titanic_data_csv.mean()
```

Output of the above code is

```
survived         0
pclass           1
sex         female
age           0.42
sibsp            0
parch            0
fare             0
dtype: object
```

---

---

<br>

```python
titanic_data_csv.index
```

Output of the above code is

```
survived     0.383838
pclass       2.308642
age         29.699118
sibsp        0.523008
parch        0.381594
fare        32.204208
dtype: float64
```

---

---

<br>

```python
titanic_data_csv.mean().sort_values()
```

Output of the above code is

```
parch        0.381594
survived     0.383838
sibsp        0.523008
pclass       2.308642
age         29.699118
fare        32.204208
dtype: float64
```

---

---

<br>

```python
titanic_data_csv.mean().sort_values().head(3)
```

Output of the above code is

```
parch       0.381594
survived    0.383838
sibsp       0.523008
dtype: float64
```

---

---

---

## tutorial_3_7_Exercise_01

### [First Exercise in Pandas](tutorial_PART_3_7_Exercise_01.ipynb "Clike here to see file")

---

---

---

## tutorial_3_9

### [Selecting Columns in Pandas](tutorial_PART_3_9.ipynb "Clike here to see full tutorial file")

<br>

```python
titanic_data_csv['age']
```

Output of the above code is

```
0      22.0
1      38.0
2      26.0
3      35.0
4      35.0
       ...
886    27.0
887    19.0
888     NaN
889    26.0
890    32.0
Name: age, Length: 891, dtype: float64
```

---

---

<br>

```python
titanic_data_csv[['fare','sex','embarked']]
```

Output of the above code is

|     |  fare   |  sex   | embarked |
| :-: | :-----: | :----: | :------: |
|  0  | 7.2500  |  male  |    S     |
|  1  | 71.2833 | female |    C     |
|  2  | 7.9250  | female |    S     |
|  3  | 53.1000 | female |    S     |
|  4  | 8.0500  |  male  |    S     |
| ... |   ...   |  ...   |   ...    |
| 886 | 13.0000 |  male  |    S     |
| 887 | 30.0000 | female |    S     |
| 888 | 23.4500 | female |    S     |
| 889 | 30.0000 |  male  |    C     |
| 890 | 7.7500  |  male  |    Q     |

---

---

---
