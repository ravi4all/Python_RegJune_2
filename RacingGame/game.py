import pygame
import time
import random
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

def count(x):
    font = pygame.font.SysFont(None, 140)
    text = font.render("{}".format(x), True, white)
    screen.blit(text, (450, 100))
    # print(c[x])
    time.sleep(1)

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
    x = 0
    c = ['3', '2', '1', 'GO','']

    startGame = False

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

    car_1_Rect = car_1.get_rect()
    car_1_Rect.x, car_1_Rect.y = rect.x - 100, rect.y
    car1_moveY = random.randint(1,5)

    car_2_Rect = car_2.get_rect()
    car_2_Rect.x, car_2_Rect.y = rect.x + 100, rect.y
    car2_moveY = random.randint(1,5)
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
            rect.y -= 8
        else:moveX -= 1

        if rect.y > height/2:
            rect.y = height/2
        elif car_1_Rect.y > height/2:
            car_1_Rect.y = height/2
        elif car_2_Rect.y > height/2:
            car_2_Rect.y = height/2

        if moveX < 0:
            moveX = 0
        elif moveX > 200:
            moveX = 200

        screen.fill(white)
        for i in range(len(trackList)):
            screen.blit(track, (trackList[i].x, trackList[i].y))
        screen.blit(myCar, (rect.x, rect.y))
        screen.blit(car_1, (car_1_Rect.x, car_1_Rect.y))
        screen.blit(car_2, (car_2_Rect.x, car_2_Rect.y))

        if startGame:
            car_1_Rect.y -= car1_moveY
            car_2_Rect.y -= car2_moveY
            if moveX > 1:
                for i in range(len(trackList)):
                    trackList[i].y += moveX
            speed(moveX)

        elif not startGame:
            if x <= 4:
                count(c[x])
                print(c[x])
                x += 1
            if x == 4:
                startGame = True

        pygame.display.update()
        clock.tick(FPS)

game()