#textures.py
from pygame import *
size=width,height=800,600
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)

picNames = ["Images/brick.jpg","Images/dirt.jpg","Images/grass.jpg","Images/massey.jpg"] #list of strings
textures = []
for name in picNames:
    pic = image.load(name) #load the actual picture
    textures.append(pic) #list of actual pictures


####at this point, the textures list has 3 images

canvasRect = Rect(100,50,600,500)
screen.fill((255,170,200))
draw.rect(screen,WHITE,canvasRect)

pos = 0 #the first background
##sub = textures[pos].subsurface((0,0,50,50))
##screen.blit(sub,(25,50))

n = len(textures)


running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type == MOUSEBUTTONDOWN:
            if evt.button == 4: #scroll up
                pos = (pos + 1) % n
            if evt.button == 5: #scroll down
                pos = (pos - 1) % n

    
    sub = textures[pos].subsurface((0,0,50,50))
    screen.blit(sub,(25,50))
    
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    
    if canvasRect.collidepoint(mx,my):
        if mb[0] == 1:
            draw.line(screen,RED,(omx,omy),(mx,my))
        if mb[2] == 1:
            sample = textures[pos].subsurface((mx-15,my-15,30,30))
            screen.blit(sample,(mx,my))


    omx = mx
    omy = my
            
    
    display.flip() 

quit()
