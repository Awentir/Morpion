import pygame

surf=pygame.display.set_mode((800,600))
run = True
posX = 50
vx = 1
clock = pygame.time.Clock()
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
    clock.tick(0)
    surf.fill((0,0,0))
    pygame.draw.circle(surf,(255,0,0),(posX,300),30,2)
    if posX>770 or posX<30:
        vx=-vx
    posX=posX+vx
    pygame.display.flip()
pygame.quit()