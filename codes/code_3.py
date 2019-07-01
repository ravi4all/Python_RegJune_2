import pygame
pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width,height))

white = 255,255,255
red = 255,0,0
screen.fill(white)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # surface,color,[x,y,width,height]
    pygame.draw.rect(screen,red,[0,0,50,50])
    pygame.draw.circle(screen,red,[100,100],50)

    pygame.display.update()