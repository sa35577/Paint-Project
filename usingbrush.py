#usingbrush.py
from pygame import *
from math import *
size=width,height=800,600
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)

running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
                       
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()

    if mb[0] == 1:
        dx = mx-omx#horizontal distance
        dy = my-omy#vertical distance
        dist = int(sqrt(dx**2+dy**2))
        if omx == mx and omy == my:
            draw.circle(screen,GREEN,(omx,omy),20)
        for i in range(1,dist+1):
            dotX = int(omx+i*dx/dist)
            dotY = int(omy+i*dy/dist)
            draw.circle(screen,GREEN,(dotX,dotY),20)

    omx,omy = mx,my
    display.flip() 

quit()
