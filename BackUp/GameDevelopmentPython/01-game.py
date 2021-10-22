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
    pygame.display.flip()

