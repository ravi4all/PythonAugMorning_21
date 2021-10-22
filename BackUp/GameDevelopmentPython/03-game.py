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

    for i in range(8):
        for j in range(i+1):
            pygame.draw.rect(screen, white, [50*j + 2, 50*i + 2, 50, 50])

    pygame.display.flip()

