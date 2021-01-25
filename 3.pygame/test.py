import pygame

pygame.init()

window = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Hello -> My Window!")

myfont = pygame.font.SysFont("", 35)
gameover = myfont.render("Game Over!", True, "red")

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    window.blit(gameover, (70, 140))
    pygame.display.update()