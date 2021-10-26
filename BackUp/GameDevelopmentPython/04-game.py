import pygame

pygame.init()

screenWidth = 1000
screenHeight = 500
size = screenWidth, screenHeight
screen = pygame.display.set_mode(size)

red = 255,0,0
white = 255,255,255

x, y = 0, 0
w, h = 50, 50

moveX = 0.3
moveY = 0.3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   # quit pygame
            quit()          # quit python

    screen.fill(red)

    pygame.draw.rect(screen, white, [x, y, w, h])
    x += moveX
    y += moveY

    if x > screenWidth - w:
        moveX = -0.3
    elif x < 0:
        moveX = 0.3

    if y > screenHeight - h:
        moveY = -0.3
    elif y < 0:
        moveY = 0.3

    pygame.display.flip()

