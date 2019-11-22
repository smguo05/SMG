# write-html-2-windows.py

import webbrowser

f = open('unimario.html', 'w')

message = """<html>
<head>
  <title>Uni Mario Project</title>
</head>
<body>
  <center><h1>Uni Mario</h1></center>
  <a href="Uni Mario(A).py">Uni Mario</a>
  <center><p>Our main objective throughout this project was to create a Uni Mario game, which we would code and create graphics for. Arya and Sarah created the code, and Katya did the graphics. This is the result.</p></center> 
  <center><img src="https://cdn.pixabay.com/photo/2017/08/28/16/17/super-mario-2690254_960_720.jpg" alt="Mario in a Tube" width="900" height="500"></center>
</body>
</html>"""

f.write(message)
f.close()

import pygame
import sys
import pygame.sprite as sprite
import time
import random

pygame.init()

pygame.display.set_caption("Uni Mario")

p_x = 150
p_y = 350
width = 40
height = 60
vel = 5

left=False
right=False
walk_count = 0
walkRight = []
walkLeft = []

myfont = pygame.font.SysFont("monospace", 25)
screen_over = pygame.font.SysFont("monospace", 100)
hitcount = 3
score=0

clock = pygame.time.Clock()
FPS = 30

background_image = pygame.image.load('Sprites/bg2.png')
background_size = background_image.get_size()
background_rect = background_image.get_rect()
                          
sw = 837
sh = 464
gw = 837
win = pygame.display.set_mode((sw, sh))
w,h = background_size

t_x = sw
t_y = 350
t_v = random.randint(15,30) #part of the random library

g_x = gw
bg_x1 = 0
bg_y1 = 0

bg_x2 = w
bg_y2 = 0

d2 = 9999
count = 9999

def load_img(file_name): #loads the image, makes the pure white background transparent
    img = pygame.image.load(file_name).convert()
    img.set_colorkey((255,255,255))

    return img

for i in range(1,7):
    walkLeft.append( load_img("Sprites/L" + str(i) + ".png" ) ) #loads in lists of images for Mario animation
    walkRight.append( load_img("Sprites/R" + str(i) + ".png") )
    
player_image = walkRight[0]

Goomba = [pygame.image.load('Sprites/G1.png'), pygame.image.load('Sprites/G2.png')]#1
index=0
Tube = pygame.image.load('Sprites/T1.png')
#Castle = pygame.image.load('Sprites/castle.png')

d2 = (t_x - 50 - p_x)**2 + (t_y - p_y)**2 #represents the distance between mario and goomba
d3 = (g_x + 250 - p_x)**2 + (t_y - p_y)**2

if d2 > 2500 and d3 > 1750:
    yes = True

#if yes == True:
pygame.mixer.music.load('Music/Bros-Theme-Song.mp3') #music
pygame.mixer.music.play(-1)
#if yes == False:
 #   pygame.mixer.music.load('Music/Over.mp3')
  #  pygame.mixer.music.play(-1)
   # pygame.mixer.music.stop
    

isJump = False
jumpCount = 10

left_idx=0
right_idx=0

run = True #main loop
while run:    
    clock.tick(FPS)    
    pygame.time.delay(50)
    
    win.blit(background_image,(sw, sh)) #makes a scrolling background 
    pygame.display.update()
    
    bg_x2 -= 8
    bg_x1 -= 8
    
    if bg_x1 < sw - 2*w:
       bg_x1 = sw
    if bg_x2 < sw - 2*w:
          bg_x2 = sw

    t_x -= t_v #controls goomba movement
    
    if t_x < 0:
        t_x = sw
        if t_v < 1000:
            t_v += 2
            
    if t_v >= 25 and t_v <= 30:
        t_v = random.randint(15,30)

    g_x -= 8 #controls tube movement
    
    if g_x < -600:
        g_x = gw
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
                                             
    keys = pygame.key.get_pressed()
    if run == True: #jumping animation
        if not isJump:
            player_image = walkRight[right_idx]
            right_idx += 1
            if right_idx >= len(walkRight):
                right_idx=0
        
    if not(isJump):      
        if keys[pygame.K_UP]:
            isJump = True
        if keys[pygame.K_SPACE]:
            isJump = True

    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            p_y -= (jumpCount ** 2)* 0.45 * neg
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10

    if bg_x1 > -w:        
        win.blit(background_image,(bg_x1,bg_y1))
    if bg_x2 > -w:
        win.blit(background_image,(bg_x2,bg_y2))
    win.blit(player_image, (p_x,p_y))
    #if score < 90:
    win.blit(Tube, (g_x + 250, t_y - 45)) 
    #elif score >= 90:
        #win.blit(Castle, (g_x + 250, t_y - 100))
    if run==True:
        win.blit(Goomba[index], (t_x - 50, t_y))
        index += 1
    if index >= len(Goomba):
        index=0

    label3 = myfont.render("Watch out for the",1, (0, 0, 0))
    win.blit(label3, (300, 10))

    label4= myfont.render("Goombas and Tubes!", 1, (0 , 0, 0))
    win.blit(label4, (300, 60))

    label5 = myfont.render("Score: "+ str(score), 1, (0, 0, 0))
    win.blit(label5, ((sw-500), 420))

    pygame.display.update() 

    d2 = (t_x - 50 - p_x)**2 + (t_y - p_y)**2 #represents the distance between Mario and Goomba
    d3 = (g_x + 250 - p_x)**2 + (t_y - p_y)**2 #represents the distance between Mario and the tube
    
    if count < 9999: count += 1
    
    if d3 < 1000:
        label2 = screen_over.render("GAME OVER", 1, (255, 0, 0))
        win.blit(label2, (165, 200))
        pygame.display.update()
        time.sleep(2)
        run = False
        
    elif d2 < 2500 and count > 10: 
        label2 = screen_over.render("GAME OVER", 1, (255, 0, 0))
        win.blit(label2, (165, 200))
        pygame.display.update()
        time.sleep(2)
        run = False
        hitcount -= 1
        count = 0
     
    else:
        score += 1/10
        
    if score >= 100: 
        label6 = screen_over.render("VICTORY!", 1, (0, 0, 255))
        win.blit(label6, (200,200))
        pygame.display.update()
        time.sleep(3)
        run = False

pygame.quit()



webbrowser.open_new_tab('unimario.html')
