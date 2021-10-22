import pygame

pygame.init()

screenWidth = 1000
screenHeight = 500
size = screenWidth, screenHeight
screen = pygame.display.set_mode(size)

red = 255,0,0
white = 255,255,255

screen.fill(red)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   # quit pygame
            quit()          # quit python

    pygame.draw.rect(screen, white, [10, 10, 50, 50])
    pygame.draw.rect(screen, white, [100, 100, 150, 150])

    pygame.draw.circle(screen, white, [300, 100], 100)

    pygame.display.flip()

