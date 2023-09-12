# Date 01-07-2021

import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('00-puppy.jpg')

cv2.imshow("This is an Puppy Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# while True:
#     cv2.imshow("This is an Puppy Image", img)

#     if cv2.waitKey(1000):
#         break
