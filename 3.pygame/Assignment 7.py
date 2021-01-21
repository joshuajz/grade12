import pygame
import time
from playsound import playsound

pygame.init()
x, y, width, height, velocity, movement, move = 30, 270, 30, 40, 5, 3, 1
window1 = pygame.display.set_mode((300, 300))
pygame.display.set_caption("animation")
play = True
isJumping = False


def check_collision(x, y):
    red_square = [(250 - 30, 250 - 40), (300, 300)]
    # (x start, y start), (x end, y end)

    # Check for the red square
    # Where the red square is
    # 250, 250      250, 300
    # 250, 300      300, 300
    if (
        red_square[0][0] <= x
        and x <= red_square[1][0]
        and red_square[0][1] <= y
        and y <= red_square[1][1]
    ):
        # We have a red collision
        print("Red Collision")
        playsound("beep.wav")

    # (x start, y start), (x end, y end)
    orange_square = [(150 - 30, 200 - 40), (200, 250)]
    if (
        orange_square[0][0] <= x
        and x <= orange_square[1][0]
        and orange_square[0][1] <= y
        and y <= orange_square[1][1]
    ):
        # We have a orange collision
        print("Orange Collision")
        playsound("beep-02.wav")

    print(x, y)


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
    if isJumping == False:
        if keys[pygame.K_SPACE]:
            isJumping = True
    if isJumping == True:
        force = (1 / 2) * move * 2 * (velocity ** 2)
        # print(force)
        y = y - force
        velocity = velocity - 1
        if velocity < 0:
            move = -1
        if velocity == -6:
            isJumping = False
            velocity = 5
            move = 1
    window1.fill((0, 0, 0))
    pygame.draw.rect(window1, (99, 99, 0), (x, y, width, height))

    # Draw the red square
    pygame.draw.rect(window1, "red", (250, 250, 50, 50))

    # Draw the orange squaue
    pygame.draw.rect(window1, "orange", (150, 200, 50, 50))

    check_collision(x, y)

    pygame.display.update()
