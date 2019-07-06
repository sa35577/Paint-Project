from pygame import *
from math import *
size=width,height=800,600
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
sx,sy = mouse.get_pos()
mmode = "up"
screen.fill(WHITE)
r = 15
running = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONDOWN:
            sx,sy = mouse.get_pos()
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()
    




    draw.ellipse(screen,GREEN,(420,420,100,100))
    for x in range(440,501):
        for y in range(440,501):
            if (30**2)*((x-470)**2) + (30**2)*((y-470)**2) <= (30**2)*(30**2):
                screen.set_at((x,y),(0,0,0,0))


    
    if mmode == "up" and mb[0] == 1:
        screenshot = screen.copy()
        mmode = "down"
    if mmode == "down":
        mx,my = mouse.get_pos()
        screen.blit(screenshot,(0,0))
        ellipserect = Rect(sx,sy,mx-sx,my-sy)
        if mb[0] == 0:
            mmode = "up"
            a = min(sx,mx)
            b = min(my,sy)
            c = abs(mx-sx)
            d = abs(my-sy)
            screen.blit(screenshot,(0,0))
            draw.ellipse(screen,GREEN,(a,b,c,d))
            for x in range(a+r,a+c-r):
                for y in range(b+r,b+d-r):
                    if ((d//2-r)**2)*((x-(a+c//2))**2)+((c//2-r)**2)*((y-(b+d//2))**2) <= ((r-c//2)**2)*((r-d//2)**2):
                        screen.set_at((x,y),(0,0,0,0))

    display.flip()
    
quit()
