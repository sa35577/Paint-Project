
#imports the pygame,random,and math modules
from pygame import *
from random import *
from math import *
myClock = time.Clock()

#setting screen size, and setting the editing display for the screen
size=width,height=1440,720 #change this
screen=display.set_mode(size)

#very important for paint project
#screenshots, drag and drop
from pygame import *
from random import *
size=width,height=800,600
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
mmode = "up"
vertices = []
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False

    mb = mouse.get_pressed()
    

    
    if mmode=="up" and mb[0] == 1:
        screenshot = screen.copy()
        mmode = "down"
    if mmode == "down" and mb[0] == 0: 
        mmode = "up"
        mx,my = mouse.get_pos()
        draw.circle(screen,GREEN,(mx,my),5)
        if len(vertices) > 0:
            draw.line(screen,WHITE,(vertices[-2],vertices[-1]),(mx,my))
        vertices.append(mx)
        vertices.append(my)
    if mb[2] == 1:
        try:
            draw.line(screen,WHITE,(mx,my),(vertices[0],vertices[1]))
            vertices = []
        except IndexError:
            pass
            
        
        
        
            
        


    
        
        
        
    
        

    display.flip()
quit()

    
    

