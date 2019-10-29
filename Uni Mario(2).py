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
walkELeft = []


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

bg_x1 = 0
bg_y1 = 0

bg_x2 = w
bg_y2 = 0

d2 = 9999

def load_img(file_name): # loads the image, makes the pure white background transparent
    img = pygame.image.load(file_name).convert()
    img.set_colorkey((255,255,255))

    return img

for i in range(1,7):
    walkLeft.append( load_img("Sprites/L" + str(i) + ".png" ) ) #loads in lists of images
    walkRight.append( load_img("Sprites/R" + str(i) + ".png") ) 
player_image = walkRight[0]

#for i2 in range(1,4):
#    walkELeft.append( load_img("Sprites/G" + str(i2) + ".png") )
#enemy_image = walkELeft[0]

enemy_image = pygame.image.load('Sprites/G1.png')

pygame.mixer.music.load('Music/bensound-summer.mp3')
pygame.mixer.music.play(-1)

isJump = False
jumpCount = 10

left_idx=0
right_idx=0

run = True #main loop
while run:
    pygame.time.delay(50)

    bg_x2 -= 5
    bg_x1 -= 5
    if bg_x1 < sw - 2*w:
       bg_x1 = sw
    if bg_x2 < sw - 2*w:
       bg_x2 = sw

    g_x -=20
    if g_x < 0:
        g_x = sw

   
          
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
                                             
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and p_x > vel: 
        p_x -= vel
        if not isJump:
            player_image = walkLeft[left_idx]
            left_idx += 1
            if left_idx >= len(walkLeft):
                left_idx=0
        
    if keys[pygame.K_RIGHT] and p_x < sw - width - vel:
        p_x += vel
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
            p_y -= (jumpCount ** 2)* 0.4 * neg
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10

    if bg_x1 > -w:        
        win.blit(background_image,(bg_x1,bg_y1))
    if bg_x2 > -w:
        win.blit(background_image,(bg_x2,bg_y2))
    win.blit(player_image, (p_x,p_y))
    win.blit(enemy_image, (g_x, g_y))

    label = myfont.render("Hit Count = "+ str(hit_count), 1, (0, 0, 0)) #NEED TO FIX
    win.blit(label, ((sw-250), 50))

  
    pygame.display.update()

   
    d2 = (g_x - p_x)**2 + (g_y - p_y)**2
    if d2 < 200:
         hit_count +=1
         if hit_count > 5:
             label2 = screen_over.render("Game Over", 1, (255, 0, 0))
             win.blit(label2, (150, 200))
             pygame.display.update()
             time.sleep(3)
             run= False

    

    theClock.tick(50)

        




pygame.quit()
