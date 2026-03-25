import pygame
from Player import *
from Python.Pygame.uhybani.Block import Block
from settings import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Uhybani")
running = True
clock = pygame.time.Clock()

try:
    with open("highscore.txt", "r") as f:
        highscore = int(f.read())
except FileNotFoundError:
    highscore = 0

score = 0
font = pygame.font.SysFont(None, 40)

SPAWN_BLOCK = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_BLOCK, 600)

hrac = Player()
hrac_group = pygame.sprite.Group()
hrac_group.add(hrac)

blok_group = pygame.sprite.Group()

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == SPAWN_BLOCK:
            # 🔥 rychlost podle score
            blok_speed = min(15, 5 + score // 5)
            blok_group.add(Block(blok_speed))

    # update
    hrac_group.update()
    blok_group.update()

    # vykreslení
    hrac_group.draw(screen)
    blok_group.draw(screen)

    # kontrola bloků, které opustily obrazovku
    for blok in blok_group:
        if blok.rect.top > HEIGHT:
            blok.kill()
            score += 1

    # kolize
    if pygame.sprite.spritecollide(hrac, blok_group, True, pygame.sprite.collide_mask):
        print("KOLIZE!")

        if score > highscore:
            highscore = score
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))

        pygame.time.delay(1000)
        running = False

    # skóre
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))

    highscore_text = font.render(f"High Score: {highscore}", True, BLACK)
    screen.blit(highscore_text, (10, 50))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()