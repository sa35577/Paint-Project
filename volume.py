#graphicsTemplate
from pygame import *
size=width,height=800,600
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
screen.fill(WHITE)
running=True
init()
mixer.Sound("MP3 Files/Beyblade Burst Super Z Opening.mp3") #loads the song 
mixer.music.play() #plays the music
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type == MOUSEBUTTONDOWN:
            screenshot = screen.copy()

    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()

    omx,omy = mx,my
    display.flip() 

quit()

