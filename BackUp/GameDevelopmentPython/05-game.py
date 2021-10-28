import pygame
import random

pygame.init()

screenWidth = 1000
screenHeight = 500
size = screenWidth, screenHeight
screen = pygame.display.set_mode(size)

red = 255,0,0
white = 255,255,255
yellow = 255,255,0

frogImg = pygame.image.load('frog.png')
frogWidth = frogImg.get_width()
frogHeight = frogImg.get_height()

w, h = 50, 50

def homeScreen():
    font = pygame.font.SysFont(None, 100)
    text = font.render("Welcome to the Jungle", True, white)

    font_2 = pygame.font.SysFont(None, 70)
    text_2 = font_2.render("Press SPACE to Start Game", True, white)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # quit pygame
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

        screen.fill(red)
        screen.blit(text, (150, 100))
        screen.blit(text_2, (150, 300))
        pygame.display.update()

def gameOver():
    font = pygame.font.SysFont(None, 200)
    text = font.render("Game Over...", True, yellow)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # quit pygame
                quit()

        screen.blit(text, (100, 100))
        pygame.display.update()

def drawSnake(snakeList):
    for i in range(len(snakeList)):
        pygame.draw.rect(screen, white, [snakeList[i][0],
                                         snakeList[i][1],w,h])

def score(counter):
    font = pygame.font.SysFont(None, 30)
    text = font.render("Score : {}".format(counter), True, yellow)
    screen.blit(text, (100,10))

def game():
    x, y = 0, 0

    moveX = 0
    moveY = 0
    speed = 0.7

    snakeLength = 1
    snakeList = []

    frogX = random.randint(1, screenWidth - frogWidth)
    frogY = random.randint(1, screenHeight - frogHeight)

    FPS = 1000
    clock = pygame.time.Clock()

    counter = 0

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

        score(counter)

        snakeHead = []
        snakeHead.append(x)
        snakeHead.append(y)
        snakeList.append(snakeHead)

        drawSnake(snakeList)

        if len(snakeList) > snakeLength:
            del snakeList[0]

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
            snakeLength += 20
            # FPS += 50
            speed += 0.1
            counter += 1

        for each in snakeList[:-1]:
            if each == snakeList[-1]:
                gameOver()

        pygame.display.flip()
        clock.tick(FPS)

# game()
homeScreen()