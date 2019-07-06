#transform.py
from pygame import *
size=width,height=900,600
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)

masseyPic=image.load("Images/massey.jpg")
smallPic=transform.scale(masseyPic,(400,250))
rotPic=transform.rotate(smallPic,45)
                                #hor   ver
flipPic=transform.flip(smallPic,True,True)

screen.blit(masseyPic,(50,50))
##creen.blit(rotPic,(150,250))

myRect = Rect(250,200,180,150)
myArea = screen.subsurface(myRect).copy()
screen.blit(myArea,(20,20))
image.save(myArea,"screen.jpg")

image.save(myArea,"screenhsot.jpg")

running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
                       
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    display.flip() 

quit()
