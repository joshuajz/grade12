import random
import pygame


def random_number(lower, upper):
    return random.randint(lower, upper)


pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Random Colours are Fun")

random_shape_colour = (
    random_number(0, 255),
    random_number(0, 255),
    random_number(0, 255),
)

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    pygame.draw.rect(window, random_shape_colour, (150, 150, 150, 150), 0)

    pygame.display.update()