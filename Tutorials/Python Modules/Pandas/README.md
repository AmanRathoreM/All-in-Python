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
titanic_data_csv.min()
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

## tutorial_3_10

### [Selecting Columns in Pandas](tutorial_PART_3_10.ipynb "Clike here to see full tutorial file")

<br>

```python
titanic_data_csv.fare.equals(titanic_data_csv['fare'])
```

Output of the above code is

```
True
```

---

---

<br>

```python
titanic_data_csv.sex
```

Output of the above code is

```
0        male
1      female
2      female
3      female
4        male
        ...
886      male
887    female
888    female
889      male
890      male
Name: sex, Length: 891, dtype: object
```

---

---

---

## tutorial_3_12

### [Indexing using iloc in Pandas](tutorial_PART_3_12.ipynb "Clike here to see full tutorial file")

<br>

```python
summer_olmypic_data_csv.iloc[1]
```

Output of the above code is

```
Year                    1896
City                  Athens
Sport               Aquatics
Discipline          Swimming
Country                  AUT
Gender                   Men
Event         100M Freestyle
Medal                 Silver
Name: HERSCHMANN, Otto, dtype: object
```

---

---

<br>

```python
summer_olmypic_data_csv.iloc[[3,5,9,13]]
```

Output of the above code is
| Athlete | Year | City | Sport | Discipline | Country | Gender | Event | Medal |
|:---------------------:|:----:|:------:|:---------:|:----------:|:-------:|:------:|:--------------------------:|:------:|
| MALOKINIS, Ioannis | 1896 | Athens | Aquatics | Swimming | GRE | Men | 100M Freestyle For Sailors | Gold |
| CHOROPHAS, Efstathios | 1896 | Athens | Aquatics | Swimming | GRE | Men | 1200M Freestyle | Bronze |
| NEUMANN, Paul | 1896 | Athens | Aquatics | Swimming | AUT | Men | 400M Freestyle | Gold |
| BURKE, Thomas | 1896 | Athens | Athletics | Athletics | USA | Men | 100M | Gold |

---

---

<br>

```python
summer_olmypic_data_csv.iloc[3:13]
```

Output of the above code is
| Athlete | Year | City | Sport | Discipline | Country | Gender | Event | Medal |
|:---------------------:|:----:|:------:|:---------:|:----------:|:-------:|:------:|:--------------------------:|:------:|
| MALOKINIS, Ioannis | 1896 | Athens | Aquatics | Swimming | GRE | Men | 100M Freestyle For Sailors | Gold |
| CHASAPIS, Spiridon | 1896 | Athens | Aquatics | Swimming | GRE | Men | 100M Freestyle For Sailors | Silver |
| CHOROPHAS, Efstathios | 1896 | Athens | Aquatics | Swimming | GRE | Men | 1200M Freestyle | Bronze |
| HAJOS, Alfred | 1896 | Athens | Aquatics | Swimming | HUN | Men | 1200M Freestyle | Gold |
| ANDREOU, Joannis | 1896 | Athens | Aquatics | Swimming | GRE | Men | 1200M Freestyle | Silver |
| CHOROPHAS, Efstathios | 1896 | Athens | Aquatics | Swimming | GRE | Men | 400M Freestyle | Bronze |
| NEUMANN, Paul | 1896 | Athens | Aquatics | Swimming | AUT | Men | 400M Freestyle | Gold |
| PEPANOS, Antonios | 1896 | Athens | Aquatics | Swimming | GRE | Men | 400M Freestyle | Silver |
| LANE, Francis | 1896 | Athens | Athletics | Athletics | USA | Men | 100M | Bronze |
| SZOKOLYI, Alajos | 1896 | Athens | Athletics | Athletics | HUN | Men | 100M | Bronze |

---

---

<br>

```python
summer_olmypic_data_csv.iloc[-1]
```

Output of the above code is

```
Year                         2012
City                       London
Sport                   Wrestling
Discipline    Wrestling Freestyle
Country                       SWE
Gender                        Men
Event                    Wg 96 KG
Medal                      Bronze
Name: LIDBERG, Jimmy, dtype: object
```

---

---

<br>

```python
summer_olmypic_data_csv.iloc[-9:-5]
```

