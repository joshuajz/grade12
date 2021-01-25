import random
import pygame


def random_numbers(lower, upper):
    return (random.randint(lower, upper), random.randint(lower, upper))


def card_find(number):
    return pygame.image.load(
        f"/home/josh/projects/grade12/3.Pygame_Intro/Cards/card {number}.png"
    )


lower = int(input("Lower Bound: "))
upper = int(input("Upper Bound: "))

user_number, computer_number = random_numbers(lower, upper)

winner = 0
if user_number > computer_number:
    winner = "User"
elif computer_number > user_number:
    winner = "Computer"
else:
    winner = "Tie"


pygame.init()

window = pygame.display.set_mode((750, 750))
pygame.display.set_caption("Higher/Lower")

myfont = pygame.font.SysFont("", 30)
numbers_display = myfont.render(
    f"Your Number: {user_number}                             Computer Number: {computer_number}",
    True,
    "white",
)
myfont_larger = pygame.font.SysFont("", 70)
winner = myfont_larger.render(f"Winner: {winner}", True, "white")

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    window.blit(numbers_display, (50, 50))
    window.blit(card_find(user_number), (50, 100))
    window.blit(card_find(computer_number), (375, 100))
    window.blit(winner, (200, 400))
    pygame.display.update()