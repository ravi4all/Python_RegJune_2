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
rect.y = height - 50
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
    else: moveX = 0

    screen.fill(white)
    for i in range(len(trackList)):
        screen.blit(track, (trackList[i].x, trackList[i].y))
    screen.blit(img, (rect.x, rect.y))

    if moveX > 1:
        for i in range(len(trackList)):
            trackList[i].y += moveX

    pygame.display.update()
    clock.tick(FPS)