import pygame
import os
from playsound import playsound
import time

score = 0
pygame.init()
window1 = pygame.display.set_mode((1000, 1000))
window1.fill("orange")
pygame.display.set_caption("click")
play = True
win = pygame.image.load("/home/josh/projects/grade12/3.Pygame_Intro/win.png")


def beep():
    playsound("beep.wav")


def pos_compare():
    global score
    x_pos, y_pos = pygame.mouse.get_pos()
    print(f"Current Position: {x_pos}, {y_pos}")
    if x_pos > 0 and x_pos < 100 and y_pos > 0 and y_pos < 100:
        print("Ouch!")
        score += 1
        print(f"Score: {score}")
        beep()
        return True
    else:
        print("You missed!")
        beep()
        return False


while play:
    my_position_x, my_position_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pos_compare():
                # Display an image, they got it right
                window1.blit(win, (100, 100))
                pygame.display.update()
                time.sleep(1)
                window1.fill("orange")
                pygame.display.update()

    pygame.display.update()
