#tool_text
from pygame import *
size=width,height=800,600
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)

font.init()

tfont = font.SysFont("Bradley Hand ITC", 35)



class tool:
    def __init__(self,button,image,name):
        self.button=button
        self.image=image
        self.name = name

pencil = tool(Rect(100,100,50,50),image.load("Images/pencil.jpg"),"pencil")
eraser = tool(Rect(100,160,50,50),image.load("Images/eraser.jpg"),"eraser")
brush = tool(Rect(100,220,50,50),image.load("Images/brush.jpg"),"brush")
spray = tool(Rect(100,280,50,50),image.load("Images/spray.jpg"),"spray")
line = tool(Rect(100,340,50,50),image.load("Images/line.jpg"),"line")
eyedropper = tool(Rect(100,400,50,50),image.load("Images/eyedropper.jpg"),"eyedropper")
rectangle = tool(Rect(100,460,50,50),image.load("Images/rectangle.jpg"),"rectangle")
ellipse = tool(Rect(100,520,50,50),image.load("Images/ellipse.jpg"),"ellipse")
polygon = tool(Rect(100,580,50,50),image.load("Images/polygon.jpg"),"polygon")
calligraphy = tool(Rect(25,25,50,50),image.load("Images/calligraphy.jpg"),"calligraphy")
trash = tool(Rect(100,640,50,50),image.load("Images/trash.png"),"trash")
undo = tool(Rect(160,100,50,50),image.load("Images/undo.jpg"),"undo")
redo = tool(Rect(220,100,50,50),image.load("Images/redo.jpg"),"redo")
border = tool(Rect(280,100,50,50),image.load("Images/borderrect.jpg"),"border")
fill = tool(Rect(340,100,50,50),image.load("Images/fillrect.jpg"),"fill")
background = tool(Rect(1100,400,50,50),image.load("Images/background.jpg"),"background")
backgroundfill = tool(Rect(1200,400,50,50),image.load("Images/backgroundfill.jpg"),"backgroundfill")
x = [pencil,eraser,brush,spray,line,eyedropper,rectangle,ellipse,polygon,trash,undo,redo,background,backgroundfill,calligraphy]

usingtool = ""
wordtool = ""
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False

    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()

    for i in x: #for all elements in the class
        screen.blit(i.image,(i.button.left,i.button.top)) #blits the image of each picture
        if i.button.collidepoint(mx,my) and mb[0] == 1:
            usingtool = i
            wordtool = i.name
    draw.rect(screen,WHITE,(300,300,400,200))
    if wordtool == "pencil":
        screen.blit(tfont.render("Tool: Pencil",True,BLACK),(300,300))
        screen.blit(tfont.render("Click on the canvas and move the cursor to draw",True,BLACK),(300,350))
    
    
    display.flip() 

quit()
