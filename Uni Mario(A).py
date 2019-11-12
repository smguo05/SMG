import pygame
import sys
import pygame.sprite as sprite
import time
import random
pygame.init()

pygame.display.set_caption("Uni Mario")


m_x = 150
m_y = 350
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

def load_img(file_name): # loads the image, makes the pure white background transparent
    img = pygame.image.load(file_name).convert()
    img.set_colorkey((255,255,255))

    return img

for i in range(1,7):
    walkLeft.append( load_img("Sprites/L" + str(i) + ".png" ) ) #loads in lists of images
    walkRight.append( load_img("Sprites/R" + str(i) + ".png") )
    

player_image = walkRight[0]

#slide = [pygame.image.load('Sprites/SL1.png'), pygame.image.load('Sprites/SL1.png')] #sliding images

Goomba = [pygame.image.load('Sprites/G1.png'), pygame.image.load('Sprites/G2.png')]#1
index=0
Tube = pygame.image.load('Sprites/T4.png')

pygame.mixer.music.load('Music/Bros-Theme-Song.mp3')
pygame.mixer.music.play(-1)

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

    t_x -= t_v
    if t_x < 0:
        t_x = sw
        if t_v < 1000:
            t_v += 2
    if t_v >= 25 and t_v <= 30:
        t_v = random.randint(15,30)

    g_x -= 8
    if g_x < -500:
        g_x = gw
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
                                             
    keys = pygame.key.get_pressed()
    #if keys[pygame.K_LEFT] and m_x > vel: 
       # m_x -= vel
        #if not isJump:
         #   player_image = walkLeft[left_idx]
          #  left_idx += 1
           # if left_idx >= len(walkLeft):
                #left_idx=0
        
    #if keys[pygame.K_RIGHT] and m_x < sw - width - vel:
       # m_x += vel
        #if not isJump:
         #   player_image = walkRight[right_idx]
          #  right_idx += 1
           # if right_idx >= len(walkRight):
            #    right_idx=0
    if run == True:
        if not isJump:
            player_image = walkRight[right_idx]
            right_idx += 1
            if right_idx >= len(walkRight):
                right_idx=0
    #if not(isJump): #slides
     #   if keys[pygame.K_DOWN]:
      #      player_image = slide[index]
       #     index += 1
        #    if index >= len(slide):
         #       index=0
            
            
        
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
            m_y -= (jumpCount ** 2)* 0.45 * neg
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10

    if bg_x1 > -w:        
        win.blit(background_image,(bg_x1,bg_y1))
    if bg_x2 > -w:
        win.blit(background_image,(bg_x2,bg_y2))
    win.blit(player_image, (m_x,m_y))
    win.blit(Tube, (g_x + 500, t_y-45))
    if run==True:
        win.blit(Goomba[index], (t_x - 50, t_y))#2
        index += 1
    if index >= len(Goomba):
        index=0
    
    #label = myfont.render("Lives = "+ str(hitcount), 1, (0, 0, 0))
    #win.blit(label, ((sw-200), 420))

    label3 = myfont.render("Watch out for the",1, (0, 0, 0))
    win.blit(label3, (300, 10))

    label4= myfont.render("Goombas and Tubes!", 1, (0 , 0, 0))
    win.blit(label4, (300, 60))

    label5 = myfont.render("Score: "+ str(score), 1, (0, 0, 0))
    win.blit(label5, ((sw-200), 420))

  
    pygame.display.update() 

   
    d2 = (t_x - 50 - m_x)**2 + (t_y - m_y)**2 #represents the distance between mario and goomba
    d3 = (g_x + 500 - m_x)**2 + (t_y - m_y)**2
    if count < 9999: count += 1
    if d3 < 1750:
        label2 = screen_over.render("Game Over", 1, (255, 0, 0))
        win.blit(label2, (165, 200))
        pygame.display.update()
        time.sleep(1)
        run = False
    elif d2 < 2500 and count > 10: #keep it between 142 and 5000, it seems to be a good distance for the hitcount
        label2 = screen_over.render("Game Over", 1, (255, 0, 0))
        win.blit(label2, (165, 200))
        pygame.display.update()
        time.sleep(1)
        run = False
       # hitcount -= 1
        #count = 0
    #if d2 < 142 and player_image==slide[index]:  #when sliding, the hitcount doesn't count
     #   hitcount -= 1
    else:
        score += 1/10
    if hitcount <= 0:
        label2 = screen_over.render("Game Over", 1, (255, 0, 0))
        win.blit(label2, (165, 200))
        pygame.display.update()
        time.sleep(1)
        run = False
    if score >= 100:
        label6 = screen_over.render("WINNER WINNER", 1, (0, 0, 255))
        win.blit(label6, (30,200))
        pygame.display.update()
        time.sleep(2)
        run = False

pygame.quit()
