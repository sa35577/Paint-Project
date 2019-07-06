from pygame import *
size=width,height=1440,600
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
##########initialize ALL variables
col=BLACK
thick=2
tool="no tool"

#########defining all RECTS
pencilRect=Rect(20,80,40,40)
eraserRect=Rect(70,80,40,40)
canvasRect=Rect(150,80,600,500)
palRect = Rect(900,200,400,400)

#######load all images
palPic = image.load("Images/palette.png")

draw.rect(screen,WHITE,canvasRect)
screen.blit(palPic,(900,200))


running=True
while running:

    print(tool)
    for evt in event.get():
        if evt.type==QUIT:
            running=False
                       
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()

    ####draw ALL rects
    draw.rect(screen,GREEN,pencilRect,2)
    draw.rect(screen,GREEN,eraserRect,2)


    #####selecting the tool
    if mb[0]==1:
        if pencilRect.collidepoint(mx,my):
            tool="pencil"
        elif eraserRect.collidepoint(mx,my):
            tool="eraser"

    #####using the tools
    if mb[0]==1:
        if canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect) #only updates Canvas    rect
            if tool=="pencil":
                draw.line(screen,col,(omx,omy),(mx,my))
            elif tool == "eraser":
                draw.circle(screen,WHITE,(mx,my),10)
            screen.set_clip(None)
    ###change the color
    if mb[0] == 1:
        if palRect.collidepoint(mx,my):
            col=screen.get_at((mx,my))
            print(col)

    
            
    omx=mx
    omy=my
    
    display.flip() 

quit()
