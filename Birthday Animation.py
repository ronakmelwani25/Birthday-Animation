import pygame
pygame.init()

WIDTH=1900
HEIGHT=1000
screen= pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("white")

balloon=pygame.image.load("Lesson 2 - Birthday Animation/Images/balloon.jpg")
bscale=pygame.transform.scale(balloon,(1900,1000))

cake=pygame.image.load("Lesson 2 - Birthday Animation/Images/cake.jpg")
cscale=pygame.transform.scale(cake,(1900,1000))

presents=pygame.image.load("Lesson 2 - Birthday Animation\Images\presents.jpg")
pscale=pygame.transform.scale(presents,(1900,1000))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(bscale,(0,0))
    pygame.display.update()
    pygame.time.wait(2000)
    screen.fill("white")
    screen.blit(cscale,(0,0))
    pygame.display.update()
    pygame.time.wait(2000)
    screen.fill("white")
    screen.blit(pscale,(0,0))
    pygame.display.update()
    pygame.time.wait(2000)