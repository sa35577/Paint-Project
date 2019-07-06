#helprect.py
from pygame import *
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
    
    draw.rect(screen,GREEN,(200,150,100,70), 1)
    draw.circle(screen,WHITE,(200,150),4)

    draw.rect(screen,GREEN,(200,350,-100,-70), 1)
    draw.circle(screen,WHITE,(200,350),4)

    draw.rect(screen,GREEN,(500,150,-100,70), 1)
    draw.circle(screen,WHITE,(500,150),4)

    draw.rect(screen,GREEN,(500,350,100,-70), 1)
    draw.circle(screen,WHITE,(500,350),4)
    
    display.flip() 

quit()
