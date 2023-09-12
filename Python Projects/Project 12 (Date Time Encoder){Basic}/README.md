# DateTime Encode-Decoder

This programme can be used to encode or decode the date. As it you are doing work on a note-book and you want to write time as well as date on your work and you does not want to write much in your copy then you can use it as it only needs **7 letters** to encode time and that also in a readable manner. 
Suppose if you want to write DateTime you would do something like this **13-12-2021 15:54:23** which will take **19** letter to display but rather than writing 19 letters you can write it as _**1LDF54H**_, perhaps it may be a bit confusing but you can use it if you want as all the things are done programmatically.

Following, I had explained what represents what.

### Encoder encodes Year as follows:
| Real Year |    By Doing    | Encoded Year |
|:---------:|:--------------:|:------------:|
|    2021   | hex(2021-2020) |       1      |
|    2022   | hex(2022-2020) |       2      |
|    2023   | hex(2023-2020) |       3      |
|    2024   | hex(2024-2020) |       4      |
|    2025   | hex(2025-2020) |       5      |
|    2026   | hex(2026-2020) |       6      |
|    2027   | hex(2027-2020) |       7      |
|    2028   | hex(2028-2020) |       8      |
|    2029   | hex(2029-2020) |       9      |
|    2030   | hex(2030-2020) |       A      |
|    2031   | hex(2031-2020) |       B      |
|    2032   | hex(2032-2020) |       C      |
|    2033   | hex(2033-2020) |       D      |
|    2034   | hex(2034-2020) |       E      |
|    2035   | hex(2035-2020) |       F      |
|    2036   | hex(2036-2020) |      10      |
|    2037   | hex(2037-2020) |      11      |
|    2038   | hex(2038-2020) |      12      |
|    2039   | hex(2039-2020) |      13      |
|    2040   | hex(2040-2020) |      14      |


### Encoder encodes Month as follows:
| Real Month | Encoded Month |
|:----------:|:-------------:|
|     01     |       A       |
|     02     |       B       |
|     03     |       C       |
|     04     |       D       |
|     05     |       E       |
|     06     |       F       |
|     07     |       G       |
|     08     |       H       |
|     09     |       I       |
|     10     |       J       |
|     11     |       K       |
|     12     |       L       |

### Encoder encodes Day as follows:
| Real Day | Encoded Day |
|:--------:|:-----------:|
|    01    |      1      |
|    02    |      2      |
|    03    |      3      |
|    04    |      4      |
|    05    |      5      |
|    06    |      6      |
|    07    |      7      |
|    08    |      8      |
|    09    |      9      |
|    10    |      A      |
|    11    |      B      |
|    12    |      C      |
|    13    |      D      |
|    14    |      E      |
|    15    |      F      |
|    16    |      G      |
|    17    |      H      |
|    18    |      I      |
|    19    |      J      |
|    20    |      K      |
|    21    |      L      |
|    22    |      M      |
|    23    |      N      |
|    24    |      O      |
|    25    |      P      |
|    26    |      Q      |
|    27    |      R      |
|    28    |      S      |
|    29    |      T      |
|    30    |      U      |
|    31    |      V      |

### Encoder encodes Hour as follows:
| Real Hour | Encoded Hour |
|:---------:|:------------:|
|     00    |       0      |
|     01    |       1      |
|     02    |       2      |
|     03    |       3      |
|     04    |       4      |
|     05    |       5      |
|     06    |       6      |
|     07    |       7      |
|     08    |       8      |
|     09    |       9      |
|     10    |       A      |
|     11    |       B      |
|     12    |       C      |
|     13    |       D      |
|     14    |       E      |
|     15    |       F      |
|     16    |       G      |
|     17    |       H      |
|     18    |       I      |
|     19    |       J      |
|     20    |       K      |
|     21    |       L      |
|     22    |       M      |
|     23    |       N      |

### Encoder encodes Minutes as follows:
| Real Minute | Encoded Minute |
|:-----------:|:--------------:|
|      00     |       00       |
|      01     |       01       |
|      02     |       02       |
|      03     |       03       |
|      04     |       04       |
|      05     |       05       |
|      06     |       06       |
|      07     |       07       |
|      08     |       08       |
|      09     |       09       |
|      10     |       10       |
|     ...     |       ...      |
|     ...     |       ...      |
|     ...     |       ...      |
|      51     |       51       |
|      52     |       52       |
|      53     |       53       |
|      54     |       54       |
|      55     |       55       |
|      56     |       56       |
|      57     |       57       |
|      58     |       58       |
|      59     |       59       |
> ### Note: Encoder does not encodes minute

### Encoder encodes Seconds as follows:
| Real Second | Encoded Second |
|:-----------:|:--------------:|
|      00     |        A       |
|      01     |        A       |
|      02     |        A       |
|      03     |        A       |
|      04     |        B       |
|      05     |        B       |
|      06     |        B       |
|      07     |        C       |
|      08     |        C       |
|      09     |        C       |
|      10     |        D       |
|      11     |        D       |
|      12     |        D       |
|      13     |        E       |
|      14     |        E       |
|      15     |        E       |
|      16     |        F       |
|      17     |        F       |
|      18     |        F       |
|      19     |        G       |
|      20     |        G       |
|      21     |        G       |
|      22     |        H       |
|      23     |        H       |
|      24     |        H       |
|      25     |        I       |
|      26     |        I       |
|      27     |        I       |
|      28     |        J       |
|      29     |        J       |
|      30     |        J       |
|      31     |        K       |
|      32     |        K       |
|      33     |        K       |
|      34     |        L       |
|      35     |        L       |
|      36     |        L       |
|      37     |        M       |
|      38     |        M       |
|      39     |        M       |
|      40     |        N       |
|      41     |        N       |
|      42     |        N       |
|      43     |        O       |
|      44     |        O       |
|      45     |        O       |
|      46     |        P       |
|      47     |        P       |
|      48     |        P       |
|      49     |        Q       |
|      50     |        Q       |
|      51     |        Q       |
|      52     |        R       |
|      53     |        R       |
|      54     |        R       |
|      55     |        S       |
|      56     |        S       |
|      57     |        S       |
|      58     |        T       |
|      59     |        T       |