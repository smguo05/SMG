import pygame
import sys
import pygame.sprite as sprite
import time
pygame.init()

pygame.display.set_caption("Uni Mario")


p_x = 100
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
hit_count = 0

theClock = pygame.time.Clock()

background_image = pygame.image.load('Sprites/bg2.png')
background_size = background_image.get_size()
background_rect = background_image.get_rect()
sw = 840
sh = 464
win = pygame.display.set_mode((sw, sh))
w,h = background_size


g_x = sw
g_y = 360
g_v = 15

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

slide = [pygame.image.load('Sprites/S1.png'), pygame.image.load('Sprites/S1.png')] #CHANGE WITH S1 WHEN AVAILABLE!!
enemy_images = [pygame.image.load('Sprites/G1.png'), pygame.image.load('Sprites/G2.png')]

index = 0

pygame.mixer.music.load('Music/bensound-summer.mp3') #runs music on loop
pygame.mixer.music.play(-1)

isJump = False
jumpCount = 10

left_idx=0
right_idx=0

run = True #main loop
while run:
    pygame.time.delay(50)

    bg_x2 -= 5 #scrolling background
    bg_x1 -= 5
    if bg_x1 < sw - 2*w:
       bg_x1 = sw
    if bg_x2 < sw - 2*w:
       bg_x2 = sw

    g_x -= g_v #respawns Goomba every background frame
    if g_x < 0:
        g_x = sw
        if g_v < 100:
            g_v += 3
            
         
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False                                       

    keys = pygame.key.get_pressed()
    if run == True:
        if not isJump:
            player_image = walkRight[right_idx]
            right_idx += 1
            if right_idx >= len(walkRight):
                right_idx=0
                
    if not(isJump): #jumping animation
        if keys[pygame.K_UP]:
            isJump = True
        if keys[pygame.K_SPACE]:
            isJump = True

    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            p_y -= (jumpCount ** 2)* 0.4 * neg
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10

    if not(isJump): #sliding animation
        if keys[pygame.K_DOWN]:
            player_image = slide[index]
            index +=1
            if index >= len(slide):
                index = 0
            

    if bg_x1 > -w:        
        win.blit(background_image,(bg_x1,bg_y1))
    if bg_x2 > -w:
        win.blit(background_image,(bg_x2,bg_y2))
    win.blit(player_image, (p_x,p_y))
    
    if run==True: #animation of Goomba
        win.blit(enemy_images[index], (g_x, g_y))
        pygame.time.delay(20)
        index +=1
    if index >= len(enemy_images):
        index = 0

    label = myfont.render("Hit Count = "+ str(hit_count), 1, (0, 0, 0))
    win.blit(label, ((sw-250), 50))

  
    pygame.display.update()

    if count < 9999: count += 1
    d2 = (g_x - p_x)**2 + (g_y - p_y)**2 #calculates distance between the Mario and Goomba
    if d2 < 5000 and count > 10: #adds only one point per hit
         hit_count +=1
         count = 0
         if hit_count > 5:
             label2 = screen_over.render("Game Over", 1, (255, 0, 0))
             win.blit(label2, (150, 200))
             pygame.display.update()
             time.sleep(3)
             run= False

    

    theClock.tick(50)

        




pygame.quit()
