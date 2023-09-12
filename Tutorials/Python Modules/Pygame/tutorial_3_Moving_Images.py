'''
Date 12-10-2021

In this PyGame tutorial, you will learn about Moving Images in PyGame
'''

import pygame as pg
pg.init()

size = width, height = 1856, 1044
title = "Moving Images in PyGame"
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
how_much_to_move = 100
while not crashed:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            crashed = True

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                car_x -= how_much_to_move
            if event.key == pg.K_RIGHT:
                car_x += how_much_to_move
            if event.key == pg.K_UP:
                car_y -= how_much_to_move
            if event.key == pg.K_DOWN:
                car_y += how_much_to_move
    # car_x -= 5
    # car_y += 5

    screen.fill(white)
    display_image(image_car, car_x, car_y)

    # print(event.type)

    pg.display.update()
    clock.tick(200)

pg.quit()
