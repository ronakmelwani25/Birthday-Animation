import pygame
pygame.init()

WIDTH=1900
HEIGHT=1000
screen= pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("white")

#print(pygame.font.get_fonts())

balloon=pygame.image.load("Lesson 2 - Birthday Animation/Images/balloon.jpg")
bscale=pygame.transform.scale(balloon,(1900,1000))
font1=pygame.font.SysFont("impact",154)
text1=font1.render("HAPPY BIRTHDAY",True,"black")
font2=pygame.font.SysFont("simsun",154)
text2=font2.render("Have a great day!",True,"navy")
font3=pygame.font.SysFont("yugothicui",154)
text3=font3.render("Enjoy your gifts!",True,"red")

cake=pygame.image.load("Lesson 2 - Birthday Animation/Images/cake.jpg")
cscale=pygame.transform.scale(cake,(1900,1000))

presents=pygame.image.load("Lesson 2 - Birthday Animation\Images\presents.jpg")
pscale=pygame.transform.scale(presents,(1900,1000))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(bscale,(0,0))
    screen.blit(text1,(500,100))
    pygame.display.update()
    pygame.time.wait(2000)
    screen.fill("white")
    screen.blit(cscale,(0,0))
    screen.blit(text2,(300,800))
    pygame.display.update()
    pygame.time.wait(2000)
    screen.fill("white")
    screen.blit(pscale,(0,0))
    screen.blit(text3,(450,800))
    pygame.display.update()
    pygame.time.wait(2000)