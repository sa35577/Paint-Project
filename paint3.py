#paint.py
#imports the pygame,random,math,tkinter (specifically for tkinter.filedialog modlues
from pygame import *
from random import *
from math import *
from tkinter import *
from tkinter.filedialog import *

#bringing Tk() for a file dialog
root = Tk()
root.withdraw()


init() #initialize everything in pygame, including the mixer and font
tfont = font.SysFont("Bradley Hand ITC", 35)
t2font = font.SysFont("Bradley Hand ITC", 20)
t3font = font.SysFont("Bradley Hand ITC", 50)

#setting the caption of display
display.set_caption("Paint Program Sat Arora")

tracks = ["Cho-Z Theme.mp3","Resonance Valt.mp3","Valt vs Lui.mp3","Valt vs Shu.mp3"]#our songs
songi = 0#song index

#setting screen size, and setting the editing display for the screen
size=width,height = 1440,720
screen=display.set_mode(size)

#declaring color tuples
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)

col = BLACK
backgroundcol = WHITE
prevcol = 0

#creating a class named "tool" that has the attributes button, image, and name
class tool:
    def __init__(self,button,image,name):
        self.button=button
        self.image=image
        self.name = name
        
#defining the space of the canvas
canvas = Rect(25,25,800,500)

#loading the color palette
palette = image.load("Images/palette.png")
paletterect = Rect(1200,200,220,220)

#adding all elements to the class, each with a rectangle, image, and name
theme = tool(Rect(84,2,1271,715),image.load("Images/theme.jpg"),"theme")
pencil = tool(Rect(30,540,40,40),image.load("Images/pencil.jpg"),"pencil")
eraser = tool(Rect(90,540,40,40),image.load("Images/eraser.jpg"),"eraser")
brush = tool(Rect(150,540,40,40),image.load("Images/brush.jpg"),"brush")
spray = tool(Rect(210,540,40,40),image.load("Images/spray.jpg"),"spray")
line = tool(Rect(270,540,40,40),image.load("Images/line.jpg"),"line")
calligraphy = tool(Rect(330,540,40,40),image.load("Images/calligraphy.jpg"),"calligraphy")
highlighter = tool(Rect(390,540,40,40),image.load("Images/highlighter.png"),"highlighter")

eyedropper = tool(Rect(30,600,40,30),image.load("Images/eyedropper.jpg"),"eyedropper")
rectangle = tool(Rect(90,600,40,40),image.load("Images/rectangle.jpg"),"rectangle")
ellipse = tool(Rect(150,600,40,40),image.load("Images/ellipse.jpg"),"ellipse")
polygon = tool(Rect(210,600,40,40),image.load("Images/polygon.jpg"),"polygon")
trash = tool(Rect(270,600,40,40),image.load("Images/trash.jpg"),"trash")
floodfill = tool(Rect(330,600,40,40),image.load("Images/floodfill.jpg"),"floodfill")

border = tool(Rect(30,660,40,40),image.load("Images/borderrect.jpg"),"border")
fill = tool(Rect(80,660,40,40),image.load("Images/fillrect.jpg"),"fill")

undo = tool(Rect(850,10,40,40),image.load("Images/undo.jpg"),"undo")
redo = tool(Rect(900,10,40,40),image.load("Images/redo.jpg"),"redo")

background = tool(Rect(850,60,40,40),image.load("Images/background.jpg"),"background")
backgroundfill = tool(Rect(900,60,40,40),image.load("Images/backgroundfill.jpg"),"backgroundfill")
save = tool(Rect(950,60,40,40),image.load("Images/save.png"),"save")

pause = tool(Rect(850,130,40,40),image.load("Images/pause.jpg"),"pause")
unpause = tool(Rect(900,130,40,40),image.load("Images/unpause.jpg"),"unpause")
shuffl = tool(Rect(950,130,40,40),image.load("Images/shuffle.jpg"),"shuffle")

volup = tool(Rect(850,200,40,40),image.load("Images/volume up.jpg"),"volup")
voldown = tool(Rect(900,200,40,40),image.load("Images/volume down.jpg"),"voldown")

achilles = tool(Rect(1100,600,80,80),image.load("Images/achilles.png"),"achilles")
valkyrie = tool(Rect(1200,600,80,80),image.load("Images/valkyrie.png"),"valkyrie")
spriggan = tool(Rect(1300,600,80,80),image.load("Images/spriggan.png"),"spriggan")
fafnir = tool(Rect(1400,600,80,80),image.load("Images/fafnir.png"),"fafnir")
xcalibur = tool(Rect(1500,600,80,80),image.load("Images/xcalibur.png"),"xcalibur")
free = tool(Rect(1600,600,80,80),image.load("Images/free.png"),"free")
shu = tool(Rect(1700,600,80,80),image.load("Images/shu.png"),"shu")
stampleft = tool(Rect(1050,615,50,50),image.load("Images/left.png"),"left")
stampright = tool(Rect(1380,615,50,50),image.load("Images/right.png"),"right")

