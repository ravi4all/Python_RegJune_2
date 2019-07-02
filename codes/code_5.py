import pygame
import random
pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width,height))

white = 255,255,255
red = 255,0,0
black = 0,0,0

img = pygame.image.load("0.png")
imgWidth = img.get_width()
imgHeight = img.get_height()
imgX = random.randint(0, width - imgWidth)
imgY = random.randint(0, height - imgHeight)

x = 0
y = 0
moveX = 0
moveY = 0

snakeLength = 1
snakeList = []

coinSound = pygame.mixer.Sound('point.wav')
bgMusic = pygame.mixer.Sound('bg_music.wav')
bgMusic.play(-1)

def snake(snakeList):
    for i in range(len(snakeList)):
        pygame.draw.rect(screen,red,[snakeList[i][0],
                                     snakeList[i][1],50,50])

FPS = 100
CLOCK = pygame.time.Clock()

def score(count):
    font = pygame.font.SysFont(None, 20)
    text = font.render("Score: {}".format(count),True,black)
    screen.blit(text, (10,10))

def gameOver(count):
    font = pygame.font.SysFont(None, 80)
    text = font.render("Game Over", True, black)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(text, (200,200))
        pygame.display.update()

count = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveX = 5
                moveY = 0
            elif event.key == pygame.K_LEFT:
                moveX = -5
                moveY = 0
            elif event.key == pygame.K_DOWN:
                moveY = 5
                moveX = 0
            elif event.key == pygame.K_UP:
                moveY = -5
                moveX = 0

    screen.fill(white)
    screen.blit(img, (imgX, imgY))
    rect_1 = pygame.draw.rect(screen,red,[x,y,50,50])
    img_rect = pygame.Rect(imgX, imgY, imgWidth, imgHeight)
    x += moveX
    y += moveY

    snakeHead = []
    snakeHead.append(x)
    snakeHead.append(y)
    snakeList.append(snakeHead)

    # print(snakeList)

    if len(snakeList) > snakeLength:
        del snakeList[0]

    snake(snakeList)

    if rect_1.colliderect(img_rect):
        imgX = random.randint(0, width - imgWidth)
        imgY = random.randint(0, height - imgHeight)
        snakeLength += 20
        FPS += 5
        count += 1
        coinSound.play()

    for each in snakeList[:-1]:
        if each == snakeList[-1]:
            gameOver(count)

    score(count)

    if x >= width:
        x = -50
    elif x < -50:
        x = width
    elif y >= height:
        y = -50
    elif y < -50:
        y = height

    pygame.display.update()
    CLOCK.tick(FPS)