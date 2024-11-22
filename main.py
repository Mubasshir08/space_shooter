import pygame
import random

# init pygame
pygame.init()
# create game window
screen = pygame.display.set_mode((800,600))

# set game title
pygame.display.set_caption("Space Shooter")
# set game icon
icon = pygame.image.load('./images/icon.png')
pygame.display.set_icon(icon)

# player icon
player_icon = pygame.image.load('./images/spaceship.png')
playerX = 370
playerY = 470
playerX_change = 0

# player init function
def player(x,y):
    screen.blit(player_icon, (x,y))

# enemy icon
enemy_icon = pygame.image.load('./images/alien.png')
enemyX = random.randint(0,736)
enemyY = random.randint(100,150)

# enemy init function
def enemy(x,y):
    screen.blit(enemy_icon, (x,y))

# background image
img = pygame.image.load('./images/background.png')
def bgImg():
    screen.blit(img, (0,0))

# game loop
# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key press event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change += 5  # Start moving right
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change -= 5  # Start moving left

        # Key release event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = 0  # Stop moving

    # Update player position
    playerX += playerX_change

    # Boundary checking to keep the player within screen limits
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:  # 800 (screen width) - 64 (player width)
        playerX = 736

    # Clear screen and redraw player
    bgImg()
    player(playerX, playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()


