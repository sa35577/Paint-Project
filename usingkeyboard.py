#usingkeyboard.py
from pygame import *
size=width,height=800,600
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)

radius = 12
col = RED


running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type == KEYDOWN:
            if evt.key == K_LEFT and radius > 0:
                radius -= 1
            if evt.key == K_RIGHT and radius < 30:
                radius += 1
            if evt.key == K_UP and radius < 26:
                radius += 5
            if evt.key == K_DOWN and radius > 4:
                radius -= 5
            if evt.key == K_g:
                col = GREEN
            if evt.key == K_r:
                col = RED
            if evt.key == K_b:
                col = BLUE

    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()

    if mb[0] == 1:
        draw.circle(screen,col,(mx,my), radius)
    print(radius)
                       
    

    display.flip()
quit()
