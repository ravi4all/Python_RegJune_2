import pygame
import random
pygame.init()

width = 1050
height = 500
screen = pygame.display.set_mode((width,height))

white = 255,255,255
red = 255,0,0
black = 0,0,0
blue = 0,0,255
green = 0,255,0

def game():
    barWidth = 150
    barHeight = 20
    bar_surface = pygame.Surface((barWidth, barHeight))
    bar_surface.fill(black)
    barRect = bar_surface.get_rect()
    barRect.x = width//2 - barWidth//2
    barRect.y = height - barHeight - 5
    barMoveX = 0

    ballRadius = 8
    ballY = barRect.y - ballRadius
    ballMoveX = 0
    ballMoveY = 0
    ballMove = False

    brickWidth = 100
    brickHeight = 25
    x = 0
    y = 0

    brickList = []
    row = 5
    col = width // brickWidth
    colorsList = []
    for i in range(row):
        for j in range(col):
            brickList.append(pygame.Rect((brickWidth + 5) * j, (brickHeight + 5) * i, brickWidth, brickHeight ))
            color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            colorsList.append(color)

    while True:
        if not ballMove:
            ballX = barRect.x + barWidth // 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    barMoveX = 1
                elif event.key == pygame.K_LEFT:
                    barMoveX = -1
                elif event.key == pygame.K_SPACE:
                    ballMoveX = 1
                    ballMoveY = -1
                    ballMove = True
            elif event.type == pygame.KEYUP:
                barMoveX = 0

        screen.fill(white)
        screen.blit(bar_surface, (barRect.x, barRect.y))
        barRect.x += barMoveX

        pygame.draw.circle(screen, blue, [ballX, ballY], ballRadius)
        ballRect = pygame.Rect(ballX, ballY, ballRadius, ballRadius)
        ballX += ballMoveX
        ballY += ballMoveY

        # for i in range(4):
        #     for j in range(10):
        #         pygame.draw.rect(screen, green, [x,y,brickWidth, brickHeight])
        #         x = (brickWidth + 5) * j
        #     y = (brickHeight + 5) * i
        #     x = 0

        for i in range(len(brickList)):
            pygame.draw.rect(screen, colorsList[i], brickList[i])

        for i in range(len(brickList)):
            if brickList[i].colliderect(ballRect):
                del brickList[i]
                del colorsList[i]
                ballMoveY  = 1
                break

        if ballX > width - ballRadius:
            ballMoveX = -1
        elif ballX < ballRadius:
            ballMoveX = 1
        elif ballY > height * 2:
            ballMove = False
            ballY = barRect.y - ballRadius
            ballMoveY = 0
            ballMoveX = 0
        elif ballY < ballRadius:
            ballMoveY = 1
        elif ballRect.colliderect(barRect):
            ballMoveY = -1

        pygame.display.update()
game()