Output of the above code is
| Athlete | Year | City | Sport | Discipline | Country | Gender | Event | Medal |
|:----------------------------:|:----:|:------:|:---------:|:-------------------:|:-------:|:------:|:--------:|:------:|
| KAZAKEVIC, Aleksandr | 2012 | London | Wrestling | Wrestling Freestyle | LTU | Men | Wg 74 KG | Bronze |
| KHUGAEV, Alan | 2012 | London | Wrestling | Wrestling Freestyle | RUS | Men | Wg 84 KG | Gold |
| EBRAHIM, Karam Mohamed Gaber | 2012 | London | Wrestling | Wrestling Freestyle | EGY | Men | Wg 84 KG | Silver |
| GAJIYEV, Danyal | 2012 | London | Wrestling | Wrestling Freestyle | KAZ | Men | Wg 84 KG | Bronze |

---

---

---

## tutorial_3_13

### [Slicing Rows and Columns with iloc in Pandas](tutorial_PART_3_13.ipynb "Clike here to see full tutorial file")

<br>

```python
summer_olmypic_data_csv.iloc[0:10,7]
```

Output of the above code is

```
Athlete
HAJOS, Alfred              Gold
HERSCHMANN, Otto         Silver
DRIVAS, Dimitrios        Bronze
MALOKINIS, Ioannis         Gold
CHASAPIS, Spiridon       Silver
CHOROPHAS, Efstathios    Bronze
HAJOS, Alfred              Gold
ANDREOU, Joannis         Silver
CHOROPHAS, Efstathios    Bronze
NEUMANN, Paul              Gold
Name: Medal, dtype: object
```

---

---

<br>

```python
summer_olmypic_data_csv.iloc[0:10,[2,-3,-1]]
```

Output of the above code is
| Athlete | Sport | Gender | Medal |
|:---------------------:|:--------:|:------:|:------:|
| HAJOS, Alfred | Aquatics | Men | Gold |
| HERSCHMANN, Otto | Aquatics | Men | Silver |
| DRIVAS, Dimitrios | Aquatics | Men | Bronze |
| MALOKINIS, Ioannis | Aquatics | Men | Gold |
| CHASAPIS, Spiridon | Aquatics | Men | Silver |
| CHOROPHAS, Efstathios | Aquatics | Men | Bronze |
| HAJOS, Alfred | Aquatics | Men | Gold |
| ANDREOU, Joannis | Aquatics | Men | Silver |
| CHOROPHAS, Efstathios | Aquatics | Men | Bronze |
| NEUMANN, Paul | Aquatics | Men | Gold |

---

---

---

## tutorial_3_15

### [Label Based Indexing Part 1 in Pandas](tutorial_PART_3_15.ipynb "Clike here to see full tutorial file")

<br>

```python
summer_olmypic_data_csv.loc['CHASAPIS, Spiridon']
```

Output of the above code is

```
Year                                1896
City                              Athens
Sport                           Aquatics
Discipline                      Swimming
Country                              GRE
Gender                               Men
Event         100M Freestyle For Sailors
Medal                             Silver
Name: CHASAPIS, Spiridon, dtype: object
```

---

---

<br>

```python
summer_olmypic_data_csv.loc["LATYNINA, Larisa"]
```

