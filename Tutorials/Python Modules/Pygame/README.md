# <h1 style="text-align:center; font-size:360%; font-family:verdana;color:#4A3E76;"><em>PyGame</em></h1>

# These tutorials are watched from [**_sentdex_**](https://www.youtube.com/channel/UCfzlCWGWYyIQ0aLC5w48gBQ "Clike here to checkout his channel") YouTube channel from [**_PyGame Playlist_**](https://www.youtube.com/playlist?list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO "Clike here to check out his Pygame tutorials Playlist")

---

---

---

---

---

## **_1.) tutorial_1_Screen of python_**

### [**_Click me_**](tutorial_1_Screen.py "Clike here to see full file") to see full file of tutorial_1_Screen

```py
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

```

---

---

## **_2.) tutorial_2_Images of python_**

### [**_Click me_**](tutorial_2_Images.py "Clike here to see full file") to see full file of tutorial_2_Images

```py
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

```

---

---

## **_3.) tutorial_3_Moving_Images of python_**

### [**_Click me_**](tutorial_3_Moving_Images.py "Clike here to see full file") to see full file of tutorial_3_Moving_Images

```py
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

```

---

---

## **_4.) tutorial_4_Adding_some_more_details of python_**

### [**_Click me_**](tutorial_4_Adding_some_more_details.py "Clike here to see full file") to see full file of tutorial_4_Adding_some_more_details

```py
'''
Date 12-10-2021

In this PyGame tutorial, we will will Add some more details in our previously worked program
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
image_car = pg.image.load("image-car.bmp")
image_car.set_colorkey(white)
image_car = pg.transform.scale(image_car, (200, 400))
image_road = pg.image.load("image-road.bmp")
image_road = pg.transform.scale(image_road, (800, 2006))
# road_x, road_y = width/2, height/2
image_road_width = image_road.get_width()    # * 460
image_road_height = image_road.get_height()  # * 2006
road_x = (width/2)-(image_road_width/2)
road_y = -486.0  # * -591.0
car_x = (width/2) - (image_car.get_width()/2)
car_y = height/1.68


def display_image(img, x=(width/2), y=(height/2)):
    screen.blit(img, (x, y))


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
            # if event.key == pg.K_UP:
            #     car_y -= how_much_to_move
            # if event.key == pg.K_DOWN:
            #     car_y += how_much_to_move

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
    clock.tick(10000)

pg.quit()

```

---

---

## **_5.) tutorial_5_Displaying_text of python_**

### [**_Click me_**](tutorial_5_Displaying_text.py "Clike here to see full file") to see full file of tutorial_5_Displaying_text

```py
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

```

---

---

## **_6.) tutorial_6_Drawing_objects_on_screen of python_**

### [**_Click me_**](tutorial_6_Drawing_objects_on_screen.py "Clike here to see full file") to see full file of tutorial_6_Drawing_objects_on_screen

```py
'''
Date 13-10-2021

In this PyGame tutorial, you will learn about Drawing objects on PyGame Window
'''

import pygame as pg
from time import sleep as sl
from random import randint as rd

pg.init()


size = width, height = 1856, 1044
title = "Drawing objects on PyGame Window"
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 255, 0)
blue = (0, 0, 255)
font_color = (11, 224, 160)
r = rd(0, 255)
g = rd(0, 255)
b = rd(0, 255)


image_car = pg.image.load("image-car.bmp")
image_car.set_colorkey(white)
image_car = pg.transform.scale(image_car, (200, 400))
image_road = pg.image.load("image-road.bmp")
image_road = pg.transform.scale(image_road, (800, 2006))
# road_x, road_y = width/2, height/2
image_road_width = image_road.get_width()    # * 460
image_road_height = image_road.get_height()  # * 2006
road_x = (width/2)-(image_road_width/2)
road_y = -487
car_x = (width/2) - (image_car.get_width()/2)
car_y = height/1.68
image_obstacle_car_x = (width/2) - (image_car.get_width()/2)
image_obstacle_car_y = height/1.68


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


def display_obstacle(x, y, width, height, color):
    pg.draw.rect(screen, color, [x, y, width, height])


screen = pg.display.set_mode(size)
pg.display.set_caption(title)
clock = pg.time.Clock()
crashed = False
speed = 5
how_much_to_move = image_road.get_width()/3
obstacle_x = [561, 828, 1094]
obstacle_y = -200
pos = rd(0, 2)
while not crashed:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            # print(road_x, road_y)
            # print(car_x, car_y)
            # * 561.3333333333333
            # * 828.0 522.0
            # * 1094.6666666666667
            crashed = True

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                car_x -= how_much_to_move
            if event.key == pg.K_RIGHT:
                car_x += how_much_to_move
            # if event.key == pg.K_UP:
            #     message_display()
            if event.key == pg.K_ESCAPE:
                crashed = True

    if car_x < 560:
        car_x += image_road.get_width()/3
    elif car_x > 1095:
        car_x -= image_road.get_width()/3

    if road_y == -382:
        road_y = -487
    else:
        road_y += speed

    screen.fill(white)
    display_image(image_road, road_x, road_y)
    display_image(image_car, car_x, car_y)
    display_obstacle(obstacle_x[pos], obstacle_y, 200, 200, (r, g, b))
    obstacle_y += speed

    if obstacle_y > height+10:
        obstacle_y = -200
        r = rd(0, 255)
        g = rd(0, 255)
        b = rd(0, 255)
        pos = rd(0, 2)

        # print(event.type)

    pg.display.update()
    clock.tick(1000)


pg.quit()

```

---

---
