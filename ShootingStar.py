import pygame

pygame.init()
win = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

player = pygame.Rect(50, 300, 30, 30)
gravity = 1
vel_y = 0

gravity_block = pygame.Rect(300, 180, 40, 40)
spike = pygame.Rect(500, 350, 40, 40)

platforms = [pygame.Rect(0, 370, 600, 30), pygame.Rect(0, 0, 600, 30)]

run = True
while run:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player.x -= 5
    if keys[pygame.K_RIGHT]: player.x += 5

    vel_y += gravity
    player.y += vel_y

    for plat in platforms:
        if player.colliderect(plat):
            if gravity > 0:
                player.bottom = plat.top
            else:
                player.top = plat.bottom
            vel_y = 0

    if player.colliderect(gravity_block):
        gravity *= -1
        vel_y = 0
        player.y += gravity * 5

    if player.colliderect(spike):
        print("You hit a spike!")
        run = False

    win.fill((30, 30, 30))
    pygame.draw.rect(win, (255, 255, 0), player)
    pygame.draw.rect(win, (0, 200, 255), gravity_block)
    pygame.draw.rect(win, (255, 0, 0), spike)
    for plat in platforms:
        pygame.draw.rect(win, (100, 100, 100), plat)

    pygame.display.update()

pygame.quit()
