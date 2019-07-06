#unerasable_background
from pygame import *
size=width,height=800,600
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)

x = transform.scale(image.load("Images/valtvsfree.png"),(400,300))
screen.blit(x,(200,150))
omx,omy = 0,0
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False

    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()

    
    if mb[0] == 1:
        draw.line(screen,GREEN,(omx,omy),(mx,my))
    if mb[2] == 1:
        screen.blit(x.subsurface((mx-200,my-150,30,30)),(mx,my))
    omx,omy = mx,my
    display.flip() 

quit()
