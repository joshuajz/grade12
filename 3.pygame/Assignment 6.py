import pygame
import time

pygame.init()
x = 30
y = 30
width = 30
height = 40
movement = 3
window1 = pygame.display.set_mode((300, 300))
pygame.display.set_caption("animation")


def check_bounds(x, y):
    bounds = (300, 300)
    if x < 0:
        x = 0
    if x > bounds[0]:
        x = bounds[0]
    if y < 0:
        y = 0
    if y > bounds[1]:
        y = bounds[1]
    return x, y


play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += movement
        time.sleep(0.05)
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= movement
        time.sleep(0.05)
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= movement
        time.sleep(0.05)
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += movement
        time.sleep(0.05)
    window1.fill((0, 0, 0))
    x, y = check_bounds(x, y)
    pygame.draw.rect(window1, "orange", (x, y, width, height))
    pygame.display.update()