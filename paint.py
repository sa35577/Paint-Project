#paint.py
#imports the pygame,random,math,tkinter (specifically for tkinter.filedialog modlues
from pygame import *
from random import *
from math import *
from tkinter import *
from tkinter.filedialog import *


root = Tk()
root.withdraw()


init() #initialize everything in pygame, including the mixer and font
tfont = font.SysFont("Bradley Hand ITC", 35)
t2font = font.SysFont("Bradley Hand ITC", 20)
mixer.music.load("MP3 Files/Beyblade Burst Super Z Opening.mp3") #loads the song 
mixer.music.play() #plays the music


#setting screen size, and setting the editing display for the screen
size=width,height = 1440,720 #change this
screen=display.set_mode(size)

#declaring color tuples
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
col = BLACK
backgroundcol = WHITE


#creating a class named "tool" that has the attributes button, image, and name
class tool:
    def __init__(self,button,image,name):
        self.button=button
        self.image=image
        self.name = name
        
#defining the space of the canvas
canvas = Rect(200,200,800,500)

#loading the color palette
palette = image.load("Images/palette.png")
paletterect = Rect(1200,200,220,220)

#adding all elements to the class, each with a rectangle, image, and name
theme = tool(Rect(84,2,1271,715),image.load("Images/theme.jpg"),"theme")
pencil = tool(Rect(100,100,50,50),image.load("Images/pencil.jpg"),"pencil")
eraser = tool(Rect(100,160,50,50),image.load("Images/eraser.jpg"),"eraser")
brush = tool(Rect(100,220,50,50),image.load("Images/brush.jpg"),"brush")
spray = tool(Rect(100,280,50,50),image.load("Images/spray.jpg"),"spray")
line = tool(Rect(100,340,50,50),image.load("Images/line.jpg"),"line")
eyedropper = tool(Rect(100,400,50,50),image.load("Images/eyedropper.jpg"),"eyedropper")
rectangle = tool(Rect(100,460,50,50),image.load("Images/rectangle.jpg"),"rectangle")
ellipse = tool(Rect(100,520,50,50),image.load("Images/ellipse.jpg"),"ellipse")
polygon = tool(Rect(100,580,50,50),image.load("Images/polygon.jpg"),"polygon")
calligraphy = tool(Rect(40,40,50,50),image.load("Images/calligraphy.jpg"),"calligraphy")
highlighter = tool(Rect(100,40,50,50),image.load("Images/highlighter.png"),"highlighter")
trash = tool(Rect(100,640,50,50),image.load("Images/trash.png"),"trash")
undo = tool(Rect(160,100,50,50),image.load("Images/undo.jpg"),"undo")
redo = tool(Rect(220,100,50,50),image.load("Images/redo.jpg"),"redo")
border = tool(Rect(280,100,50,50),image.load("Images/borderrect.jpg"),"border")
fill = tool(Rect(340,100,50,50),image.load("Images/fillrect.jpg"),"fill")
background = tool(Rect(1100,400,50,50),image.load("Images/background.jpg"),"background")
backgroundfill = tool(Rect(1200,400,50,50),image.load("Images/backgroundfill.jpg"),"backgroundfill")
save = tool(Rect(1100,460,50,50),image.load("Images/save.png"),"save")
achilles = tool(Rect(1100,600,80,80),image.load("Images/achilles.png"),"achilles")
valkyrie = tool(Rect(1200,600,80,80),image.load("Images/valkyrie.png"),"valkyrie")
spriggan = tool(Rect(1300,600,80,80),image.load("Images/spriggan.png"),"spriggan")
fafnir = tool(Rect(1400,600,80,80),image.load("Images/fafnir.png"),"fafnir")
xcalibur = tool(Rect(1500,600,80,80),image.load("Images/xcalibur.png"),"xcalibur")
free = tool(Rect(1600,600,80,80),image.load("Images/free.png"),"free")
shu = tool(Rect(1700,600,80,80),image.load("Images/shu.png"),"shu")
stampleft = tool(Rect(1050,615,50,50),image.load("Images/left.jpg"),"left")
stampright = tool(Rect(1380,615,50,50),image.load("Images/right.jpg"),"right")
valtvsfree = image.load("Images/valtvsfree.png")
valtvsfreemini = tool(Rect(1000,100,80,80),transform.scale(valtvsfree,(96,54)),"valtvsfree")



