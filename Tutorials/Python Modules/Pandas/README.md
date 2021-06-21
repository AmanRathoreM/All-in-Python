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
