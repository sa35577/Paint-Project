#graphicsTemplate
from pygame import *
size=width,height=800,600
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
screen.fill(WHITE)
running=True
omx,omy = 0,0
draw.rect(screen,BLACK,(2,2,796,596),1)        
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False

    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    if mb[0] == 1:
        draw.line(screen,BLACK,(omx,omy),(mx,my))
    if mb[2] == 1:
        rc=screen.get_at((mx,my))#gets the colour of the pixel where the user right-clicked 
        spots = [(mx,my)] #list of points
        while len(spots)>0:
            newSpots =[]
            for fx,fy in spots:
            #inside the canvas   #current point is the same colour as the initial when we right-clicked
                if 0<fx<800 and 0<fy<600 and screen.get_at((fx,fy))==rc:
                    screen.set_at((fx,fy),BLACK)
                    newSpots += [(fx+1,fy),(fx-1,fy),(fx,fy-1),(fx,fy+1)]
                #mark the 4 points for filling (right, left, up and down from the current point)
            spots = newSpots
            if len(spots)>8000:
                break
    
    
    

    omx,omy = mx,my
    display.flip() 

quit()

