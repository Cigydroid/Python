import pygame
import random
from Settings import *
from Player import *
from Enemies import *
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load(ENEMY_IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (ENEMY_WIDTH, ENEMY_HEIGHT))

        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = ENEMY_SPEED

    def update(self):
        self.rect.x += self.speed

        # otočení směru na kraji
        if self.rect.right >= WIDTH or self.rect.left <= 0:
            self.speed *= -1
            self.rect.y += 20


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load(BULLET_IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (BULLET_WIDTH, BULLET_HEIGHT))

        self.rect = self.image.get_rect(midbottom=(x, y))
        self.speed = BULLET_SPEED

    def update(self):
        self.rect.y -= self.speed

        if self.rect.bottom < 0:
            self.kill()








def vypis_menu():
    menu_font = pygame.font.SysFont("Arial", 50)
    title_text = menu_font.render("SPACE INVADERS", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(400, 50))
    screen.blit(title_text, title_rect)
    play_text = menu_font.render("PLAY", True, (255, 255, 255))
    play_rect = play_text.get_rect(center=(400, 200))
    settings_text = menu_font.render("SETTINGS", True, (255, 255, 255))
    settings_rect = settings_text.get_rect(center=(400, 300))
    quit_text = menu_font.render("QUIT", True, (255, 255, 255))
    quit_rect = quit_text.get_rect(center=(400, 400))
    
    screen.blit(play_text, play_rect)
    screen.blit(settings_text, settings_rect)
    screen.blit(quit_text, quit_rect)