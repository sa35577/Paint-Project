from pygame import *
size=width,height=800,600
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)

radius = 12
col = RED
sx,sy = 0,0
th = 1 #thickness of the line

running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type == MOUSEBUTTONDOWN:
            sx,sy = mouse.get_pos() #starting position
            screenshot = screen.copy() #taking a screenshot
            if evt.button==4: #scrolling up
                th += 1
            if evt.button == 5 and th>1:#scrolling down
                th -= 1
                

            
    mb=mouse.get_pressed()
    mx,my = mouse.get_pos()
    if mb[0] == 1:
        screen.blit(screenshot, (0,0))
        draw.line(screen,GREEN,(sx,sy),(mx,my), th)
    
    display.flip()
quit()
