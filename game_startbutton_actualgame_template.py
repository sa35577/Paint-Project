#graphicsTemplate
from pygame import *
size=width,height=800,600
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
back = "starting"
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False

    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    if back == "starting":
        x = Rect(350,250,100,100)
        draw.rect(screen,GREEN,x)
        if mb[0] == 1 and x.collidepoint(mx,my):
            back = "game"
    else:
        draw.rect(screen,RED,(350,250,100,100))
            
    
    display.flip() 

quit()
