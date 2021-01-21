import pygame

colour_screen = input("Colour of Screen: ")

shape = input("Shape (line, circle, rectangle, ellipse, polygon): ")

shape_colour = input("Shape Colour: ")
while shape_colour == colour_screen:
    print("Pick a different colour -> The screen and shape are the same.")
    shape_colour = input("Shape Colour: ")

line_thickness = int(input("Line Thickness: "))
if shape == "line":
    print("Location Start: ")
    location_start = (int(input("x: ")), int(input("y: ")))
    print("Location End: ")
    location_end = (int(input("x: ")), int(input("y: ")))
elif shape == "circle":
    print("Location: ")
    location = (int(input("x: ")), int(input("y: ")))
    radius = int(input("Radius: "))
elif shape == "rectangle":
    location = (
        int(input("Top Left: ")),
        int(input("Top Right: ")),
        int(input("Rectangle Width: ")),
        int(input("Rectangle Height: ")),
    )
elif shape == "ellipse":
    location = (
        int(input("Top left x: ")),
        int(input("Top right y: ")),
        int(input("Oval Width: ")),
        int(input("Oval Height: ")),
    )
elif shape == "polygon":
    amount = int(input("How many point sets? "))
    points = []
    for i in range(amount):
        points.append(((int(input("x: "))), int(input("y: "))))

pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Hello -> My Window!")

myfont = pygame.font.SysFont("", 35)


play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    window.fill(colour_screen)

    if shape == "line":
        pygame.draw.line(
            window, shape_colour, location_start, location_end, line_thickness
        )
    elif shape == "circle":
        pygame.draw.circle(window, shape_colour, location, radius, line_thickness)
    elif shape == "rectangle":
        pygame.draw.rect(window, shape_colour, location, line_thickness)
    elif shape == "ellipse":
        pygame.draw.ellipse(window, shape_colour, location, line_thickness)
    elif shape == "polygon":
        pygame.draw.polygon(window, shape_colour, points, line_thickness)

    pygame.display.update()