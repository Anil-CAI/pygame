import pygame, random

pygame.init()
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

snake = [(100, 50)]
direction = (10, 0)
food = (random.randint(0, 59)*10, random.randint(0, 39)*10)
score = 0

run = True
while run:
    pygame.time.delay(100)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: direction = (-10, 0)
    if keys[pygame.K_RIGHT]: direction = (10, 0)
    if keys[pygame.K_UP]: direction = (0, -10)
    if keys[pygame.K_DOWN]: direction = (0, 10)

    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, head)

    if head == food:
        score += 1
        food = (random.randint(0, 59)*10, random.randint(0, 39)*10)
    else:
        snake.pop()

    if (head in snake[1:] or not 0 <= head[0] < WIDTH or not 0 <= head[1] < HEIGHT):
        print("Game Over! Score:", score)
        run = False

    win.fill((0, 0, 0))
    for s in snake:
        pygame.draw.rect(win, (0, 255, 0), (*s, 10, 10))
    pygame.draw.rect(win, (255, 0, 0), (*food, 10, 10))
    pygame.display.update()
    clock.tick(15)

pygame.quit()
