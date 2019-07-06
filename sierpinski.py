#sierpinski
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

def triangle(screen,x,y,size):
    h = size*sin(radians(60))
    points = [(x,y),(x+size/2,y-h),(x+size,y)]
    draw.polygon(screen,GREEN,points,1)

def sierp(screen,x,y,size):
    triangle(screen,x,y,size)
    if size > 8:
        h = 0.5*size*sin(radians(60)) #new height
        sierp(screen,x+size/4,y-h,size/2)#top
        sierp(screen,x,y,size/2)#left
        sierp(screen,x+size/2,y,size/2)#right
        
    


sierp(screen,60,580,600)
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False

    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    

    omx,omy = mx,my
    display.flip() 

quit()

