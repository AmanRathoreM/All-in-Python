# Date 02-07-2021
# Direct Drawing on Images with a mouse - Part Two


import numpy as np
import matplotlib.pyplot as plt
import cv2

blank_img = np.zeros((900, 1600, 3),  np.uint8)


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(blank_img, (x, y), 100, (110, 155, 148))

    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(blank_img, (x, y), 50, (200, 132, 245), -1)


cv2.namedWindow(winname='my_drawing (Press Esc i.e. Escape to Exit)')

cv2.setMouseCallback('my_drawing (Press Esc i.e. Escape to Exit)', draw_circle)

while True:

    cv2.imshow('my_drawing (Press Esc i.e. Escape to Exit)', blank_img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
