# Date 02-07-2021
# Direct Drawing on Images with a mouse - Part Three


import numpy as np
import cv2

blank_img = np.zeros((900, 1600, 3),  np.uint8)


drawing = False
ix, iy = -1, -1


def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(blank_img, (ix, iy), (x, y), (200, 132, 245), -1)

    elif event == cv2.EVENT_LBUTTONUP:

        drawing = False

        cv2.rectangle(blank_img, (ix, iy), (x, y), (200, 132, 245), -1)


cv2.namedWindow(winname='my_drawing')

cv2.setMouseCallback('my_drawing', draw_rectangle)

while True:
    cv2.imshow('my_drawing', blank_img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