#creating a list of all tools
x = [pencil,eraser,brush,spray,line,eyedropper,rectangle,ellipse,polygon,trash,undo,redo,background,backgroundfill,calligraphy,save,highlighter]
y = [border,fill]
imgs = [achilles,valkyrie,spriggan,fafnir,xcalibur,free,shu]
backs = [valtvsfree]
minibacks = [valtvsfreemini]
#declaring empty variables usingtool (for the tool name assigned by computer) and wordtool (for the tool's name attribute, for me to understand)
usingtool = ""
wordtool = ""
prevwordtool = ""
usingfiller = fill
wordfiller = "fill"
prevwordfiller = "fill"
#declaring variable r for the radius for tools such as the brush
sprayr = 50
prevsprayr = 0
brushr = 20
prevbrushr = 0
eraserr = 10
preveraserr = 0
rectr = 5
prevrectr = 0
ellipser = 10
prevellipser = 0
callir = 3
prevcallir = 0
hir = 10
prevhir = 0

#initializing omx and omy to be 0,0
omx,omy = 0,0

#setting variable gamestart for a start screen
gamestart = "no"

#variables needed for polygon tool
mmode = "up"
vertices = []

#ellipse variables
lock2 = False
#variables needed for undo and redo
screenshots = []
mmode2,mmode3 = "up","up"
mmode4 = "up"
undostatus,redostatus = "off","off"
count = -2
firstredo = False

#for stamps
mmode5 = "up"
usingstamp = ""
wordstamp = ""
stamppos = 0
mmode6 = "up"
mmode7 = "up"
lock = False

