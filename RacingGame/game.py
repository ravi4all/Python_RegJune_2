import pygame
pygame.init()

width = 1000
height = 500

screen = pygame.display.set_mode((width, height))

white = 255,255,255
red = 255,0,0

img = pygame.Surface((50,50))
img.fill(red)
rect = img.get_rect()
rect.center = width/2, height/2
moveX = 0
FPS = 500
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                FPS += 1
                moveX += 1
                print("Space Pressed...")
                # moveX = 1
        elif event.type == pygame.KEYUP:
            moveX = 0

    screen.fill(white)
    # pygame.draw.rect(screen, red, rect)
    screen.blit(img, (rect.x, rect.y))
    rect.x += moveX
    # print(rect.x,moveX)

    pygame.display.update()
    clock.tick(FPS)