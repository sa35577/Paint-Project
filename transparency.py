#transparency.py
'''

Color in Python is actually RGBA (The A is for "alpha").
It controls how transparent/opaque the color is
(0-transparent    127-semi transparent   255-opaque)
These values are only used when you blit a surface
onto the screen.
So, if I want to draw a partially transparent circle, I
will draw this circle to a blank surface (sticky note),
then blit the surface to the screen (paper)

'''
from pygame import *
size=width,height=800,600
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)

marker = Surface((20,20),SRCALPHA) #make a blank surface
draw.circle(marker,(255,0,0,30),(10,10),10) #drawing a circle on the small surface
mx,my = 0,0
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False

    omx,omy = mx,my
                       
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    if mx != omx or my != omy: #checking if there is movement
        if mb[0] == 1:
            screen.blit(marker,(mx,my))
    
    display.flip() 

quit()
