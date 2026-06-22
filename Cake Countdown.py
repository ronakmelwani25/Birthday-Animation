import pygame
pygame.init()

WIDTH=1900
HEIGHT=1000
screen= pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("white")

cake=pygame.image.load("Lesson 2 - Birthday Animation/Images/cake.jpg")
cake=pygame.transform.scale(cake,(1900,1000))
font=pygame.font.SysFont("ebrima",1000)
text5=font.render("5",True,"red")
text4=font.render("4",True,"blue")
text3=font.render("3",True,"green")
text2=font.render("2",True,"gold")
text1=font.render("1",True,"purple")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill("white")
    screen.blit(text5,(700,-250))
    pygame.display.update()
    pygame.time.wait(1000)
    screen.fill("white")

    screen.blit(text4,(700,-250))
    pygame.display.update()
    pygame.time.wait(1000)
    screen.fill("white")

    screen.blit(text3,(700,-250))
    pygame.display.update()
    pygame.time.wait(1000)
    screen.fill("white")

    screen.blit(text2,(700,-250))
    pygame.display.update()
    pygame.time.wait(1000)
    screen.fill("white")

    screen.blit(text1,(700,-250))
    pygame.display.update()
    pygame.time.wait(1000)
    screen.fill("white")

    screen.blit(cake,(0,0))
    pygame.display.update()
    pygame.time.wait(1000)
    break