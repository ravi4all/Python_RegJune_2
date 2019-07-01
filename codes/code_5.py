import pygame
import random
pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width,height))

white = 255,255,255
red = 255,0,0

img = pygame.image.load("0.png")
imgWidth = img.get_width()
imgHeight = img.get_height()
imgX = random.randint(0, width - imgWidth)
imgY = random.randint(0, height - imgHeight)

x = 0
y = 0
moveX = 0
moveY = 0
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveX = 1
                moveY = 0
            elif event.key == pygame.K_LEFT:
                moveX = -1
                moveY = 0
            elif event.key == pygame.K_DOWN:
                moveY = 1
                moveX = 0
            elif event.key == pygame.K_UP:
                moveY = -1
                moveX = 0

    screen.fill(white)
    screen.blit(img, (imgX, imgY))
    rect_1 = pygame.draw.rect(screen,red,[x,y,50,50])
    img_rect = pygame.Rect(imgX, imgY, imgWidth, imgHeight)
    x += moveX
    y += moveY

    if rect_1.colliderect(img_rect):
        imgX = random.randint(0, width - imgWidth)
        imgY = random.randint(0, height - imgHeight)

    if x >= width - 50:
        moveX = -1
    elif x < 0:
        moveX = 1
    elif y >= height - 50:
        moveY = -1
    elif y < 0:
        moveY = 1

    pygame.display.update()