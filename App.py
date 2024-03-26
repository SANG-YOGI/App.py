import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Random Game')

# Set up colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up player
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - player_size]
player_speed = 5

# Set up enemies
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 2

# Set up coins
coin_size = 30
coin_pos = [random.randint(0, WIDTH - coin_size), random.randint(0, HEIGHT - coin_size)]

# Set up fonts
font = pygame.font.Font(None, 36)

# Set up sounds
coin_sound = pygame.mixer.Sound('coin.wav')
enemy_sound = pygame.mixer.Sound('enemy.wav')
pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_pos[0] -= player_speed
            if event.key == pygame.K_RIGHT:
                player_pos[0] += player_speed
            if event.key == pygame.K_UP:
                player_pos[1] -= player_speed
            if event.key == pygame.K_DOWN:
                player_pos[1] += player_speed

    # Player boundaries
    if player_pos[0] < 0:
        player_pos[0] = 0
    if player_pos[0] > WIDTH - player_size:
        player_pos[0] = WIDTH - player_size
    if player_pos[1] < 0:
        player_pos[1] = 0
    if player_pos[1] > HEIGHT - player_size:
        player_pos[1] = HEIGHT - player_size

    # Enemy movement
    enemy_pos[1] += enemy_speed
    if enemy_pos[1] > HEIGHT:
        enemy_pos[0] = random.randint(0, WIDTH - enemy_size)
        enemy_pos[1] = 0

    # Collision detection
    if player_pos[0] < enemy_pos[0] + enemy_size and player_pos[0] + player_size > enemy_pos[0] and player_pos[1] < enemy_pos[1] + enemy_size and player_pos[1] + player_size > enemy_pos[1]:
        running = False
        pygame.mixer.music.stop()
        enemy_sound.play()

    if player_pos[0] < coin_pos[0] + coin_size and player_pos[0] + player_size > coin_pos[0] and player_pos[1] < coin_pos[1] + coin_size and player_pos[1] + player_size > coin_pos[1]:
        coin_pos = [random.randint(0, WIDTH - coin_size), random.randint(0, HEIGHT - coin_size)]
        pygame.mixer.music.stop()
        coin_sound.play()

    # Drawing
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen, WHITE, (coin_pos[0], coin_pos[1], coin_size, coin_size))
    label = font.render('Score: ' + str(coin_pos[1] // 50), 1, (BLUE))
    screen.blit(label, (10, 10))

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
