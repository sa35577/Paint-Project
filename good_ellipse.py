#good_ellipse
from pygame import *
from pygame.gfxdraw import *
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

    for x in range(800):
        for y in range(800):
            if (x,y) in filled_ellipse(screen,400,300,400,300,BLUE):
                print(x,y)

    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()

    
    display.flip() 

quit()
