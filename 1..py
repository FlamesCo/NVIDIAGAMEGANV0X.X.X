import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Create the paddle
paddle = pygame.Rect(screen_width // 2, screen_height - 20, 100, 10)

# Create the ball
ball = pygame.Rect(screen_width // 2, screen_height // 2, 10, 10)

# Create the bricks with varying colors
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
bricks = []
for y in range(0, screen_height // 4, 30):
    for x in range(0, screen_width, 90):
        bricks.append((pygame.Rect(x, y, 80, 20), colors[(y//30) % 3]))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move_ip(-5, 0)
    if keys[pygame.K_RIGHT]:
        paddle.move_ip(5, 0)

    # Move the ball
    ball.move_ip(2, 2)

    # Collision detection
    if ball.colliderect(paddle):
        ball.top = paddle.top - 10
    if ball.left < 0 or ball.right > screen_width:
        ball.left = 0
    if ball.top < 0 or ball.bottom > screen_height:
        ball.top = 0
    for brick, color in bricks:
        if ball.colliderect(brick):
            bricks.remove((brick, color))

    # Draw the paddle
    pygame.draw.rect(screen, (255, 255, 255), paddle)

    # Draw the ball
    pygame.draw.rect(screen, (255, 255, 255), ball)

    # Draw the bricks
    for brick, color in bricks:
        pygame.draw.rect(screen, color, brick)

    # Update the game display
    pygame.display.update()

# Quit Pygame
pygame.quit()
