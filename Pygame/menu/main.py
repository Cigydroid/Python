import pygame
import settings
from Player import Player
pygame.init()

screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")
running = True
def vypis_menu():
    screen.fill((0, 0, 127))
    screen.blit(settings.title_text, settings.title_rect)
    screen.blit(settings.play_text, settings.play_rect)
    screen.blit(settings.settings_text, settings.settings_rect)
    screen.blit(settings.quit_text, settings.quit_rect)
def vypis_settings():
    screen.fill((0, 0, 127))
    screen.blit(settings.res800_text, settings.res800_rect)
    screen.blit(settings.res1024_text, settings.res1024_rect)
    screen.blit(settings.res1280_text, settings.res1280_rect)
    screen.blit(settings.back_text, settings.back_rect)
state = "MENU"   # MENU, PLAYING, PAUSED, GAME_OVER
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if state == "MENU":
                if settings.play_rect.collidepoint(event.pos):
                    state = "PLAYING"
                elif settings.settings_rect.collidepoint(event.pos):
                    state = "SETTINGS"s
                elif settings.quit_rect.collidepoint(event.pos):
                    running = False
            elif state == "SETTINGS":
                if settings.res800_rect.collidepoint(event.pos):
                    settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT = 800, 600
                    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
                elif settings.res1024_rect.collidepoint(event.pos):
                    settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT = 1024, 768
                    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
                elif settings.res1280_rect.collidepoint(event.pos):
                    settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT = 1280, 960
                    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
                elif settings.back_rect.collidepoint(event.pos):
                    state = "MENU"
    if state == "MENU":
        vypis_menu()
    elif state == "PLAYING":
        # herní logika
        pass
    elif state == "SETTINGS":
        vypis_settings()
    elif state == "GAME_OVER":
        # zobrazení skóre, restart
        pass
    pygame.display.flip()
pygame.quit()