Output of the above code is
| Athlete | Year | City | Sport | Discipline | Country | Gender | Event | Medal |
|:----------------:|:----:|:---------------------:|:----------:|:-----------:|:-------:|:------:|:------------------------:|:------:|
| LATYNINA, Larisa | 1956 | Melbourne / Stockholm | Gymnastics | Artistic G. | URS | Women | Floor Exercises | Gold |
| LATYNINA, Larisa | 1956 | Melbourne / Stockholm | Gymnastics | Artistic G. | URS | Women | Individual All-Round | Gold |
| LATYNINA, Larisa | 1956 | Melbourne / Stockholm | Gymnastics | Artistic G. | URS | Women | Team Competition | Gold |
| LATYNINA, Larisa | 1956 | Melbourne / Stockholm | Gymnastics | Artistic G. | URS | Women | Team, Portable Apparatus | Bronze |
| LATYNINA, Larisa | 1956 | Melbourne / Stockholm | Gymnastics | Artistic G. | URS | Women | Uneven Bars | Silver |
| LATYNINA, Larisa | 1956 | Melbourne / Stockholm | Gymnastics | Artistic G. | URS | Women | Vault | Gold |
| LATYNINA, Larisa | 1960 | Rome | Gymnastics | Artistic G. | URS | Women | Balance Beam | Silver |
| LATYNINA, Larisa | 1960 | Rome | Gymnastics | Artistic G. | URS | Women | Floor Exercises | Gold |
| LATYNINA, Larisa | 1960 | Rome | Gymnastics | Artistic G. | URS | Women | Individual All-Round | Gold |
| LATYNINA, Larisa | 1960 | Rome | Gymnastics | Artistic G. | URS | Women | Team Competition | Gold |
| LATYNINA, Larisa | 1960 | Rome | Gymnastics | Artistic G. | URS | Women | Uneven Bars | Silver |
| LATYNINA, Larisa | 1960 | Rome | Gymnastics | Artistic G. | URS | Women | Vault | Bronze |
| LATYNINA, Larisa | 1964 | Tokyo | Gymnastics | Artistic G. | URS | Women | Balance Beam | Bronze |
| LATYNINA, Larisa | 1964 | Tokyo | Gymnastics | Artistic G. | URS | Women | Floor Exercises | Gold |
| LATYNINA, Larisa | 1964 | Tokyo | Gymnastics | Artistic G. | URS | Women | Individual All-Round | Silver |
| LATYNINA, Larisa | 1964 | Tokyo | Gymnastics | Artistic G. | URS | Women | Team Competition | Gold |
| LATYNINA, Larisa | 1964 | Tokyo | Gymnastics | Artistic G. | URS | Women | Uneven Bars | Bronze |
| LATYNINA, Larisa | 1964 | Tokyo | Gymnastics | Artistic G. | URS | Women | Vault | Silver |

---

---

---

## tutorial_3_16

### [Label Based Indexing Part 2 in Pandas](tutorial_PART_3_16.ipynb "Clike here to see full tutorial file")

<br>

```python
summer_olmypic_data_csv.loc['DRIVAS, Dimitrios':'CHASAPIS, Spiridon']
```

Output of the above code is
| Athlete | Year | City | Sport | Discipline | Country | Gender | Event | Medal |
| :----------------: | :--: | :----: | :------: | :--------: | :-----: | :----: | :------------------------: | :----: |
| DRIVAS, Dimitrios | 1896 | Athens | Aquatics | Swimming | GRE | Men | 100M Freestyle For Sailors | Bronze |
| MALOKINIS, Ioannis | 1896 | Athens | Aquatics | Swimming | GRE | Men | 100M Freestyle For Sailors | Gold |
| CHASAPIS, Spiridon | 1896 | Athens | Aquatics | Swimming | GRE | Men | 100M Freestyle For Sailors | Silver |

---

---

<br>

```python
summer_olmypic_data_csv.loc['DRIVAS, Dimitrios':'CHASAPIS, Spiridon',['Medal','Event','Year']]
```

Output of the above code is
| Athlete | Medal | Event | Year |
|:------------------:|:------:|:--------------------------:|:----:|
| DRIVAS, Dimitrios | Bronze | 100M Freestyle For Sailors | 1896 |
| MALOKINIS, Ioannis | Gold | 100M Freestyle For Sailors | 1896 |
| CHASAPIS, Spiridon | Silver | 100M Freestyle For Sailors | 1896 |

---

---

---

## tutorial_3_18

### [Indexing and Slicing with reindex in Pandas](tutorial_PART_3_18.ipynb "Clike here to see full tutorial file")

<br>

```python
summer_olmypic_data_csv.reindex(index=[4,90,7000,30000],columns=['Athlete','Event','Medal'])
```

Output of the above code is
| | Athlete | Event | Medal |
|------:|-------------------------:|---------------------------:|-------:|
| 4 | CHASAPIS, Spiridon | 100M Freestyle For Sailors | Silver |
| 90 | NEUKIRCH, Karl | Team, Horizontal Bar | Gold |
| 7000 | WARNHOLTZ, Rudolf (Tito) | Hockey | Silver |
| 30000 | PAUTARAN, Maryna | K-4 500M | Bronze |

---

---

<br>

```python
summer_olmypic_data_csv.reindex(index=[4,90,7000,30000,999999,1000000],columns=['Athlete','Event','Medal','Age'])
```

