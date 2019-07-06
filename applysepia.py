#graphicsTemplate
from pygame import *
size=width,height=800,600
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
running=True
masseyPic = image.load("Images/massey.jpg")
screen.blit(masseyPic,(0,0))
t = 0
for x in range(800):
    for y in range(600):
        t += 1
        r,g,b,a = screen.get_at((x,y))
        r2 = min(255,int(0.393*r+0.769*g+0.189*b))
        g2 = min(255,int(0.349*r + 0.686*g + 0.168*b))
        b2 = min(255,int(0.272*r + 0.534*g + 0.131*b))
        screen.set_at((x,y),(r2,g2,b2))
        if t == 100:
            display.flip()
            t = 0
        
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False

    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    
            
    
    display.flip() 

quit()
