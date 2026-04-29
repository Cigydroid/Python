import pygame
import settings
from Player import Player
from Enemy import Enemy

pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders OOP V2")
clock = pygame.time.Clock()

player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

enemy = Enemy(50,25)
enemy_group =pygame.sprite.Group()
enemy_group.add(enemy)

running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(settings.BG_COLOR)
    player_group.update()
    player_group.draw(screen)
    enemy_group.update()
    enemy_group.draw(screen)
    pygame.display.flip()
pygame.quit()