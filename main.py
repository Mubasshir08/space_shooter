import pygame
import random
import math

# Initialize pygame
pygame.init()

# Create game window
screen = pygame.display.set_mode((800, 600))

# Score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
scoreX = 10
scoreY = 10

def display_score(x, y):
    score_show = font.render(f"Score : {score}", True, (255, 255, 255))
    screen.blit(score_show, (x, y))

# Game over text
def display_game_over():
    text_show = font.render("Game Over", True, (255, 255, 255))
    text_rect = text_show.get_rect(center=(400, 300))  # Centered on the screen
    screen.blit(text_show, text_rect)

# Set game title and icon
pygame.display.set_caption("Space Shooter")
icon = pygame.image.load('./images/icon.png')
pygame.display.set_icon(icon)

# Player variables
player_icon = pygame.image.load('./images/spaceship.png')
playerX = 370
playerY = 470
playerX_change = 0

def player(x, y):
    screen.blit(player_icon, (x, y))

# Enemy variables
enemy_icon = pygame.image.load('./images/alien.png')
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemy = 6

def enemy(x, y):
    screen.blit(enemy_icon, (x, y))

# Bullet variables
bullet_icon = pygame.image.load('./images/bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 10
bullet_state = 'ready'

def bullet_fire(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet_icon, (x, y))

# Bullet and enemy collision detection
def isCollision(eX, eY, bX, bY):
    distance = math.sqrt((math.pow((eX - bX), 2)) + (math.pow((eY - bY), 2)))
    return distance < 24

# Enemy and player collision detection
def isEnemyCollision(eX, eY, pX, pY):
    distance = math.sqrt((math.pow((eX - pX), 2)) + (math.pow((eY - pY), 2)))
    return distance < 75

# Background image
bg_image = pygame.image.load('./images/background.png')

def bgImg():
    screen.blit(bg_image, (0, 0))

# Initialize enemy positions
for _ in range(num_of_enemy):
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(5)
    enemyY_change.append(40)

# Game loop variables
running = True
game_over = False

# Game loop
while running:
    bgImg()  # Draw the background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key press events
        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    playerX_change = 5  # Move right
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    playerX_change = -5  # Move left
                if event.key == pygame.K_SPACE and bullet_state == 'ready':
                    bulletX = playerX  # Set bullet starting position
                    bullet_fire(bulletX + 17, bulletY)

            # Key release events
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_d, pygame.K_a]:
                    playerX_change = 0  # Stop movement

    if not game_over:
        # Update player position
        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:  # Prevent moving off-screen
            playerX = 736

        # Update enemy positions
        for i in range(num_of_enemy):
            # Enemy movement
            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 5
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -5
                enemyY[i] += enemyY_change[i]

            # Check if the bullet hits the enemy
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                bulletY = 480
                bullet_state = 'ready'
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)
                score += 1

            # Check if the enemy collides with the player
            enemy_collision = isEnemyCollision(enemyX[i], enemyY[i], playerX, playerY)
            if enemy_collision:
                game_over = True  # Set the game over flag
                break  # Exit the enemy loop

            # Draw enemy (only if no collision with player)
            if not game_over:
                enemy(enemyX[i], enemyY[i])

        # Bullet movement
        if bullet_state == 'fire':
            bullet_fire(bulletX + 17, bulletY)
            bulletY -= bulletY_change
            if bulletY <= 0:
                bulletY = 480
                bullet_state = 'ready'

    # Display the score
    display_score(scoreX, scoreY)

    if game_over:
        display_game_over()

    # Draw player
    player(playerX, playerY)

    # Update display
    pygame.display.update()
