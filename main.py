import pygame

# init pygame
pygame.init()
# create game window
screen = pygame.display.set_mode((800,600))

# set game title
pygame.display.set_caption("Space Shooter")
# set game icon
icon = pygame.image.load('./images/icon.png')
pygame.display.set_icon(icon)

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,255,255))
    pygame.display.update()

