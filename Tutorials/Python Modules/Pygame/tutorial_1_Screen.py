'''
Date 12-10-2021

In this PyGame tutorial, you will learn a bit about PyGame's Screen
'''

import pygame as pg
pg.init()

size = width, height = 1856, 1044
title = "Screen"
screen = pg.display.set_mode(size)
pg.display.set_caption(title)
clock = pg.time.Clock()
crashed = False

while not crashed:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            crashed = True

        print(event.type)

    pg.display.update()
    clock.tick(60)

pg.quit()
