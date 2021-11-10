# import numpy as np
import time
import random as rd

header = "Serial No.,Time,Random1,Random2,Random3,Random4\n"

i = 1


with open('check1.csv', 'a', encoding='UTF8') as file:

    # file.write(header)

    while i <= 20:

        Serial_Num = i
        Time = time.strftime("%H:%M:%S")
        Random1 = rd.randint(4, 7845)
        Random2 = rd.randint(-145545, -15)
        Random3 = rd.randint(1, 10)
        Random4 = rd.randint(215445, 4454545)

        # data = [i, time.strftime("%H:%M:%S"), rd.randint(4, 7845),
        #         rd.randint(-145545, -15), rd.randint(1, 10), rd.randint(215445, 4454545)]

        data = f"{Serial_Num},{Time},{Random1},{Random2},{Random3}4{Random4}\n"

        file.write(data)
        # write the data

        i += 1