Output of the above code is
| | Athlete | Event | Medal | Age |
|:-------:|:------------------------:|:--------------------------:|:------:|:---:|
| 4 | CHASAPIS, Spiridon | 100M Freestyle For Sailors | Silver | NaN |
| 90 | NEUKIRCH, Karl | Team, Horizontal Bar | Gold | NaN |
| 7000 | WARNHOLTZ, Rudolf (Tito) | Hockey | Silver | NaN |
| 30000 | PAUTARAN, Maryna | K-4 500M | Bronze | NaN |
| 999999 | NaN | NaN | NaN | NaN |
| 1000000 | NaN | NaN | NaN | NaN |

---

---

---

## tutorial_3_21_Exercise_02

### [Second Exercise in Pandas](tutorial_PART_3_21_Exercise_02.ipynb "Clike here to see file")

---

---

---

## tutorial_4_2

### [Series in Pandas](tutorial_PART_4_2.ipynb "Clike here to see full tutorial file")

<br>

```python
age.to_frame()
```

Output of the above code is
| | age |
|:---:|:----:|
| 0 | 22.0 |
| 1 | 38.0 |
| 2 | 26.0 |
| 3 | 35.0 |
| 4 | 35.0 |
| ... | ... |
| 886 | 27.0 |
| 887 | 19.0 |
| 888 | NaN |
| 889 | 26.0 |
| 890 | 32.0 |

---

---

<br>

```python
age.to_frame().info()
```

Output of the above code is

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 1 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   age     714 non-null    float64
dtypes: float64(1)
memory usage: 7.1 KB
```

---

---

---

## tutorial_4_3

### [Analyzing Numerical Series with unique, nunique and value_counts functions in Pandas Part 1](tutorial_PART_4_3.ipynb "Clike here to see full tutorial file")

<br>

```python
age.unique()
```

Output of the above code is

```
array([22.  , 38.  , 26.  , 35.  ,   nan, 54.  ,  2.  , 27.  , 14.  ,
        4.  , 58.  , 20.  , 39.  , 55.  , 31.  , 34.  , 15.  , 28.  ,
        8.  , 19.  , 40.  , 66.  , 42.  , 21.  , 18.  ,  3.  ,  7.  ,
       49.  , 29.  , 65.  , 28.5 ,  5.  , 11.  , 45.  , 17.  , 32.  ,
       16.  , 25.  ,  0.83, 30.  , 33.  , 23.  , 24.  , 46.  , 59.  ,
       71.  , 37.  , 47.  , 14.5 , 70.5 , 32.5 , 12.  ,  9.  , 36.5 ,
       51.  , 55.5 , 40.5 , 44.  ,  1.  , 61.  , 56.  , 50.  , 36.  ,
       45.5 , 20.5 , 62.  , 41.  , 52.  , 63.  , 23.5 ,  0.92, 43.  ,
       60.  , 10.  , 64.  , 13.  , 48.  ,  0.75, 53.  , 57.  , 80.  ,
       70.  , 24.5 ,  6.  ,  0.67, 30.5 ,  0.42, 34.5 , 74.  ])
```

---

---

<br>

```python
age.nunique(dropna=False)
```

Output of the above code is

```
89
```

---

---

<br>

```python
age.value_counts()
```

Output of the above code is

```
24.00    30
22.00    27
18.00    26
19.00    25
30.00    25
         ..
55.50     1
70.50     1
66.00     1
23.50     1
0.42      1
Name: age, Length: 88, dtype: int64
```

---

---

<br>

```python
age.value_counts(ascending=True)
```

Output of the above code is

```
0.42      1
23.50     1
66.00     1
70.50     1
55.50     1
         ..
30.00    25
19.00    25
18.00    26
22.00    27
24.00    30
Name: age, Length: 88, dtype: int64
```

---

---

<br>

```python
age.value_counts(normalize=True)
```

Output of the above code is

```
24.00    0.042017
22.00    0.037815
18.00    0.036415
19.00    0.035014
30.00    0.035014
           ...
55.50    0.001401
70.50    0.001401
66.00    0.001401
23.50    0.001401
0.42     0.001401
Name: age, Length: 88, dtype: float64
```

---

---

<br>

```python
age.value_counts(normalize=True,dropna=False).sum()
```

Output of the above code is

```
0.9999999999999999
```

---

---

<br>

```python
age.value_counts(normalize=True,dropna=False)
```

Output of the above code is

```
NaN      0.198653
24.00    0.033670
22.00    0.030303
18.00    0.029181
28.00    0.028058
           ...