#adding all backgrounds, with miniature pictures for a small scale
valtvsfree = image.load("Images/valtvsfree.png")
valtzone = image.load("Images/valtzone.png")
choshu = image.load("Images/choshu.png")
phi = image.load("Images/phi.png")
valtvsfreemini = tool(Rect(900,250,80,80),transform.scale(valtvsfree,(96,54)),"valtvsfree")
valtzonemini = tool(Rect(1000,250,80,80),transform.scale(valtzone,(96,54)),"valtzone")
choshumini = tool(Rect(900,320,80,80),transform.scale(choshu,(96,54)),"choshu")
phimini = tool(Rect(1000,320,80,80),transform.scale(phi,(96,54)),"phi")
#background of whole project
launch = image.load("Images/launch.png")

#creating a list of all tools
tools = [pencil,eraser,brush,spray,line,eyedropper,rectangle,ellipse,polygon,trash,undo,redo,background,backgroundfill,calligraphy,save,highlighter,floodfill,pause,unpause,shuffl,]
y = [border,fill]
imgs = [achilles,valkyrie,spriggan,fafnir,xcalibur,free,shu]

#list of backgrounds
backs = [valtvsfree,valtzone,choshu,phi]
minibacks = [valtvsfreemini,valtzonemini,choshumini,phimini]

#making all tools size 40 by 40
for i in range(len(tools)):
    tools[i].image = transform.scale(tools[i].image,(40,40))

#declaring empty variables of current and past tools, and current and past fill/unfillers
usingtool = ""
wordtool = ""
prevwordtool = ""
usingfiller = fill
wordfiller = "fill"
prevwordfiller = "fill"
#declaring variables ending with r for the radius/thickness for tools such as the brush
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
liner = 5
prevliner = 0
pencilr = 1
prevpencilr = 0

#initializing old mx and old my to be 0,0
omx,omy = 0,0

#setting variable gamestart for a start screen
gamestart = "no"

#variables needed for polygon tool
mmode = "up"
vertices = []

#ellipse variables
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

#boolean to avoid triggering save/load with stamps
lock = False

