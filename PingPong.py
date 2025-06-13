import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game - Out System with Restart")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)
big_font = pygame.font.SysFont("Arial", 50)

def draw_buttons():
    restart_btn = pygame.Rect(WIDTH//2 - 110, HEIGHT//2 + 40, 100, 40)
    quit_btn = pygame.Rect(WIDTH//2 + 10, HEIGHT//2 + 40, 100, 40)
    
    pygame.draw.rect(win, (0, 200, 0), restart_btn)  # Green Restart
    pygame.draw.rect(win, (200, 0, 0), quit_btn)      # Red Quit

    restart_text = font.render("Restart", True, (255, 255, 255))
    quit_text = font.render("Quit", True, (255, 255, 255))

    win.blit(restart_text, (restart_btn.x + 10, restart_btn.y + 5))
    win.blit(quit_text, (quit_btn.x + 25, quit_btn.y + 5))

    return restart_btn, quit_btn

def reset_game():
    return pygame.Rect(20, 150, 10, 100), pygame.Rect(570, 150, 10, 100), pygame.Rect(300, 200, 10, 10), [4, 4], None

# Initial game state
paddle1, paddle2, ball, ball_speed, winner = reset_game()
run = True
game_active = True

while run:
    pygame.time.delay(20)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    if game_active:
        # Paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paddle1.top > 0: paddle1.y -= 5
        if keys[pygame.K_s] and paddle1.bottom < HEIGHT: paddle1.y += 5
        if keys[pygame.K_UP] and paddle2.top > 0: paddle2.y -= 5
        if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT: paddle2.y += 5

        # Ball movement
        ball.x += ball_speed[0]
        ball.y += ball_speed[1]

        # Collision with top/bottom
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed[1] *= -1

        # Collision with paddles
        if ball.colliderect(paddle1) or ball.colliderect(paddle2):
            ball_speed[0] *= -1

        # Out system
        if ball.left <= 0:
            winner = "Player 2"
            game_active = False
        elif ball.right >= WIDTH:
            winner = "Player 1"
            game_active = False

    # Drawing
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 255, 255), paddle1)
    pygame.draw.rect(win, (255, 255, 255), paddle2)
    pygame.draw.ellipse(win, (255, 255, 255), ball)

    if not game_active and winner:
        # Show win message
        text = big_font.render(f"{winner} Wins!", True, (255, 0, 0))
        win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 60))

        # Draw buttons
        restart_btn, quit_btn = draw_buttons()

        # Handle button clicks
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        if restart_btn.collidepoint(mouse_pos) and mouse_click[0]:
            paddle1, paddle2, ball, ball_speed, winner = reset_game()
            game_active = True
        elif quit_btn.collidepoint(mouse_pos) and mouse_click[0]:
            run = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
