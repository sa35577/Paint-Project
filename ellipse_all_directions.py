from pygame import *
from math import *
size=width,height=800,600
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
mmode = "up"
r = 10
running = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONDOWN:
            sx,sy = mouse.get_pos()
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()


    if mmode == "up" and mb[0] == 1:
        screenshot = screen.copy()
        mmode = "down"
    if mmode == "down" and mb[0] == 0:
        mmode = "up"
    if mb[0] == 1:
        screen.blit(screenshot,(0,0))
        a = min(mx,sx)
        b = max(mx,sx)
        c = min(my,sy)
        d = max(my,sy)
        draw.ellipse(screen,RED,(a,c,b-a,d-c))
    if mb[2] == 1:
        screen.fill(BLACK)


    display.flip()
    
quit()
