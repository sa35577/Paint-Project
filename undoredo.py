#undoredo.py
from pygame import *
size=width,height=800,600
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)

canvas = Rect(100,100,600,400)
pencil = Rect(50,50,25,25)
undo = Rect(50,150,25,25)
redo = Rect(50,250,25,25)

screenshots = []

tool = ""
mmode = "up"
mmode2 = "up"
mmode3 = "up"
undostatus,count = "off",-2
redostatus = "off"
firstredo = False

draw.rect(screen,WHITE,canvas)
draw.rect(screen,RED,pencil)
draw.rect(screen,GREEN,undo)
draw.rect(screen,RED,redo)

running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
    
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    

   
    if mb[0] == 1 and pencil.collidepoint(mx,my):
        tool = "pencil"
    elif mb[0] == 1 and undo.collidepoint(mx,my):
        tool = "undo"
    elif mb[0] == 1 and redo.collidepoint(mx,my):
        tool = "redo"

    if tool == "undo":
        undostatus = "on"
    elif tool == "redo":
        redostatus = "on"
        
    else:
        undostatus = "off"
        redostatus = "off"
        firstredo = True
        count = -2
        if mmode2 == "up" and mb[0] == 1:
            mmode2 = "down"
        if mmode2 == "down" and mb[0] == 0:
            mmode2 = "up"
            screenshots.append(screen.copy())

    if canvas.collidepoint(mx,my):
        screen.set_clip(canvas)
        if tool == "pencil" and mb[0] == 1:
            draw.line(screen,BLACK,(omx,omy),(mx,my))
        elif tool == "undo":
            if mmode == "up" and mb[0] == 1:
                mmode = "down"
            if mmode == "down" and mb[0] == 0:
                mmode = "up"
                draw.rect(screen,WHITE,canvas)
                try: 
                    screen.blit(screenshots[count],(0,0))
                except IndexError:
                    pass
                count -= 1
        elif tool == "redo":
            if mmode3 == "up" and mb[0] == 1:
                mmode3 = "down"
            if mmode3 == "down" and mb[0] == 0:
                mmode3 = "up"
                if firstredo:
                    count += 1
                    firstredo = False  
                if count < -1:
                    count += 1
                elif count > -1:
                    count = -1
                draw.rect(screen,WHITE,canvas)
                screen.blit(screenshots[count],(0,0))
                
                
        screen.set_clip(None)
    omx,omy = mx,my
    
    display.flip() 

quit()
