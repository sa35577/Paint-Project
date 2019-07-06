#drawingtext.py
from pygame import *
from random import *
size=width,height=800,600 #must use at least 1024,768
screen=display.set_mode(size,)

font.init() #initialize everything for font
comicFont = font.SysFont("Comic Sans MS",50)

RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)

#converting the text "Massey" into a picture
                                    #aliased or anti-aliased
txtMasseyPic = comicFont.render("Massey",True,RED)
txtMasseyPic2 = comicFont.render("Massey",True,RED)
screen.blit(txtMasseyPic,(400,300))
screen.blit(txtMasseyPic2, (100,300))


words = ["python","winter","school","summer","programming","hello"]


running=True
while running:
    click = False
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type == MOUSEBUTTONDOWN:
            click = True
            print("hello")
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()
    #if mb[0] == 1: #holding the mouse (keeping it "pressed")
    if click and mb[0] ==1:
      word = choice(words)
      col = (randint(0,255),randint(0,255),randint(0,255))
      txtMasseyPic = comicFont.render(word,True,col)
      screen.blit(txtMasseyPic,(mx,my)) #draw from top left

      w = txtMasseyPic.get_width() #gets the width of the picture (massey text)
      h = txtMasseyPic.get_height() #gets the height of the picture (massey text)
      #print(w,h)
      #print(click)

      screen.blit(txtMasseyPic,(mx-w//2,my-h//2)) #draw from center
                       
    display.flip()
font.quit()
del comicFont

quit()
