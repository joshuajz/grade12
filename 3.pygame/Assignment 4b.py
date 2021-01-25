import random
import pygame
import time

pygame.init()

window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("4b")


def random_dim():
    return (random.randint(0, 75), random.randint(0, 75))


def random_loc():
    return (random.randint(0, 800), random.randint(0, 800))


play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    dim = random_dim()
    loc = random_loc()
    pygame.draw.rect(window, "blue", (dim + loc), 3)
    print(f"Creating a rectangle at x: {loc[0]:3} | y: {loc[1]:3}")
    time.sleep(1)
    pygame.display.update()