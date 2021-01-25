import pygame
import time

pygame.init()
x, y, width, height, movement = 30, 230, 30, 40, 10
white = (255, 255, 255)
window1 = pygame.display.set_mode((300, 300))

bullets = []

pygame.display.set_caption("background")
bckgrd = pygame.image.load(
    r"/home/josh/projects/grade12/3.Pygame_Intro/star_bckgrd.png"
)
bckgr_rect = bckgrd.get_rect()
my_alien = pygame.image.load(
    r"/home/josh/projects/grade12/3.Pygame_Intro/alien.png"
)  # .convert()
my_alien = pygame.transform.scale(my_alien, (60, 60))

bullet_pic = pygame.image.load(
    "/home/josh/projects/grade12/3.Pygame_Intro/bullet_edit.png"
)


def alien_draw():
    window1.blit(my_alien, (x, y))


def draw_bullets():
    for bullet in bullets:
        window1.blit(bullet[0], (bullet[1]["x"], bullet[1]["y"]))


def create_bullet(x, y):
    bullets.append([pygame.transform.scale(bullet_pic, (5, 15)), {"x": x, "y": y}])


def move_bullets():
    for bullet in bullets:
        bullet[1]["y"] -= 0.1


play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x += movement
        time.sleep(0.05)
    if keys[pygame.K_LEFT]:
        x -= movement
        time.sleep(0.05)

    if keys[pygame.K_SPACE]:
        create_bullet(x + 27, y - 25)

    window1.fill((0, 0, 0))
    window1.blit(bckgrd, bckgr_rect)
    alien_draw()
    draw_bullets()
    move_bullets()
    pygame.display.update()
