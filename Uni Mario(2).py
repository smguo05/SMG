import pygame
pygame.init()

win = pygame.display.set_mode((590, 369))
pygame.display.set_caption("Uni Mario")


x = 100
y = 185
width = 40
height = 60
vel = 5

left=False
right=False
walk_count = 0
walkRight = []
walkLeft = []

def load_img(file_name): # loads the image, makes the pure white background transparent
    img = pygame.image.load(file_name).convert()
    img.set_colorkey((255,255,255))

    return img

for i in range(1,7):
    walkLeft.append( load_img("Sprites/L" + str(i) + ".png" ) ) #loads in lists of images
    walkRight.append( load_img("Sprites/R" + str(i) + ".png") ) 
#walkRight = [pygame.transform.flip(img,True,False) for img in walkLeft] #flips left images to be right

player_image = walkRight[0]
background_image = pygame.image.load("Sprites/bg.jpg").convert()

pygame.mixer.music.load('Music/bensound-summer.mp3')
pygame.mixer.music.play(-1)

isJump = False
jumpCount = 10

left_idx=0
right_idx=0

run = True #main loop
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel
        if not isJump:
            player_image = walkLeft[left_idx]
            left_idx += 1
            if left_idx >= len(walkLeft):
                left_idx=0
        
    if keys[pygame.K_RIGHT] and x < 590 - width - vel:
        x += vel
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
            y -= (jumpCount ** 2)* 0.25 * neg
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10

    win.blit(background_image, [0, 0])
    win.blit(player_image, (x,y))
  
    pygame.display.update()


        




pygame.quit()
