import pygame

surf=pygame.display.set_mode((800,600))
run = True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
    pygame.draw.line(surf,(255,255,255),(10,20),(150,200),2)
    pygame.display.flip()
pygame.quit()