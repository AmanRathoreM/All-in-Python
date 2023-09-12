'''
Date 12-10-2021

In this PyGame tutorial, you will learn about Images in PyGame
'''

import pygame as pg
pg.init()

size = width, height = 1856, 1044
title = "Images in PyGame"
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 255, 0)
blue = (0, 0, 255)
image_car = pg.image.load("image-car.jpg")


def display_image(img, x=(width/2), y=(height/2)):
    screen.blit(img, (x, y))


screen = pg.display.set_mode(size)
pg.display.set_caption(title)
clock = pg.time.Clock()
crashed = False

car_x, car_y = width/2, height/2

while not crashed:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            crashed = True

    screen.fill(white)
    display_image(image_car, car_x, car_y)

    # print(event.type)

    pg.display.update()
    clock.tick(10)

pg.quit()
