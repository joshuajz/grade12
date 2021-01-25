import random
import pygame
import time

pygame.init()

window = pygame.display.set_mode((300, 300))
pygame.display.set_caption("4a")


play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    window.fill((0, 0, 0))
    pygame.draw.rect(
        window, "blue", (0, 0, random.randint(1, 300), random.randint(1, 300)), 0
    )
    time.sleep(3)
    pygame.display.update()