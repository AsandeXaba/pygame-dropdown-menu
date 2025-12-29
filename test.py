import pygame, sys
from UI_resources import dropdown

pygame.init()

sw, sh = 800, 500
screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Tester")

fps = 60
clock = pygame.time.Clock()

# Dropdown test
btn_names = ["Start","Options", "Quit"]
menu = dropdown.Dropdown(100, 100, 100, 50, btn_names)

menu.content[1].changeFontSize(35)
menu.content[1].moveTextBy((-5, 5))

while True:
    screen.fill((255, 255, 255))
    clock.tick(fps)

    menu.show(screen)

    for btn in menu.content:
        if btn.clicked:
            print(f"{btn.name} button was clicked", end="\r")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()