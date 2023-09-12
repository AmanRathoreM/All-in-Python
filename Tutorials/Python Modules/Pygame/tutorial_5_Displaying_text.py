'''
Date 12-10-2021

In this PyGame tutorial, you will learn about adding text to PyGame window
'''

import pygame as pg
from time import sleep as sl

pg.init()


size = width, height = 1856, 1044
title = "Adding text to PyGame window"
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 255, 0)
blue = (0, 0, 255)
font_color = (11, 224, 160)
image_car = pg.image.load("image-car.bmp")
image_car.set_colorkey(white)
image_car = pg.transform.scale(image_car, (200, 400))
image_road = pg.image.load("image-road.bmp")
image_road = pg.transform.scale(image_road, (800, 2006))
# road_x, road_y = width/2, height/2
image_road_width = image_road.get_width()    # * 460
image_road_height = image_road.get_height()  # * 2006
road_x = (width/2)-(image_road_width/2)
road_y = -486.0
car_x = (width/2) - (image_car.get_width()/2)
car_y = height/1.68


def display_image(img, x=(width/2), y=(height/2)):
    screen.blit(img, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text="Game Over!"):
    screen.fill(white)
    pg.display.update()
    largeText = pg.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((width/2), (height/2))
    screen.blit(TextSurf, TextRect)
    pg.display.update()
    sl(2)


screen = pg.display.set_mode(size)
pg.display.set_caption(title)
clock = pg.time.Clock()
crashed = False

how_much_to_move = image_road.get_width()/3


while not crashed:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            # print(road_x, road_y)
            # print(car_x, car_y)
            # * 561.3333333333333 522.0
            # * 828.0 522.0
            # * 1094.6666666666667 522.0
            crashed = True

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                car_x -= how_much_to_move
            if event.key == pg.K_RIGHT:
                car_x += how_much_to_move
            if event.key == pg.K_UP:
                message_display()

    if car_x < 560:
        car_x += image_road.get_width()/3
    elif car_x > 1095:
        car_x -= image_road.get_width()/3

    if road_y > (-591):
        road_y -= 1
    else:
        road_y = (-486)

    screen.fill(white)
    display_image(image_road, road_x, road_y)
    display_image(image_car, car_x, car_y)

    # print(event.type)

    pg.display.update()
    clock.tick(100)


pg.quit()
