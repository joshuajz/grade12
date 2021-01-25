import pygame
import random

# import winsound


def main():
    score = 0
    pygame.init()
    window = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("window")
    play = True
    myFont = pygame.font.SysFont("", 100)
    circleColour = (0, 0, 200)
    circlePosition = (150, 100)

    cookie = pygame.image.load("cookie.png")

    plusOneList = []

    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # winsound.Beep(500, 100)
                x, y = event.pos
                if cookie.get_rect(topleft=(250, 250)).collidepoint(x, y):
                    score += 1
                    plusOneList.append(plusOne())
        # print(plusOneList)
        for one in plusOneList:
            print(one.alpha)
            if one.timer > 0:
                one.timer -= 1
            else:
                if one.alpha > 0:
                    one.alpha = max(0, one.alpha - 1)

            window.blit(one.text(), (100, 100))

        displayScore = myFont.render(
            f"{score} {'cookie' if score == 1 else 'cookies'}", True, (0, 0, 0)
        )

        window.fill((255, 255, 255))
        window.blit(cookie, (250, 250))
        window.blit(displayScore, (325, 100))
        pygame.display.update()


class plusOne:
    def __init__(self):
        self.alpha = 255
        self.colour = (0, 0, 0)
        self.timer = 40
        self.location = (random.randint(100, 400), random.randint(100, 300))
        self.og_font = pygame.font.SysFont("", 20).render("+1", True, self.colour)

    def text(self):
        text_surface = self.og_font.copy()
        text_surface.fill((0, 0, 0, self.alpha), special_flags=pygame.BLEND_RGB_MULT)
        return text_surface


main()