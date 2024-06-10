import pygame

surf=pygame.display.set_mode((800,600))
run = True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Vous avez appuyé sur la touche espace")
            elif event.key == pygame.K_a:
                print("Vous avez appuyé sur la touche A")
            elif event.key == pygame.K_RETURN:
                print("Vous avez appuyé sur la touche Entrée")
            else:
                print("Vous avez appuyé sur une touche mais zebi je sais pas laquelle")
    surf.fill((0,0,0))
    pygame.display.flip()
pygame.quit()