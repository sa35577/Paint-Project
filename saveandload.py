#saveandload.py
from pygame import *
from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
root = Tk()
root.withdraw()
size=width,height=800,600
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
saveRect=Rect(50,50,40,40)
loadRect=Rect(100,50,40,40)
canvasRect=Rect(200,150,500,400)
fname = ""
mmode = "up"
draw.rect(screen,WHITE,canvasRect)
draw.rect(screen,BLUE,saveRect)
draw.rect(screen,GREEN,loadRect)
sx,sy = 0,0
print(RED[0],RED[1],RED[2])
##draw.line(screen,RED,(250,200),(500,340))
##draw.rect(screen,(125,150,160),(300,400,200,100))
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type == MOUSEBUTTONDOWN:
            sx,sy = mouse.get_pos()


    mb=mouse.get_pressed()
    mx,my = mouse.get_pos()
    

    
    if fname != "":
        if canvasRect.collidepoint(mx,my) and mmode == "down":
            screen.blit(screenshot,(0,0))
            screen.blit(x,(mx-(z.width)//2,my-(z.height)//2))
            if evt.type == MOUSEBUTTONDOWN and evt.button == 1:
                fname = ""
                mmode = "up"

    
    if saveRect.collidepoint(sx,sy) and mb[0] == 1:
        sx,sy = 0,0
        try:
            fname = asksaveasfilename(defaultextension=".jpg")
            if fname != "":
                image.save(screen.subsurface(canvasRect),fname)

            fname = ""
        except:
            print("Saving error")
        
    if loadRect.collidepoint(mx,my) and mb[0] == 1 and mmode == "up":
        try:
            fname = askopenfilename(filetypes=(("JPG Image","*.jpg*"),
                                                 ("PNG Image","*.png*") ))
            if fname != "":
                x = (image.load("%s"%fname))
                z = x.get_rect()
                mmode = "down"
                screenshot = screen.copy()
        except:
            pass

        

    
    display.flip() 

quit()
