# Pandas

## These tutorials are watched from [**_Udemy_**](https://www.udemy.com/ "Clike here to checkout Udemy Website") website from [**_Pandas tutorial by Alexander Hagmann_**](https://www.udemy.com/share/101WOgAEcdc1lXQH4B/ "Clike here to check out his Course")

---

---

---

---

---

## tutorial_3_1

### [Creating Data Frame](tutorial_3_1.ipynb "Clike here to see full tutorial file")

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

### [Creating Data Frame](tutorial_3_2.ipynb "Clike here to see full tutorial file")

```python
pd.options.display.max_rows
```

```console
60
```

---

---

```python
pd.options.display.min_rows
```

```console
20
```

---

---

```python
pd.options.display.min_rows = 40
```

---

---

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

```python
titanic_data_csv.head(3)
```

Output of the above code is
| | survived | pclass | sex | age | sibsp | parch | fare | embarked | deck |
|---------:|-------:|----:|----:|------:|------:|-----:|---------:|-----:|--:|
| 0 | 0 | 3 | male | 22.0 | 1 | 0 | 7.2500 | S | NaN |
| 1 | 1 | 1 | female | 38.0 | 1 | 0 | 71.2833 | C | C |
| 2 | 1 | 3 | female | 26.0 | 0 | 0 | 7.9250 | S | NaN |