36.50    0.001122
55.50    0.001122
66.00    0.001122
23.50    0.001122
0.42     0.001122
Name: age, Length: 89, dtype: float64
```

---

---

<br>

```python
age.value_counts(normalize=True,dropna=False)*100
```

Output of the above code is

```
NaN      19.865320
24.00     3.367003
22.00     3.030303
18.00     2.918070
28.00     2.805836
           ...
36.50     0.112233
55.50     0.112233
66.00     0.112233
23.50     0.112233
0.42      0.112233
Name: age, Length: 89, dtype: float64
```

---

---

<br>

```python
arr1=age.value_counts(normalize=True,dropna=False)*100
arr1.sum()
```

Output of the above code is

```
100
```

---

---

<br>

```python
age.value_counts(dropna=True,bins=5)
```

Output of the above code is

```
(16.336, 32.252]    346
(32.252, 48.168]    188
(0.339, 16.336]     100
(48.168, 64.084]     69
(64.084, 80.0]       11
Name: age, dtype: int64
```

---

---

<br>

```python
age.value_counts(normalize=True,bins=5)
```

Output of the above code is

```
(16.336, 32.252]    0.388328
(32.252, 48.168]    0.210999
(0.339, 16.336]     0.112233
(48.168, 64.084]    0.077441
(64.084, 80.0]      0.012346
Name: age, dtype: float64
```

---

---

<br>

```python
age.value_counts(normalize=True,bins=5)*100
```

Output of the above code is

```
(16.336, 32.252]    38.832772
(32.252, 48.168]    21.099888
(0.339, 16.336]     11.223345
(48.168, 64.084]     7.744108
(64.084, 80.0]       1.234568
Name: age, dtype: float64
```

---

---

---

## tutorial_4_4

### [Analyzing Numerical Series with unique, nunique and value_counts functions in Pandas Part 2](tutorial_PART_4_4.ipynb "Clike here to see full tutorial file")

<br>

There is nothing much in this tutorial

---

---

---

## tutorial_4_5

### [Creating Pandas Series Part 1](tutorial_PART_4_5.ipynb "Clike here to see full tutorial file")

<br>

```python
pd.Series([45,7,6,4,7,9,78],index=['SUN','MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'],name='Sales')
```

Output of the above code is

```
SUN    45
MON     7
TUE     6
WED     4
THU     7
FRI     9
SAT    78
Name: Sales, dtype: int64
```

---

---

---

## tutorial_4_6

### [Creating Pandas Series Part 2](tutorial_PART_4_6.ipynb "Clike here to see full tutorial file")

<br>

```python
sales=list(sales)
sales
```

Output of the above code is

```
[448, 348, 869, 481, 712, 225, 475, 415, 217, 947]
```

---

---

<br>

```python
sales={'SUN':sales[0],'Mon':sales[1],'TUE':sales[2],'WED':sales[3],'THU':sales[4],'FRI':sales[5],'SAT':sales[6]}
sales
```

Output of the above code is

```
{'SUN': 448,
 'Mon': 348,
 'TUE': 869,
 'WED': 481,
 'THU': 712,
 'FRI': 225,
 'SAT': 475}
```

---

---

<br>

```python
pd.Series(sales)
```

Output of the above code is

```
SUN    448
Mon    348
TUE    869
WED    481
THU    712
FRI    225
SAT    475
dtype: int64
```

---

---

---

## tutorial_4_7

### [Indexing and Slicing Pandas Series](tutorial_PART_4_7.ipynb "Clike here to see full tutorial file")

<br>

```python
age.iloc[:-860]
```

Output of the above code is

```
0     22.0
1     38.0
2     26.0
3     35.0
4     35.0
5      NaN
6     54.0
7      2.0
8     27.0
9     14.0
10     4.0
11    58.0
12    20.0
13    39.0
14    14.0
15    55.0
16     2.0
17     NaN
18    31.0
19     NaN
20    35.0
21    34.0
22    15.0
23    28.0
24     8.0
25    38.0
26     NaN
27    19.0
28     NaN
29     NaN
30    40.0
Name: age, dtype: float64
```

---

---

---

## tutorial_4_8

### [Sorting of Pandas Series and inplace Parameter](tutorial_PART_4_8.ipynb "Clike here to see full tutorial file")

<br>

```python
age.sort_values(ascending= False,na_position= 'first',inplace=True)
age
```

Output of the above code is

```
5       NaN
17      NaN
19      NaN
26      NaN
28      NaN
       ...
