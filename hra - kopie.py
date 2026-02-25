import pygame, random, sys

# Start pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

# Load images
player_img = pygame.image.load("derek.webp").convert_alpha()
block_img = pygame.image.load("george.jfif").convert_alpha()

# Resize images to 40x40
player_img = pygame.transform.scale(player_img, (40, 40))
block_img = pygame.transform.scale(block_img, (40, 40))

# Create game objects (Rect is still used for position & collision)
player = pygame.Rect(180, 350, 40, 40)
block = pygame.Rect(random.randint(0,360), 0, 40, 40)

score, speed = 0, 5
state = "menu"

# Menu buttons
start_btn = pygame.Rect(100,150,200,50)
quit_btn  = pygame.Rect(100,220,200,50)

# Main loop
while True:

    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()[0]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # ---------------- MENU ----------------
    if state == "menu":

        screen.fill((0,0,0))

        pygame.draw.rect(screen,(0,150,0),start_btn)
        pygame.draw.rect(screen,(150,0,0),quit_btn)

        screen.blit(font.render("START", True,(255,255,255)), (150,160))
        screen.blit(font.render("QUIT", True,(255,255,255)), (165,230))

        pygame.display.flip()

        if start_btn.collidepoint(mouse_pos) and mouse_click:
            state = "game"
            score = 0
            block.y = 0
            block.x = random.randint(0,360)

        if quit_btn.collidepoint(mouse_pos) and mouse_click:
            sys.exit()

    # ---------------- GAME ----------------
    else:

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and player.left > 0:
            player.x -= 5

        if keys[pygame.K_d] and player.right < WIDTH:
            player.x += 5

        block.y += speed

        # Player misses block
        if block.y > HEIGHT:
            state = "menu"
            block.y = 0
            block.x = random.randint(0,360)

        # Player catches block
        if player.colliderect(block):
            score += 1
            block.y = 0
            block.x = random.randint(0,360)

        # Draw game
        screen.fill((0,0,0))

        # Draw images instead of rectangles
        screen.blit(player_img, player)
        screen.blit(block_img, block)

        pygame.display.set_caption(f"Score: {score}")

        pygame.display.flip()
        clock.tick(30)
