import pygame

surf = pygame.display.set_mode((900,900))
run = True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False