mmode8 = "up"
newimg = ""
#pygame loop
running=True
while running:
    for evt in event.get():
        #will quit if the close window button is clicked
        if evt.type==QUIT:
            running=False
        #checks if the mouse has been pressed
        if evt.type == MOUSEBUTTONDOWN:
            sx,sy  = mouse.get_pos() #gets position of the mouse
            screenshot = screen.copy() #takes a screenshot of the current window, used for displaying only 1 line, shape, or ellipse while you hold the mouse down
            if evt.button == 4:
                if wordtool == "eraser" and eraserr < 100:
                    eraserr += 5
                if wordtool == "brush" and brushr < 100:
                    brushr += 5
                if wordtool == "spray" and sprayr < 200:
                    sprayr += 5
                if wordtool == "rectangle" and rectr < 50:
                    rectr += 1
                if wordtool == "ellipse" and ellipser < 50:
                    ellipser += 1
                if wordtool == "calligraphy" and callir < 10:
                    callir += 1
                if wordtool == "highlighter" and hir < 50:
                    hir += 5
            if evt.button == 5:
                if wordtool == "eraser" and eraserr > 5:
                    eraserr -= 5
                if wordtool == "brush" and brushr > 5:
                    brushr -= 5
                if wordtool == "spray" and sprayr > 20:
                    sprayr -= 5
                if wordtool == "rectangle" and rectr > 1:
                    rectr -= 1
                if wordtool == "calligraphy" and callir > 1:
                    callir -= 1
                if wordtool == "highlighter" and hir > 5:
                    hir -= 5
    if mixer.music.get_busy() == False:
        mixer.music.play()
    mb=mouse.get_pressed() #mb holds the status if the mouse is pressed
    mx,my=mouse.get_pos()  #the position of the mouse is stored in the ordered pair (mx,my)

    if gamestart == "no": #checks if gamestart is "no", which means the game has just opened, and will be taken to the start screen
        screen.blit(theme.image,(theme.button.left,theme.button.top))
        starter = Rect(600,525,200,70)
        draw.rect(screen,GREEN,starter)
        
        if starter.collidepoint(mx,my):
            draw.rect(screen,BLUE,(597,523,203,73),3)
        if mb[0] == 1 and starter.collidepoint(mx,my):
            gamestart = "firsttime"
        display.flip()
    elif gamestart == "firsttime": #checks if gamestart is "firsttime", which means the start button was just clicked, and we need to put the background, palette, and canvas on to start the game
        screen.fill(GREEN)
        #loading the palette image
        screen.blit(palette,(1200,200))
        #drawing the canvas
        draw.rect(screen,WHITE,canvas)
        draw.rect(screen,BLUE,(1100,50,225,30))
        display.flip()
        gamestart = "on"
    else: #the only other option is "on", which will have code for the game
        for i in x: #for all elements in the class
            screen.blit(i.image,(i.button.left,i.button.top)) #blits the image of each picture
            if i.button.collidepoint(mx,my): #checks if the mouse is on the image
                draw.rect(screen,RED,(i.button.left-3,i.button.top-3,56,56),3) #draws a red rectangle around it
            else:
                draw.rect(screen,GREEN,(i.button.left-3,i.button.top-3,56,56),3) #otherwise, a green rectangle is drawn around it
            if i.button.collidepoint(mx,my) and mb[0] == 1: #checks if the mouse is on the button and the mouse is pressed
                usingtool = i #stores the tool beig used (the one the computer will understand) in usingtool
                wordtool = i.name #stores the name of the tool itself in wordtool
                print(wordtool)
            if usingtool != "": #checks if a tool is in use
                draw.rect(screen,BLUE,(usingtool.button.left-3,usingtool.button.top-3,56,56),3) #will draw a blue rectagle around the tool's image
        for i in y: #for all elements in the class
            screen.blit(i.image,(i.button.left,i.button.top)) #blits the image of teach picture
            if i.button.collidepoint(mx,my): #checks if the mouse is on the image
                draw.rect(screen,(255,255,0),(i.button.left-3,i.button.top-3,56,56),3) #draws a red rectangle around it
            else:
                draw.rect(screen,BLACK,(i.button.left-3,i.button.top-3,56,56),3) #otherwise, a green rectangle is drawn around it
            if i.button.collidepoint(mx,my) and evt.type == MOUSEBUTTONDOWN: #checks if the mouse is on the button and the mouse is pressed
                usingfiller = i #stores the tool beig used (the one the computer will understand) in usingtool
                wordfiller = i.name #stores the name of the tool itself in wordtool
            if usingfiller != "": #checks if a tool is in use
                draw.rect(screen,(0,255,255),(usingfiller.button.left-3,usingfiller.button.top-3,56,56),3) #will draw a blue rectagle around the tool's image
        for i in imgs:
            if i.button.collidepoint(mx,my) and mb[0] == 1 and mmode5 == "up":
                wordstamp = i.name
                usingstamp = i
        for i in range(3):
            screen.blit(imgs[i].image,(imgs[i].button.left,imgs[i].button.top))
        for i in range(len(minibacks)):
            screen.blit(minibacks[i].image,(minibacks[i].button.left,minibacks[i].button.top))
        screen.blit(stampleft.image,(stampleft.button.left,stampleft.button.top))
        screen.blit(stampright.image,(stampright.button.left,stampright.button.top))

        if mb[0] == 1 and stampleft.button.collidepoint(mx,my) and mmode6 == "up" and lock == False:
            mmode6 = "down"
            lock = True
            imgs.append(imgs[0])
        if mb[0] == 0 and mmode6 == "down":
            mmode6 = "up"
            del imgs[0]
            lock = False
            for j in range(3):
                draw.rect(screen,GREEN,(1100+(100*j),600,80,80))
            for j in range(len(imgs)):
                imgs[j].button = Rect(1100+100*j,600,80,80)
        if mb[0] == 1 and stampright.button.collidepoint(mx,my) and mmode7 == "up" and lock == False:
            mmode7 = "down"
            lock = True
            imgs = [imgs[-1]] + imgs
        if mb[0] == 0 and mmode7 == "down":
            mmode7 = "up"
            del imgs[-1]
            lock = False
            for j in range(3):
                draw.rect(screen,GREEN,(1100+(100*j),600,80,80))
            for j in range(len(imgs)):
                imgs[j].button = Rect(1100+100*j,600,80,80)
        if wordtool == "undo":
            undostatus = "on"
        elif wordtool == "redo":
            redostatus = "on"
        else:
            undostatus = "off"
            redostatus = "off"
            firstredo = True
            count = -2
            if mmode == "up" and mb[0] == 1:
                mmode = "down"
            if mmode == "down" and mb[0] == 0:
                if wordtool in ["pencil","eraser","brush","spray","line","rectangle","polygon","trash","background","backgroundfill","calligraphy"]:
                    screenshots.append(screen.copy())
                mmode = "up"
        for i in imgs:
            if i.name == wordstamp:
                if i.button.collidepoint(mx,my) and mb[0] == 1 and mmode5 == "up" and lock == False:
                    wordtool = ""
                    usingtool = ""
                    screen.set_clip(canvas)
                    lock = True
                    mouse.set_visible(False)
                    mmode5 = "down"
                if mmode5 == "down":
                    if mb[0] == 1:
                        screen.blit(screenshot,(0,0))
                        if canvas.collidepoint(mx,my):
                            screen.blit(i.image,(mx-i.button.width//2,my-i.button.height//2))
                    if mb[0] == 0:
                        lock = False
                        mmode5 = "up"
                        mouse.set_visible(True)
                        screen.set_clip(None)
       
        for i in minibacks:
            if i.button.collidepoint(mx,my) and mb[0] == 1:
                iindex = minibacks.index(i)
                screen.blit(transform.scale(backs[iindex],(canvas.width,canvas.height)),(200,200))
        if mb[0] == 1:
            if wordtool == "eyedropper": #checks if the mouse is pressed and the tool selected is the eyedropper 
                if paletterect.collidepoint(mx,my): #checks if the mouse is on the palette
                    col = screen.get_at((mx,my)) #take the color of the pixel the mouse is on, stores it in variable col
            elif wordtool == "backgroundfill":
                if paletterect.collidepoint(mx,my):
                    backgroundcol = screen.get_at((mx,my))
                    draw.rect(screen,screen.get_at((mx,my)),canvas)
            elif wordtool == "background" and mmode8 == "up":
               try:
                   fname = askopenfilename(filetypes=(("JPG Image","*.jpg*"),
                                                 ("PNG Image","*.png*") ))
                   
                   newimg = image.load("%s" % fname)
                   newimgrect = newimg.get_rect()
                   mmode8 = "down"
                   screenshot = screen.copy()
                       
                   if newimgrect.width >= 800 or newimgrect.height >= 500:
                       newimg = transform.scale(newimg,(800,500))
                       screen.blit(newimg,(200,200))
                       newimg = ""
                       mmode8 = "up"
                   backgroundcol = 0
                   
               except:
                   pass 
               wordtool = ""
               usingtool = ""
            elif wordtool == "save":
                try:
                    fname = asksaveasfilename(defaultextension=".png")
                    if fname != "":
                        image.save(screen.subsurface(canvas),fname)
                    fname = ""
                except:
                    pass
                
        if newimg != "":
            if canvas.collidepoint(mx,my) and mmode8 == "down":
                screen.blit(screenshot,(0,0))
                screen.blit(newimg,(mx-(newimgrect.width)//2,my-(newimgrect.height)//2))
                if evt.type == MOUSEBUTTONDOWN and evt.button == 1:
                    newimg = ""
                    mmode8 = "up"
        
        if mb[0] == 1 and canvas.collidepoint(mx,my): #checking if the mouse is pressed while you are on the canvas
            screen.set_clip(canvas) #only lets the canvas be edited
            dx = mx-omx #distance from the old mx to mx
            dy = my-omy #distance from the old my to my
            dist = int(sqrt(dx**2+dy**2)) #finding the distasnce from (omx,omy) to (mx,my)
            
            if wordtool == "pencil": #checks if the tool is pencil
                draw.line(screen,col,(omx,omy),(mx,my),1) #draws a line from (omx,omy) to (mx,my)
            elif wordtool == "eraser": #checks if the tool is eraser
                if backgroundcol != 0:
                    for i in range(1,dist+1):
                        draw.circle(screen,backgroundcol,(int(omx+i*dx/dist),int(omy+i*dy/dist)),eraserr)
                else:
                    for i in range(1,dist+1):
                        try:
                            screen.blit(newimg.subsurface(int(omx+i*dx/dist)-eraserr//2-200,int(omy+i*dy/dist)-eraserr//2-200,eraserr,eraserr),(int(omx+i*dx/dist),int(omy+i*dy/dist)))
                        except:
                            pass
            elif wordtool == "brush": #checks if the tool is brush
                for i in range(1,dist+1): #loops through every natural number from 1 to dist, inclusive
                    draw.circle(screen,col,(int(omx+i*dx/dist),int(omy+i*dy/dist)),brushr) #draws a circle of raduis brushr towards mx,my
                
            elif wordtool == "spray": #checks if the tool is spraypaint
                for i in range(sprayr//10): #loops through sprayr//10 times
                    rx,ry = randint(mx-sprayr,mx+sprayr),randint(my-sprayr,my+sprayr) #takes a random pair of integers within a square of 2*sprayr by 2*sprayr, with its center at (mx,my)
                    if (rx-mx)**2+(ry-my)**2<=sprayr**2: #checking if the point lies in the circle with center (mx,my) and radius sprayr
                        draw.rect(screen,col,(rx,ry,1,1)) #draws a rectangle with the size of 1 pixel
            elif wordtool == "line":#checks if the tool is a line
                screen.blit(screenshot,(0,0)) #places the screenshot on
                draw.line(screen,col,(sx,sy),(mx,my)) #draws the line, from the point the mouse was on when pressed ((sx,sy))
            elif wordtool == "rectangle": #checks if the tool is a rectangle
                if wordfiller == "fill":
                    screen.blit(screenshot,(0,0)) #places the screenshot on
                    draw.rect(screen,col,(sx,sy,mx-sx,my-sy)) #draws a rectangle with the top left corner of the old position of the cursor, and the opposite corner at the new position of the cursor
                elif wordfiller == "border":
                    screen.blit(screenshot,(0,0))
                    draw.rect(screen,col,(sx,sy,mx-sx,my-sy),rectr)
                    c1 = min(mx,sx)
                    c2 = min(my,sy)
                    c3 = max(mx,sx)
                    c4 = max(my,sy)
                    draw.rect(screen,col,(c1-(rectr-1)//2,c2-(rectr-1)//2,rectr,rectr))
                    draw.rect(screen,col,(c1-(rectr-1)//2,c4-(rectr+1)//2,rectr,rectr))
                    draw.rect(screen,col,(c3-(rectr+1)//2,c2-(rectr-1)//2,rectr,rectr))
                    draw.rect(screen,col,(c3-(rectr+1)//2,c4-(rectr+1)//2,rectr,rectr))
            elif wordtool == "trash":
                draw.rect(screen,backgroundcol,canvas)
            elif wordtool == "calligraphy":
                for i in range(1,dist+1):
                    dotx = int(omx+i*dx/dist)
                    doty = int(omy+i*dy/dist)
                    draw.rect(screen,col,(dotx-(callir//2),doty-callir,callir,callir*2))
            elif wordtool == "highlighter":
                marker = Surface((hir,hir),SRCALPHA)
                draw.circle(marker,(col[0],col[1],col[2],10),(hir//2,hir//2),(hir//2))
                for i in range(1,dist+1,2):
                    screen.blit(marker,(int(omx+i*dx/dist),int(omy+i*dy/dist)))
            screen.set_clip(None)
        
        if canvas.collidepoint(mx,my):
            screen.set_clip(canvas)
            if wordtool == "ellipse": #checks if the tool is an ellipse
                if mmode4 == "up" and mb[0] == 1:
                    screenshot = screen.copy()
                    mmode4 = "down"
                    sx,sy = mouse.get_pos()
                if mmode4 == "down" and mb[0] == 1:
                    mx,my = mouse.get_pos()
                    screen.blit(screenshot,(0,0))
                    draw.rect(screen,col,(sx,sy,mx-sx,my-sy),1)
                if mmode4 == "down" and mb[0] == 0:
                    mmode4 = "up"
                    screen.blit(screenshot,(0,0))
                    try:
                        if wordfiller == "fill":
                            draw.ellipse(screen,col,(min(mx,sx),min(my,sy),abs(mx-sx),abs(my-sy)))
                        elif wordfiller == "border":
                            draw.ellipse(screen,col,(min(mx,sx),min(my,sy),abs(mx-sx),abs(my-sy)),ellipser)
                        screenshots.append(screen.copy())
                    except:
                        pass
                    
            elif wordtool == "polygon":
                if mmode2 == "up" and mb[0] == 1:
                    screenshot = screen.copy()
                    mmode2 = "down"
                if mmode2 == "down" and mb[0] == 0:
                    mmode2 = "up"
                    tx,ty = mouse.get_pos()
                    draw.rect(screen,col,(tx,ty,1,1))
                    if len(vertices) > 0:
                        draw.line(screen,col,(vertices[-2],vertices[-1]),(tx,ty))
                    if canvas.collidepoint(tx,ty):
                        vertices.append(tx)
                        vertices.append(ty)
                if mb[2] == 1:
                    try:
                        draw.line(screen,col,(tx,ty),(vertices[0],vertices[1]))
                        vertices = []
                    except IndexError:
                        pass
            elif wordtool == "undo":
                if mmode2 == "up" and mb[0] == 1:
                    mmode2 = "down"
                if mmode2 == "down" and mb[0] == 0:
                    mmode2 = "up"
                    draw.rect(screen,WHITE,canvas)
                    try: 
                        screen.blit(screenshots[count],(0,0))
                    except IndexError:
                        pass
                    count -= 1
            elif wordtool == "redo":
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
                    try:
                        screen.blit(screenshots[count],(0,0))
                    except IndexError:
                        pass
                
            screen.set_clip(None) #this will allow editing all over the pygame window now
        if prevwordtool != wordtool or prevwordfiller != wordfiller:
            draw.rect(screen,WHITE,(400,50,405,100))
        if wordtool == "pencil":
            screen.blit(tfont.render("Tool: Pencil",True,BLACK),(400,50))
            screen.blit(t2font.render("Click on the canvas and move the cursor to draw.",True,BLACK),(400,85))
        elif wordtool == "eraser":
            screen.blit(tfont.render("Tool: Eraser",True,BLACK),(400,50))
            if preveraserr != eraserr:
                draw.rect(screen,WHITE,(525,90,45,20))
            screen.blit(t2font.render("Eraser Radius: %i" % eraserr,True,BLACK),(400,85))
        elif wordtool == "brush":
            screen.blit(tfont.render("Tool: Brush",True,BLACK),(400,50))
            if prevbrushr != brushr:
                draw.rect(screen,WHITE,(525,90,45,20))
            screen.blit(t2font.render("Brush Radius: %i" % brushr,True,BLACK),(400,85))
        elif wordtool == "spray":
            screen.blit(tfont.render("Tool: Spray",True,BLACK),(400,50))
            if prevsprayr != sprayr:
                draw.rect(screen,WHITE,(525,100,45,20))
            screen.blit(t2font.render("Spray Radius: %i" % sprayr,True,BLACK),(400,95))
        elif wordtool == "line":
            screen.blit(tfont.render("Tool: Line",True,BLACK),(400,50))
            screen.blit(t2font.render("1. Press and hold on starting point.",True,BLACK),(400,85))
            screen.blit(t2font.render("2. Move the cursor and let go where you",True,BLACK),(400,110))
            screen.blit(t2font.render("    want to end.",True,BLACK),(400,125))
        elif wordtool == "eyedropper":
            screen.blit(tfont.render("Tool: Eyedropper",True,BLACK),(400,50))
            screen.blit(t2font.render("Select a colour from the colour palette.",True,BLACK),(400,85))
        elif wordtool == "rectangle":
            screen.blit(tfont.render("Tool: Rectangle",True,BLACK),(400,50))
            screen.blit(t2font.render("1. Press and hold on starting point.",True,BLACK),(400,85))
            screen.blit(t2font.render("2. Release on the opposite corner.",True,BLACK),(400,105))
            if wordfiller == "border":
                if prevrectr != rectr:
                    draw.rect(screen,WHITE,(543,127,40,23))
                screen.blit(t2font.render("Rectangle width:  %i" % rectr,True,BLACK),(400,122))
        elif wordtool == "ellipse":
            screen.blit(tfont.render("Tool: Ellipse",True,BLACK),(400,50))
            screen.blit(t2font.render("1. Press and hold on a corner.",True,BLACK),(400,85))
            screen.blit(t2font.render("2. Release on the opposite corner.",True,BLACK),(400,105))
            if wordfiller == "border":
                if prevellipser != ellipser:
                    draw.rect(screen,WHITE,(543,127,40,23))
                screen.blit(t2font.render("Ellipse thickness:  %i" % ellipser,True,BLACK),(400,122))
        elif wordtool == "calligraphy":
            screen.blit(tfont.render("Tool: Calligraphy",True,BLACK),(400,50))
            screen.blit(t2font.render("Click on the canvas and move the cursor to draw.",True,BLACK),(400,85))
            if prevcallir != callir:
                draw.rect(screen,WHITE,(600,116,30,25))
            screen.blit(t2font.render("Calligraphy Thickness:  %i" % callir,True,BLACK),(400,110))
        elif wordtool == "undo":
            screen.blit(tfont.render("Tool: Undo",True,BLACK),(400,50))
            screen.blit(t2font.render("Click on the canvas to undo",True,BLACK),(400,85))
        elif wordtool == "redo":
            screen.blit(tfont.render("Tool: Redo",True,BLACK),(400,50))
            screen.blit(t2font.render("Click on the canvas to redo",True,BLACK),(400,85))
        elif wordtool == "backgroundfill":
            screen.blit(tfont.render("Tool: Background Fill",True,BLACK),(400,50))
            screen.blit(t2font.render("Choose a color by clicking on the palette.",True,BLACK),(400,85))
        elif wordtool == "polygon":
            screen.blit(tfont.render("Tool: Polygon",True,BLACK),(400,50))
            screen.blit(t2font.render("1. Left click to select first vertex.",True,BLACK),(400,85))
            screen.blit(t2font.render("2. Left click to select next vertex.",True,BLACK),(400,105))
            screen.blit(t2font.render("3. Right click to enclose shape",True,BLACK),(400,125))
        elif wordtool == "trash":
            screen.blit(tfont.render("Tool: Trash",True,BLACK),(400,50))
            screen.blit(t2font.render("Click on the canvas to clear the screen.",True,BLACK),(400,85))
        elif wordtool == "highlighter":
            screen.blit(tfont.render("Tool: Highlighter",True,BLACK),(400,50))
            if prevhir != hir:
                draw.rect(screen,WHITE,(570,100,45,20))
            screen.blit(t2font.render("Highlighter Radius: %i" % hir,True,BLACK),(400,95))
        if omx != mx or omy != my:
            draw.rect(screen,BLUE,(1230,50,95,30))

        screen.blit(t2font.render("Mouse position: %s,%s" % (mx,my),True,WHITE),(1100,50))
            
            
            
            
            
        

        prevwordtool = wordtool
        preveraserr = eraserr
        prevbrushr = brushr
        prevsprayr = sprayr
        prevrectr = rectr
        prevellipser = ellipser
        prevcallir = callir
        prevhir = hir
        prevwordfiller = wordfiller
        
        
        omx = mx #setting omx to the mx value, as mx will get a new value
        omy = my #setting omy to the my value, as my will get a new value
        
        display.flip() #"flips" the screen

del tfont
del t2font
quit() #quit the window


