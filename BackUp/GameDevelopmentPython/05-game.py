import pygame
import random

pygame.init()

screenWidth = 1000
screenHeight = 500
size = screenWidth, screenHeight
screen = pygame.display.set_mode(size)

frogImg = pygame.image.load('frog.png')
frogWidth = frogImg.get_width()
frogHeight = frogImg.get_height()

frogX = random.randint(1, screenWidth - frogWidth)
frogY = random.randint(1, screenHeight - frogHeight)

red = 255,0,0
white = 255,255,255

x, y = 0, 0
w, h = 50, 50

moveX = 0
moveY = 0
speed = 0.3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   # quit pygame
            quit()          # quit python

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveX = speed
                moveY = 0
            elif event.key == pygame.K_LEFT:
                moveX = -speed
                moveY = 0
            elif event.key == pygame.K_DOWN:
                moveY = speed
                moveX = 0
            elif event.key == pygame.K_UP:
                moveY = -speed
                moveX = 0
        # else:
        #     moveX = 0
        #     moveY = 0

    screen.fill(red)
    screen.blit(frogImg, (frogX, frogY))

    frogRect = pygame.Rect(frogX, frogY, frogWidth, frogHeight)
    snakeRect = pygame.draw.rect(screen, white, [x, y, w, h])
    x += moveX
    y += moveY

    if x > screenWidth:
        # moveX = -0.3
        x = -w
    elif x < -50:
        x = screenWidth

    if y > screenHeight:
        # moveY = -0.3
        y = -h
    elif y < -50:
        # moveY = 0.3
        y = screenHeight

    if frogRect.colliderect(snakeRect):
        frogX = random.randint(1, screenWidth - frogWidth)
        frogY = random.randint(1, screenHeight - frogHeight)

    pygame.display.flip()

