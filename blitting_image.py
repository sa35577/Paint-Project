5#graphicsTemplate
from pygame import *
size=width,height=800,600
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
running=True
achilles = image.load("Images/achilles.jpg")
achillesrect = Rect(0,0,71,64)
screen.blit(achilles,(0,0))
print(achillesrect.width)
mmode = "up"
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type == MOUSEBUTTONDOWN:
            screenshot = screen.copy()

    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()

    if achillesrect.collidepoint(mx,my) and mmode == "up" and mb[0] == 1:
        mouse.set_visible(False)
        mmode = "down"
    if mmode == "down":
        screen.blit(screenshot,(0,0))
        screen.blit(achilles,(mx,my))
        if mb[0] == 0:
            mmode = "up"
            mouse.set_visible(True)
    
    display.flip() 

quit()