#more variables
mmode8 = "up"
newimg = ""
volume = 1
mmode9 = "up"

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
            screenshot2 = screen.copy() #does the same, except in screenshot2
            if evt.button == 4:
                #scrolling up, increase radius
                if wordtool == "pencil" and pencilr < 5:
                    pencilr += 1
                if wordtool == "line" and liner < 50:
                    liner += 1
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
                #scrolling down,decrease radius
                if wordtool == "pencil" and pencilr > 1:
                    pencilr -= 1
                if wordtool == "line" and liner > 1:
                    liner -= 1
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
    #play music if nothing is playing
    if mixer.music.get_busy() == False:#checks if playing
        mixer.music.load("MP3 Files/%s"%tracks[songi%4])#if not, will load next song in list (mod4 to restart)
        mixer.music.play()#play music
        songi += 1#increment songi
    
    mb=mouse.get_pressed() #mb holds the status if the mouse is pressed
    mx,my=mouse.get_pos()  #the position of the mouse is stored in the ordered pair (mx,my)

    if gamestart == "no": #checks if gamestart is "no", which means the game has just opened, and will be taken to the start screen
        screen.blit(theme.image,(theme.button.left,theme.button.top))
        starter = Rect(600,525,200,70)
        draw.rect(screen,(80,150,220),starter)
        screen.blit(t3font.render("Start",True,RED),(645,527))
        
        if starter.collidepoint(mx,my):
            draw.rect(screen,BLUE,(597,523,203,73),3)#drawing a blue rectangle around if hovered over
        if mb[0] == 1 and starter.collidepoint(mx,my):
            gamestart = "firsttime"#will move past "no" to "firsttime" if clicked
        display.flip()
    elif gamestart == "firsttime": #checks if gamestart is "firsttime", which means the start button was just clicked, and we need to put the background, palette, and canvas on to start the game
        screen.blit(launch,(0,0))#background
        #loading the palette image
        screen.blit(palette,(1200,200))
        #drawing the canvas
        draw.rect(screen,WHITE,canvas)
        screen.blit(image.load("Images/scroll.png"),(950,400))#scroll is the location for the explanation for the tools
        screen.blit(volup.image,(volup.button.left,volup.button.top))#blit volume down
        screen.blit(voldown.image,(voldown.button.left,voldown.button.top))#blit volume up
        display.flip()
        gamestart = "on"#will move to "on", and always stay there
    else: #the only other option is "on", which will have code for the game
        for i in tools: #for all elements in the class
            screen.blit(i.image,(i.button.left,i.button.top)) #blits the image of each picture
            if i.button.collidepoint(mx,my): #checks if the mouse is on the image
                draw.rect(screen,RED,(i.button.left-3,i.button.top-3,46,46),3) #draws a red rectangle around it
            else:
                draw.rect(screen,GREEN,(i.button.left-3,i.button.top-3,46,46),3) #otherwise, a green rectangle is drawn around it
            if i.button.collidepoint(mx,my) and mb[0] == 1 and lock == False: #checks if the mouse is on the button and the mouse is pressed
                usingtool = i #stores the tool beig used (the one the computer will understand) in usingtool
                wordtool = i.name #stores the name of the tool itself in wordtool
                usingstamp = ""
                wordstamp = ""
                
            if usingtool != "": #checks if a tool is in use
                draw.rect(screen,BLUE,(usingtool.button.left-3,usingtool.button.top-3,46,46),3) #will draw a blue rectagle around the tool's image
        for i in y: #for all elements in the class
            screen.blit(i.image,(i.button.left,i.button.top)) #blits the image of teach picture
            if i.button.collidepoint(mx,my): #checks if the mouse is on the image
                draw.rect(screen,(255,255,0),(i.button.left-3,i.button.top-3,46,46),3) #draws a red rectangle around it
            else:
                draw.rect(screen,BLACK,(i.button.left-3,i.button.top-3,46,46),3) #otherwise, a green rectangle is drawn around it
            if i.button.collidepoint(mx,my) and evt.type == MOUSEBUTTONDOWN: #checks if the mouse is on the button and the mouse is pressed
                usingfiller = i #stores the tool beig used (the one the computer will understand) in usingtool
                wordfiller = i.name #stores the name of the tool itself in wordtool
            if usingfiller != "": #checks if a tool is in use
                draw.rect(screen,(0,255,255),(usingfiller.button.left-3,usingfiller.button.top-3,46,46),3) #will draw a blue rectagle around the tool's image
        for i in imgs:#checking if any stamp is clicked on (and at the moment with the mmode5)
            if i.button.collidepoint(mx,my) and mb[0] == 1 and mmode5 == "up":
                #setting stamp variables
                wordstamp = i.name 
                usingstamp = i
                #taking out other tools to avoid collision
                wordtool = ""
                usingtool = ""
        for i in range(3):#blitting the first 3 stamps in the list
            screen.blit(imgs[i].image,(imgs[i].button.left,imgs[i].button.top))
        for i in range(len(minibacks)):#blitting all elements in the miniature backgrounds
            screen.blit(minibacks[i].image,(minibacks[i].button.left,minibacks[i].button.top))
        #displaying left and right buttons for stamps
        screen.blit(stampleft.image,(stampleft.button.left,stampleft.button.top))
        screen.blit(stampright.image,(stampright.button.left,stampright.button.top))
                                                                                    #boolean for avoiding collision with other tools
        if mb[0] == 1 and stampleft.button.collidepoint(mx,my) and mmode6 == "up" and lock == False:#checking if the left button was just clicked
            mmode6 = "down"#changing mouse mode for next statement
            lock = True #prevent collision
            imgs = [imgs[-1]] + imgs#putting the last element in the beginning
        if mb[0] == 0 and mmode6 == "down":#checking if just relleased
            mmode6 = "up"#changing mouse mode to enable clicking on button
            del imgs[-1]#remvoing last item
            lock = False#allow collision
            for j in range(len(imgs)):#setting the rest to be in positions behind, but not blitting
                imgs[j].button = Rect(1100+100*j,600,80,80)
            for j in range(3):
                screen.blit(launch.subsurface(1100+(100*j),600,80,80),(1100+(100*j),600))#blitting the new first 3 elements
        if mb[0] == 1 and stampright.button.collidepoint(mx,my) and mmode7 == "up" and lock == False: #checking if right button was just clicked
            mmode7 = "down"#changing mouse mode to enable next statement
            lock = True#prevent collision
            imgs.append(imgs[0])#putting the first item in last spot
        if mb[0] == 0 and mmode7 == "down":#checking if just released
            mmode7 = "up"#changing mouse mode to enable clicking
            del imgs[0]#removing first item
            lock = False#allow collision
            for j in range(len(imgs)):#setting all others behind
                imgs[j].button = Rect(1100+100*j,600,80,80)
            for j in range(3):#blitting first 3 items
                screen.blit(launch.subsurface(1100+(100*j),600,80,80),(1100+(100*j),600))
        if wordtool == "undo":#turns on the undostatus if undo button was clicked
            undostatus = "on"
        elif wordtool == "redo":#turns on redostatus if redo button was clicked
            redostatus = "on"
        else:#turns off undo and redo status,as well as firstredo
            undostatus = "off"
            redostatus = "off"
            firstredo = True
            count = -2
            if mmode == "up" and mb[0] == 1:#moment of click
                mmode = "down"#enable next statement
            if mmode == "down" and mb[0] == 0:#moment of release
                if wordtool in ["pencil","eraser","brush","spray","line","rectangle","polygon","trash","background","backgroundfill","calligraphy","undo","floodfill"]:
                    screenshots.append(screen.copy()) #append the screenshot if a tool capable of changing the canvas was used
                mmode = "up"#enable click

        if usingstamp != "":#checking if there is some stamp used
            lock = True#prevent collision
            screen.set_clip(canvas)#allowing the only part to change to be canvas
            mouse.set_visible(False)#turning off mouse visibility
            screen.blit(screenshot2,(0,0))#blitting screenshot
            screen.blit(usingstamp.image,(mx-usingstamp.button.width//2,my-usingstamp.button.height//2))#blitting the stamp with the center of mouse pos
            if mb[0] == 1 and mmode5 == "up":#moment of click
                mmode5 = "down"#enable release
            if mb[0] == 0 and mmode5 == "down":#moment of release
                mmode5 = "up"#enable click
                screenshots.append(screen.copy())#appending for undo/redo
            screen.set_clip(None)
            if mb[2] == 1:#right click will be the last stamp, and empties the stamp variables to turn off
                screenshots.append(screen.copy())
                lock = False#enable collision
                usingstamp = ""
                wordstamp = ""

            mouse.set_visible(True)#turning on mouse visibility
            screen.set_clip(None)#allowing all parts of screen to be edited
        for i in minibacks:
            if i.button.collidepoint(mx,my) and mb[0] == 1:#checking if any mini backgrounds are clicked
                iindex = minibacks.index(i)#getting position in list,as the backgrounds and mini backgrounds lists are related
                newimg = backs[iindex]
                newimg = transform.scale(newimg,(canvas.width,canvas.height))#blitting onto the canvas with exact canvas dimensions
                screen.blit(newimg,(canvas.left,canvas.top))
                backgroundcol = 0#setting the solid background color to 0 (None)
        if mb[0] == 1:
            if wordtool == "eyedropper": #checks if the mouse is pressed and the tool selected is the eyedropper 
                if paletterect.collidepoint(mx,my): #checks if the mouse is on the palette
                    col = screen.get_at((mx,my)) #take the color of the pixel the mouse is on, stores it in variable col
            elif wordtool == "backgroundfill":
                if paletterect.collidepoint(mx,my):#will check if tool is backgroundfill,and if clicked on palette
                    backgroundcol = screen.get_at((mx,my))#get color
                    draw.rect(screen,screen.get_at((mx,my)),canvas)#filling color on canvas
            elif wordtool == "pause":
                mixer.music.pause()#pauses music if pause button is hit
            elif wordtool == "unpause":
                mixer.music.unpause()#resumes music if resume button is hit
                
            elif wordtool == "background" and mmode8 == "up":#opening image icon
               try:
                   fname = askopenfilename(filetypes=(("JPG Image","*.jpg*"),
                                                 ("PNG Image","*.png*") ))#getting file name,with jpg and png files accepted
                   
                   newimg = image.load("%s" % fname)#loading image
                   newimgrect = newimg.get_rect()#getting rectangle dimensions of image
                   mmode8 = "down"#enable release
                   screenshot = screen.copy()#take a screenshot
                       
                   if newimgrect.width >= 800 or newimgrect.height >= 500:#checking if image is too big for cavnas
                       newimg = transform.scale(newimg,(800,500))#make image a background
                       screen.blit(newimg,(25,25))
                       mmode8 = "up"#enable click
                       backgroundcol = 0
                   
               except:
                   pass 
               wordtool = ""#setting tool to none
               usingtool = ""
            elif wordtool == "save":#saving tool clicked
                try:
                    fname = asksaveasfilename(defaultextension=".png")#getting file name
                    if fname != "":
                        image.save(screen.subsurface(canvas),fname)#saving file if a name was entered
                    fname = ""#setting the file name to "", or None
                except:
                    pass
                
        if newimg != "":#checking if the image opened was small enough to fit as an image
            if canvas.collidepoint(mx,my) and mmode8 == "down":#moment of release
                screen.blit(screenshot,(0,0))#blitting screenshot
                screen.blit(newimg,(mx-(newimgrect.width)//2,my-(newimgrect.height)//2))#blitting image so center is mouse position
                if evt.type == MOUSEBUTTONDOWN and evt.button == 1:#checking for left click
                    newimg = ""#setting new image to none
                    mmode8 = "up"#enable click
        if wordtool == "shuffle":#checks if shuffle tool is clicked
            shuffle(tracks) #will shuffle the tracks (why i named the pic shuffl and not shuffle)
            songi = 0#set index to 0
            mixer.music.load("MP3 Files/%s"%tracks[0])#load first song
            mixer.music.play()#play music
            wordtool = ""#set wordtool and usingtool to none to avoid reshuffling on accident
            usingtool = ""
                
        
        if mb[0] == 1 and canvas.collidepoint(mx,my): #checking if the mouse is pressed while you are on the canvas
            screen.set_clip(canvas) #only lets the canvas be edited
            dx = mx-omx #distance from the old mx to mx
            dy = my-omy #distance from the old my to my
            dist = int(sqrt(dx**2+dy**2)) #finding the distasnce from (omx,omy) to (mx,my)
            
            if wordtool == "pencil": #checks if the tool is pencil
                draw.line(screen,col,(omx,omy),(mx,my),pencilr) #draws a line from (omx,omy) to (mx,my)
            elif wordtool == "eraser": #checks if the tool is eraser
                if backgroundcol != 0:#checks for solid background
                    for i in range(1,dist+1):
                        draw.circle(screen,backgroundcol,(int(omx+i*dx/dist),int(omy+i*dy/dist)),eraserr)#drawing a circle for an eraser each closer to new spot, with the color of background
                else:
                    for i in range(1,dist+1):
                        try:
                            screen.blit(newimg.subsurface(int(omx+i*dx/dist)-eraserr//2-25,int(omy+i*dy/dist)-eraserr//2-25,eraserr,eraserr),(int(omx+i*dx/dist),int(omy+i*dy/dist)))#blitting the portion of the background back on as an eraser 
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
                draw.line(screen,col,(sx,sy),(mx,my),liner) #draws the line, from the point the mouse was on when pressed ((sx,sy))
            elif wordtool == "rectangle": #checks if the tool is a rectangle
                if wordfiller == "fill":
                    screen.blit(screenshot2,(0,0)) #places the screenshot on
                    draw.rect(screen,col,(sx,sy,mx-sx,my-sy)) #draws a rectangle with the top left corner of the old position of the cursor, and the opposite corner at the new position of the cursor
                elif wordfiller == "border":#checks if the rectangle is unfilled
                    screen.blit(screenshot,(0,0))#blit screenshot
                    draw.rect(screen,col,(sx,sy,mx-sx,my-sy),rectr)#drawing rectangle
                    c1 = min(mx,sx)
                    c2 = min(my,sy)
                    c3 = max(mx,sx)
                    c4 = max(my,sy)
                    #drawing squares of length rectr in the four corners to fill in
                    draw.rect(screen,col,(c1-(rectr-1)//2,c2-(rectr-1)//2,rectr,rectr))
                    draw.rect(screen,col,(c1-(rectr-1)//2,c4-(rectr+1)//2,rectr,rectr))
                    draw.rect(screen,col,(c3-(rectr+1)//2,c2-(rectr-1)//2,rectr,rectr))
                    draw.rect(screen,col,(c3-(rectr+1)//2,c4-(rectr+1)//2,rectr,rectr))
            elif wordtool == "trash":#checks for trash tool
                backgroundcol = WHITE#background color as white
                draw.rect(screen,backgroundcol,canvas)#making canvas white
            elif wordtool == "calligraphy":#check for calligraphy tool
                for i in range(1,dist+1):
                    #getting distances (i/dist) of the way
                    dotx = int(omx+i*dx/dist)
                    doty = int(omy+i*dy/dist)
                    draw.rect(screen,col,(dotx-(callir//2),doty-callir,callir,callir*2))#drawing a rectangle on a point closer and closer to the new mouse position (1 to dist)
            elif wordtool == "highlighter":#check for highlighter tool
                marker = Surface((hir,hir),SRCALPHA)#setting a transparent surface
                draw.circle(marker,(col[0],col[1],col[2],10),(hir//2,hir//2),(hir//2))#drawing circle onto surface
                for i in range(1,dist+1,2):
                    screen.blit(marker,(int(omx+i*dx/dist),int(omy+i*dy/dist)))#blitting that circle every time along the way to new mouse position
            elif wordtool == "floodfill" and backgroundcol != 0 and canvas.collidepoint(mx,my):#floodfill tool, and checking for a solid background on the canvas
                rc=screen.get_at((mx,my))#gets the colour of the pixel where the user right-clicked 
                spots = [(mx,my)] #list of points
                while len(spots)>0:#keeps going until spots is empty
                    newSpots =[]
                    for fx,fy in spots:#for a point on the spots list
                        if 0<fx<825 and 0<fy<525 and screen.get_at((fx,fy))==rc:#checks to see if the point is on the canvas,and comparing the color
                            screen.set_at((fx,fy),col)#setting color
                            newSpots += [(fx+1,fy),(fx-1,fy),(fx,fy-1),(fx,fy+1)]#mark the 4 points for filling (right, left, up and down from the current point)
                    spots = newSpots#setting old list to new lost
                    if len(newSpots) > 8000:#will break before the program crashes
                        break
            
            screen.set_clip(None)#allowing editing everywhere

        if canvas.collidepoint(mx,my):#checks if mouse is on canvas
            screen.set_clip(canvas)#editing only on canvas
            if wordtool == "ellipse": #checks if the tool is an ellipse
                if mmode4 == "up" and mb[0] == 1:#moment of click
                    screenshot = screen.copy()#get screenshot
                    mmode4 = "down"#enable release
                    sx,sy = mouse.get_pos()#get mouse position of moment of click
                if mmode4 == "down" and mb[0] == 1:#still holding down
                    mx,my = mouse.get_pos()#get mouse position of still holding down
                    screen.blit(screenshot,(0,0))#blitting the screenshot
                    draw.rect(screen,col,(sx,sy,mx-sx,my-sy),1)#drawing a rectangle of dimensions of ellipse
                if mmode4 == "down" and mb[0] == 0:#moment of release
                    mmode4 = "up"#enable click
                    screen.blit(screenshot,(0,0))#blit screenshot for last time
                    try:
                        if wordfiller == "fill":
                            draw.ellipse(screen,col,(min(mx,sx),min(my,sy),abs(mx-sx),abs(my-sy)))#draw ellipse fully if selection is filled
                        elif wordfiller == "border":
                            #draw ellipse unfilled from starting point and the 4 points around it to avoid missing pixels
                            draw.ellipse(screen,col,(min(mx,sx),min(my,sy),abs(mx-sx),abs(my-sy)),ellipser)
                            draw.ellipse(screen,col,(min(mx,sx)-1,min(my,sy),abs(mx-sx),abs(my-sy)),ellipser)
                            draw.ellipse(screen,col,(min(mx,sx)+1,min(my,sy),abs(mx-sx),abs(my-sy)),ellipser)
                            draw.ellipse(screen,col,(min(mx,sx),min(my,sy)-1,abs(mx-sx),abs(my-sy)),ellipser)
                            draw.ellipse(screen,col,(min(mx,sx),min(my,sy)+1,abs(mx-sx),abs(my-sy)),ellipser)
                        screenshots.append(screen.copy())#appending screenshot to moves list
                    except:
                        pass
                    
            elif wordtool == "polygon":#checks if tool is polygon
                if mmode2 == "up" and mb[0] == 1:#moment of click
                    screenshot = screen.copy()#get screenshot
                    mmode2 = "down"#enable release
                if mmode2 == "down" and mb[0] == 0:#moment of release
                    mmode2 = "up"#enable click
                    tx,ty = mouse.get_pos()#position of vertex
                    draw.rect(screen,col,(tx,ty,1,1))#drawing a pixel size vertex
                    if len(vertices) > 0:#checks to see if the first point is inside
                        draw.line(screen,col,(vertices[-2],vertices[-1]),(tx,ty))#draws a line from the 2nd last point to the first last point
                    if canvas.collidepoint(tx,ty):#checks to see if in canvas
                        #appending new vertex
                        vertices.append(tx)
                        vertices.append(ty)
                if mb[2] == 1:#right click to renclose
                    try:
                        draw.line(screen,col,(tx,ty),(vertices[0],vertices[1]))#drawing from last point to first point
                        vertices = []#emptying vertices list
                    except IndexError:
                        pass
            elif wordtool == "undo" and lock == False:#checking if tool is undo and collision is allowed
                if mmode2 == "up" and mb[0] == 1:#moment of click
                    mmode2 = "down"#enable release
                if mmode2 == "down" and mb[0] == 0:#moment of release
                    mmode2 = "up"#enable click
                    draw.rect(screen,WHITE,canvas)#drawing a rectangle on canvass
                    try: 
                        screen.blit(screenshots[count],(0,0))#drawing a rectangle on canvas
                    except IndexError:#avoiding being on the -1st screen
                        pass
                    count -= 1#decreasing count (the screenshot number) by 1
                    
            elif wordtool == "redo" and lock == False:#checking if tool is redo and collision is allowed
                if mmode3 == "up" and mb[0] == 1:#moment of click
                    mmode3 = "down"#enable release
                if mmode3 == "down" and mb[0] == 0:#moment of release
                    mmode3 = "up"#enable click
                    if firstredo:#checks to see if this is the first redo click in a row
                        count += 1#increment count by 1
                        firstredo = False#making the firstredo false, as it was just done  
                    if count < -1:#checks if the screen is not the last on the screenshots list
                        count += 1#increases count by 1
                    elif count > -1:#checks if the screen is "above" the last item in the list,which is why we decrement by 1
                        count = -1
                    draw.rect(screen,WHITE,canvas)#drawing blank rectangle over canvas
                    try:
                        screen.blit(screenshots[count],(0,0))#blitting the new screen on top
                    except IndexError:#avoiding going from the 0th to 1st (the second!) item
                        pass
                    
                
            screen.set_clip(None) #this will allow editing all over the pygame window now
        if mb[0] == 1 and mmode9 == "up" and voldown.button.collidepoint(mx,my):#if volume down is clicked on
            mmode9 = "down"#enable release
        if mb[0] == 0 and mmode9 == "down" and voldown.button.collidepoint(mx,my):#if volume up is released
            volume = mixer.music.get_volume()#get volume
            mmode9 = "up"#enable click
            if volume > 0:
                mixer.music.set_volume(volume-0.01)#decrement if volume > 0
                screen.blit(launch.subsurface(1160,110,70,30),(1160,110))#blitting part of background to put new volume
        if mb[0] == 1 and mmode9 == "up" and volup.button.collidepoint(mx,my):#if volume up is clicked on
            mmode9 = "down"#enable release
        if mb[0] == 0 and mmode9 == "down" and volup.button.collidepoint(mx,my):#if volume down is released
            volume = mixer.music.get_volume()#get volume
            mmode9 = "up"#enable click
            if volume < 1:
                mixer.music.set_volume(volume+0.01)#increment if volume < 1
                screen.blit(launch.subsurface(1160,110,70,30),(1160,110))#blitting part of background to put new volume

        screen.blit(t2font.render("Volume:  %i"%(int(volume*100)),True,WHITE),(1100,110))#blit volume
                
        ###BLITTING TEXT FOR INSTRUCTIONS
        if prevwordtool != wordtool or prevwordfiller != wordfiller:
            screen.blit(image.load("Images/scroll.png"),(500+450,550-150))
        if wordtool == "pencil":
            screen.blit(tfont.render("Tool: Pencil",True,BLACK),(570+450,575-150))
            screen.blit(t2font.render("Click on the canvas and move the cursor",True,BLACK),(585+450,620-150))
            screen.blit(t2font.render("to draw.",True,BLACK),(585+450,645-150))
            if prevpencilr != pencilr:
                screen.blit(image.load("Images/scroll.png").subsurface(710-500,620-550,40,30),(1160,500))
            screen.blit(t2font.render("Pencil Radius: %i"%pencilr,True,BLACK),(585+450,660-150))
        elif wordtool == "eraser":
            screen.blit(tfont.render("Tool: Eraser",True,BLACK),(570+450,575-150))
            if preveraserr != eraserr:
                screen.blit(image.load("Images/scroll.png").subsurface(710-500,620-550,40,30),(710+450,620-150))
            screen.blit(t2font.render("Eraser Radius:  %i" % eraserr,True,BLACK),(585+450,620-150))
        elif wordtool == "brush":
            screen.blit(tfont.render("Tool: Brush",True,BLACK),(570+450,575-150))
            if prevbrushr != brushr:
                screen.blit(image.load("Images/scroll.png").subsurface(710-500,620-550,40,30),(710+450,620-150)) 
            screen.blit(t2font.render("Brush Radius: %i" % brushr,True,BLACK),(585+450,620-150))
        elif wordtool == "spray":
            screen.blit(tfont.render("Tool: Spray",True,BLACK),(570+450,575-150))
            if prevsprayr != sprayr:
                screen.blit(image.load("Images/scroll.png").subsurface(710-500,620-550,60,30),(710+450,620-150)) 
            screen.blit(t2font.render("Spray Radius:  %i" % sprayr,True,BLACK),(585+450,620-150))
        elif wordtool == "line":
            screen.blit(tfont.render("Tool: Line",True,BLACK),(570+450,575-150))
            if prevliner != liner:
                screen.blit(image.load("Images/scroll.png").subsurface(710-500,620-550,30,30),(1270,420)) 
            screen.blit(t2font.render("Thickness: %i"%liner,True,BLACK),(570+610,425))
            screen.blit(t2font.render("1. Press and hold on starting point.",True,BLACK),(585+450,620-150))
            screen.blit(t2font.render("2. Move the cursor and let go where you",True,BLACK),(585+450,645-150))
            screen.blit(t2font.render("    want to end.",True,BLACK),(585+450,665-150))
        elif wordtool == "eyedropper":
            screen.blit(tfont.render("Tool: Eyedropper",True,BLACK),(570+450,575-150))
            screen.blit(t2font.render("Select a colour from the colour palette.",True,BLACK),(585+450,620-150))
        elif wordtool == "rectangle":
            screen.blit(tfont.render("Tool: Rectangle",True,BLACK),(570+450,575-150))
            screen.blit(t2font.render("1. Press and hold on starting point.",True,BLACK),(585+450,620-150))
            screen.blit(t2font.render("2. Release on the opposite corner.",True,BLACK),(585+450,640-150))
            if wordfiller == "border":
                if prevrectr != rectr:
                    screen.blit(image.load("Images/scroll.png").subsurface(725-500,600-550,35,30),(730+450,660-150)) 
                screen.blit(t2font.render("Rectangle width:  %i" % rectr,True,BLACK),(585+450,660-150))
        elif wordtool == "ellipse":
            screen.blit(tfont.render("Tool: Ellipse",True,BLACK),(570+450,575-150))
            screen.blit(t2font.render("1. Press and hold on a corner.",True,BLACK),(585+450,620-150))
            screen.blit(t2font.render("2. Release on the opposite corner.",True,BLACK),(585+450,640-150))
            if wordfiller == "border":
                if prevellipser != ellipser:
                    screen.blit(image.load("Images/scroll.png").subsurface(725-500,600-550,35,30),(730+450,660-150)) 
                screen.blit(t2font.render("Ellipse thickness:  %i" % ellipser,True,BLACK),(585+450,660-150))
        elif wordtool == "calligraphy":
            screen.blit(tfont.render("Tool: Calligraphy",True,BLACK),(570+450,575-150))
            screen.blit(t2font.render("Click on the canvas and move the cursor to draw",True,BLACK),(565+450,620-150))
            if prevcallir != callir:
                screen.blit(image.load("Images/scroll.png").subsurface(710-500,620-550,35,30),(760+450,640-150)) 
            screen.blit(t2font.render("Calligraphy Thickness:  %i" % callir,True,BLACK),(565+450,640-150))
        elif wordtool == "undo":
            screen.blit(tfont.render("Tool: Undo",True,BLACK),(570+450,575-150))
            screen.blit(t2font.render("Click on the canvas to undo",True,BLACK),(585+450,620-150))
        elif wordtool == "redo":
            screen.blit(tfont.render("Tool: Redo",True,BLACK),(570+450,575-150))
            screen.blit(t2font.render("Click on the canvas to redo",True,BLACK),(585+450,620-150))
        elif wordtool == "backgroundfill":
            screen.blit(tfont.render("Tool: Background Fill",True,BLACK),(570+450,575-150))
            screen.blit(t2font.render("Choose a color by clicking on the palette.",True,BLACK),(585+450,620-150))
        elif wordtool == "polygon":
            screen.blit(tfont.render("Tool: Polygon",True,BLACK),(570+450,575-150))
            screen.blit(t2font.render("1. Left click to select first vertex.",True,BLACK),(585+450,620-150))
            screen.blit(t2font.render("2. Left click to select next vertex.",True,BLACK),(585+450,640-150))
            screen.blit(t2font.render("3. Right click to enclose shape",True,BLACK),(585+450,660-150))
        elif wordtool == "trash":
            screen.blit(tfont.render("Tool: Trash",True,BLACK),(570+450,575-150))
            screen.blit(t2font.render("Click on the canvas to clear the screen.",True,BLACK),(585+450,620-150))
        elif wordtool == "highlighter":
            screen.blit(tfont.render("Tool: Highlighter",True,BLACK),(570+450,575-150))
            if prevhir != hir:
                screen.blit(image.load("Images/scroll.png").subsurface(710-500,620-550,40,30),(755+450,620-150))
            screen.blit(t2font.render("Highlighter Radius:  %i" % hir,True,BLACK),(585+450,620-150))
        elif wordtool == "floodfill":
            screen.blit(tfont.render("Tool: Floodfill",True,BLACK),(570+450,575-150))
            screen.blit(t2font.render("Click on an area to enclose",True,BLACK),(575+450,620-150))
            screen.blit(t2font.render("Works only on solid backgrounds",True,BLACK),(575+450,640-150))
        elif wordstamp != "":
            screen.blit(tfont.render("Tool: Stamp",True,BLACK),(570+450,575-150))
            screen.blit(t2font.render("Left click to place, right click to place & stop",True,BLACK),(565+450,620-150))

        #checks to see if mouse position changed, and will cover the old one with the background if so
        if omx != mx or omy != my:
            screen.blit(launch.subsurface(1230,50,100,30),(1230,50))
        #blitting mouse position
        screen.blit(t2font.render("Mouse position:  %s,%s" % (mx,my),True,WHITE),(1100,50))
        #checks to see if color of tool changed, and will cover the old one with background if so
        if prevcol != col:
            screen.blit(launch.subsurface(1145,80,125,30),(1145,80))
        #blitting color
        screen.blit(t2font.render("Color: %i,%i,%i"%(col[0],col[1],col[2]),True,WHITE),(1100,80))
            
            
            
            
        
        #setting all previous tool radii to current tool radii, as we are at the end of the loop
        prevwordtool = wordtool
        prevpencilr = pencilr
        prevliner = liner
        preveraserr = eraserr
        prevbrushr = brushr
        prevsprayr = sprayr
        prevrectr = rectr
        prevellipser = ellipser
        prevcallir = callir
        prevhir = hir
        prevwordfiller = wordfiller

        
        prevcol = col #setting old color to new one
        
        
        omx = mx #setting omx to the mx value, as mx will get a new value
        omy = my #setting omy to the my value, as my will get a new value
        
        display.flip() #will now show all changes

del tfont
del t2font
quit() #quit the window


