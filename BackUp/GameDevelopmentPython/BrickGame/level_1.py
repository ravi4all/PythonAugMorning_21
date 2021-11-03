import pygame

pygame.init()
pygame.mixer.init()

screenWidth = 1000
screenHeight = 500
size = screenWidth, screenHeight
screen = pygame.display.set_mode(size)

red = 255,0,0
white = 255,255,255
blue = 0,0,255
black = 0,0,0

def homeScreen():
    font = pygame.font.SysFont(None, 100)
    text = font.render("Smash the Bricks", True, white)

    font_2 = pygame.font.SysFont(None, 70)
    text_2 = font_2.render("Press SPACE to Start Game", True, white)

    bgImg = pygame.image.load("img_1.jpg")
    bgMusic = pygame.mixer.Sound('music_1.wav')
    bgMusic.play()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # quit pygame
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bgMusic.set_volume(0.5)
                    main()

        screen.blit(bgImg, (0,0))

        screen.blit(text, (200, 100))
        screen.blit(text_2, (180, 200))

        pygame.display.flip()

def gameOver():
    pass

def life(count):
    font = pygame.font.SysFont(None, 30)
    text = font.render("Life : {}".format(count), True, red)
    screen.blit(text, (5,5))

def main():
    barW = 200
    barH = 20

    barX = screenWidth // 2 - barW // 2
    barY = screenHeight - barH - 5

    moveBarX = 0

    ballRadius = 8
    ballY = barY - ballRadius
    moveBallX = 0
    moveBally = 0

    moveBall = False

    brickW = 100
    brickH = 30
    brickList = []
    rows = 5
    cols = screenWidth // brickW

    for i in range(1,rows):
        for j in range(cols):
            brickX = j * (brickW + 5)
            brickY = i * (brickH + 5)
            brick = pygame.Rect(brickX, brickY, brickW, brickH)
            brickList.append(brick)

    speed = 0.3
    lifeCount = 3

    while True:
        if not moveBall:
            ballX = barX + barW // 2

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # quit pygame
                quit()  # quit python

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moveBarX = speed
                elif event.key == pygame.K_LEFT:
                    moveBarX = -speed

                if event.key == pygame.K_SPACE:
                    moveBallX = speed
                    moveBally = -speed
                    moveBall = True

            else:
                moveBarX = 0

        screen.fill(white)

        barRect = pygame.draw.rect(screen, red, [barX, barY, barW, barH])
        barX += moveBarX

        pygame.draw.circle(screen, black, [ballX, ballY], ballRadius)
        ballX += moveBallX
        ballY += moveBally
        ballRect = pygame.Rect(ballX, ballY, ballRadius, ballRadius)

        for i in range(len(brickList)):
            pygame.draw.rect(screen, blue, brickList[i])

        for i in range(len(brickList)):
            if brickList[i].colliderect(ballRect):
                del brickList[i]
                moveBally = speed
                speed += 0.1
                break

        # Right Boundary
        if ballX > screenWidth - ballRadius:
            moveBallX = -speed
        # Left Boundary
        elif ballX < ballRadius:
            moveBallX = speed

        # Top Boundary
        if ballY < ballRadius:
            moveBally = speed
        # Bottom Boundary
        elif ballY > screenHeight * 2:
            moveBallX = 0
            moveBally = 0
            moveBall = False
            ballY = barY - ballRadius
            lifeCount -= 1

        if barRect.colliderect(ballRect):
            moveBally = -speed

        life(lifeCount)

        pygame.display.flip()

# main()
homeScreen()