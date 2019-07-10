import pygame
pygame.init()

width = 1000
height = 500

screen = pygame.display.set_mode((width, height))

white = 255,255,255
red = 255,0,0

def speed(s):
    font = pygame.font.SysFont(None, 35)
    text = font.render("Speed : {}".format(s), True, red)
    screen.blit(text, (10, 10))


def game():
    myCar = pygame.image.load('car_2.png')
    # img.fill(red)
    rect = myCar.get_rect()
    rect.center = width/2, height/2
    rect.y = height - myCar.get_height()
    moveX = 0

    # track = pygame.image.load("track_1.jpg")
    # track = pygame.transform.rotate(track,90)
    # track_rect.center = width/2, height/2

    trackList = []
    for i in range(100):
        track = pygame.image.load("track_1.jpg")
        track = pygame.transform.rotate(track, 90)
        track_rect = track.get_rect()
        trackHeight = track.get_height()
        track_rect.center = width/2, height/2
        track_rect.y = -(trackHeight * i)
        trackList.append(track_rect)

    car_1 = pygame.image.load('car_1.png')
    car_2 = pygame.image.load('car_3.png')
    FPS = 50
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_SPACE]:
            moveX += 1
        else:moveX -= 1

        if moveX < 0:
            moveX = 0
        elif moveX > 200:
            moveX = 200

        screen.fill(white)
        for i in range(len(trackList)):
            screen.blit(track, (trackList[i].x, trackList[i].y))
        screen.blit(myCar, (rect.x, rect.y))
        screen.blit(car_1, (rect.x - 100, rect.y))
        screen.blit(car_2, (rect.x + 100, rect.y))

        if moveX > 1:
            for i in range(len(trackList)):
                trackList[i].y += moveX

        speed(moveX)
        pygame.display.update()
        clock.tick(FPS)

game()