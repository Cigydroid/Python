import pygame
import sys

pygame.init()

# Window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platform Builder - Solid Blocks")

clock = pygame.time.Clock()

# Colors
WHITE = (25, 25, 105)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
RED = (200, 0, 0)

# Grid
TILE_SIZE = 10
platforms = set()

# Player
player_size = 20
player_rect = pygame.Rect(WIDTH // 2, HEIGHT - player_size, player_size, player_size)

velocity_y = 0
gravity = 0.8
speed = 4
jump_force = -12
on_ground = False

font = pygame.font.SysFont(None, 48)
win = False

running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # === STAVĚNÍ BLOKŮ ===
    mouse_buttons = pygame.mouse.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos()

    grid_x = (mouse_x // TILE_SIZE) * TILE_SIZE
    grid_y = (mouse_y // TILE_SIZE) * TILE_SIZE

    if mouse_buttons[0]:
        platforms.add((grid_x, grid_y))

    if mouse_buttons[2]:
        platforms.discard((grid_x, grid_y))

    keys = pygame.key.get_pressed()

    # === POHYB X ===
    dx = 0
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        dx = -speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        dx = speed

    player_rect.x += dx

    for plat in platforms:
        plat_rect = pygame.Rect(plat[0], plat[1], TILE_SIZE, TILE_SIZE)
        if player_rect.colliderect(plat_rect):
            if dx > 0:
                player_rect.right = plat_rect.left
            if dx < 0:
                player_rect.left = plat_rect.right

    # === POHYB Y ===
    if keys[pygame.K_SPACE] and on_ground:
        velocity_y = jump_force
        on_ground = False

    velocity_y += gravity
    player_rect.y += velocity_y

    on_ground = False

    for plat in platforms:
        plat_rect = pygame.Rect(plat[0], plat[1], TILE_SIZE, TILE_SIZE)
        if player_rect.colliderect(plat_rect):

            # Dopad shora
            if velocity_y > 0:
                player_rect.bottom = plat_rect.top
                velocity_y = 0
                on_ground = True

            # Náraz hlavou
            elif velocity_y < 0:
                player_rect.top = plat_rect.bottom
                velocity_y = 0

    # Okraje obrazovky
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > WIDTH:
        player_rect.right = WIDTH
    if player_rect.bottom > HEIGHT:
        player_rect.bottom = HEIGHT
        velocity_y = 0
        on_ground = True

    # Výhra
    if player_rect.top <= 0:
        win = True

    # === KRESLENÍ ===
    for plat in platforms:
        pygame.draw.rect(screen, BLUE, (plat[0], plat[1], TILE_SIZE, TILE_SIZE))

    pygame.draw.rect(screen, GREEN, player_rect)

    if win:
        text = font.render("VYHRÁL JSI!", True, RED)
        screen.blit(text, (WIDTH // 2 - 120, HEIGHT // 2 - 25))

    pygame.display.flip()

pygame.quit()
sys.exit()