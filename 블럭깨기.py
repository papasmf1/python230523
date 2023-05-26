import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Block Breaking Game")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Set up the player paddle
paddle_width = 100
paddle_height = 10
paddle_x = window_width // 2 - paddle_width // 2
paddle_y = window_height - paddle_height - 10
paddle_speed = 5
paddle = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)

# Set up the ball
ball_radius = 10
ball_x = random.randint(ball_radius, window_width - ball_radius)
ball_y = window_height // 2
ball_dx = random.choice([-2, 2])
ball_dy = -2
ball = pygame.Rect(ball_x, ball_y, ball_radius, ball_radius)

# Set up the blocks
block_width = 60
block_height = 20
block_rows = 5
block_cols = window_width // block_width
blocks = []
for row in range(block_rows):
    for col in range(block_cols):
        block_x = col * block_width
        block_y = row * block_height + 50
        block = pygame.Rect(block_x, block_y, block_width, block_height)
        blocks.append(block)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < window_width:
        paddle.x += paddle_speed

    # Move the ball
    ball.x += ball_dx
    ball.y += ball_dy

    # Check for collisions with walls
    if ball.left <= 0 or ball.right >= window_width:
        ball_dx *= -1
    if ball.top <= 0:
        ball_dy *= -1

    # Check for collisions with paddle
    if ball.colliderect(paddle):
        ball_dy *= -1

    # Check for collisions with blocks
    for block in blocks:
        if ball.colliderect(block):
            blocks.remove(block)
            ball_dy *= -1
            break

    # Check if the ball missed the paddle
    if ball.bottom >= window_height:
        running = False

    # Clear the screen
    window.fill(BLACK)

    # Draw the paddle, ball, and blocks
    pygame.draw.rect(window, WHITE, paddle)
    pygame.draw.circle(window, RED, (ball.x, ball.y), ball_radius)
    for block in blocks:
        pygame.draw.rect(window, GREEN, block)

    # Update the display
    pygame.display.update()
    clock.tick(60)

# Quit the game
pygame.quit()
