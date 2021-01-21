import pygame

colour = input("Colour: ")
text = input("Text: ")
location = (int(input("x: ")), int(input("y: ")))

pygame.init()

window = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Assignment #1")

myfont = pygame.font.SysFont("", 35)
text_output = myfont.render(text, True, colour)

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    window.blit(text_output, location)
    pygame.display.update()