78     0.83
469    0.75
644    0.75
755    0.67
803    0.42
Name: age, Length: 891, dtype: float64
```

---

---

---

## tutorial_4_9

### [nlargest and nsmallest methods in Pandas](tutorial_PART_4_9.ipynb "Clike here to see full tutorial file")

<br>

```python
age.nlargest(n=9)
```

Output of the above code is

```
630    80.0
851    74.0
96     71.0
493    71.0
116    70.5
672    70.0
745    70.0
33     66.0
54     65.0
Name: age, dtype: float64
```

---

---

<br>

```python
age.nsmallest(n=30)
```

Output of the above code is

```
803    0.42
755    0.67
469    0.75
644    0.75
78     0.83
831    0.83
305    0.92
164    1.00
172    1.00
183    1.00
381    1.00
386    1.00
788    1.00
827    1.00
7      2.00
16     2.00
119    2.00
205    2.00
297    2.00
340    2.00
479    2.00
530    2.00
642    2.00
824    2.00
43     3.00
193    3.00
261    3.00
348    3.00
374    3.00
407    3.00
Name: age, dtype: float64
```

---

---

---

## tutorial_4_10

### [idxmin and idsmax in Pandas](tutorial_PART_4_10.ipynb "Clike here to see full tutorial file")

<br>

```python
age.idxmin()
```

Output of the above code is

```
803
```

---

---

<br>

```python
age.idxmax()
```

Output of the above code is

```
630
```

---

---

---

## tutorial_4_11

### [Manipulating Pandas Series](tutorial_PART_4_11.ipynb "Clike here to see full tutorial file")

<br>

```python
age[:]=12
age
```

Output of the above code is

```
<ipython-input-13-7d9ef9a484ad>:1: SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  age[:]=12
C:\ProgramData\Anaconda3\lib\site-packages\pandas\core\indexing.py:670: SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  iloc._setitem_with_indexer(indexer, value)
0      12.0
1      12.0
2      12.0
3      12.0
4      12.0
       ...
886    12.0
887    12.0
888    12.0
889    12.0
890    12.0
Name: age, Length: 891, dtype: float64
```

---

---

<br>

```python
titanic_data_csv
```

Output of the above code is

|     | survived | pclass |  sex   | age  | sibsp | parch |  fare   | embarked | deck |
| :-: | :------: | :----: | :----: | :--: | :---: | :---: | :-----: | :------: | :--: |
|  0  |    0     |   3    |  male  | 12.0 |   1   |   0   | 7.2500  |    S     | NaN  |
|  1  |    1     |   1    | female | 12.0 |   1   |   0   | 71.2833 |    C     |  C   |
|  2  |    1     |   3    | female | 12.0 |   0   |   0   | 7.9250  |    S     | NaN  |
|  3  |    1     |   1    | female | 12.0 |   1   |   0   | 53.1000 |    S     |  C   |
|  4  |    0     |   3    |  male  | 12.0 |   0   |   0   | 8.0500  |    S     | NaN  |
| ... |   ...    |  ...   |  ...   | ...  |  ...  |  ...  |   ...   |   ...    | ...  |
| 886 |    0     |   2    |  male  | 12.0 |   0   |   0   | 13.0000 |    S     | NaN  |
| 887 |    1     |   1    | female | 12.0 |   0   |   0   | 30.0000 |    S     |  B   |
| 888 |    0     |   3    | female | 12.0 |   1   |   2   | 23.4500 |    S     | NaN  |
| 889 |    1     |   1    |  male  | 12.0 |   0   |   0   | 30.0000 |    C     |  C   |
| 890 |    0     |   3    |  male  | 12.0 |   0   |   0   | 7.7500  |    Q     | NaN  |

---

---

---

## tutorial_4_13_Exercise_03

### [Exercise 3](tutorial_PART_4_13_Exercise_03.ipynb "Clike here to see full tutorial file")

---

---

---
