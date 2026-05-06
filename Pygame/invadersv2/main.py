import pygame
import settings
from Player import Player
from Enemy import Enemy
from Bullet import Bullet
import random as rand
import os
class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = []
        # Načteme obrázky pomocí cesty ze settings
        # Pokud máš např. 5 obrázků (exp1 až exp5):
        for i in range(1, 6):
            img_path = settings.EXPLOSION_IMAGE_PATH.format(i)
            img = pygame.image.load(img_path).convert_alpha()
            # Můžeš explozi i automaticky zmenšit/zvětšit:
            # img = pygame.transform.scale(img, (60, 60))
            self.images.append(img)

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x, y))
        self.counter = 0

    def update(self):
        # Použijeme rychlost animace ze settings
        self.counter += 1
        if self.counter >= settings.EXPLOSION_ANIMATION_SPEED:
            self.counter = 0
            self.index += 1
            if self.index < len(self.images):
                self.image = self.images[self.index]
            else:
                self.kill() # Exploze zmizí po posledním obrázku

# --- NASTAVENÍ HRY ---
pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders OOP V2")
clock = pygame.time.Clock()

player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

enemy_group = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group() 
explosion_group = pygame.sprite.Group() # Grupa pro exploze

def create_enemies():
    x = 50  
    y = 25
    for i in range(2):
        for j in range(10):
            enemy = Enemy(x,y)
            enemy_group.add(enemy)
            x += 50 
        y += 50
        x = 50
create_enemies()
    
running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player.cooldown == 0:
                bullet = Bullet(player.rect.left + 5,player.rect.top + 40,"Player")
                player_group.add(bullet)
                bullet = Bullet(player.rect.right - 5,player.rect.top + 40,"Player")
                player_group.add(bullet)
                player.cooldown = pygame.time.get_ticks()

    # Logika střelby nepřátel
    if len(enemy_group) > 0 and rand.randint(0, 100) < 2:
        random_enemy = rand.choice(enemy_group.sprites())
        new_ebullet = Bullet(random_enemy.rect.centerx, random_enemy.rect.bottom, "alien")
        enemy_bullets.add(new_ebullet)

    # --- LOGIKA ZÁSAHŮ (KOLIZE) ---
    # Kontrola střel hráče proti alienům
    for sprite in player_group.sprites():
        if isinstance(sprite, Bullet): # Najdeme střely v player_group
            hits = pygame.sprite.spritecollide(sprite, enemy_group, True)
            if hits:
                sprite.kill() # Střela zmizí
                for enemy in hits:
                    # Vytvoření exploze na místě mrtvého aliena
                    expl = Explosion(enemy.rect.centerx, enemy.rect.centery)
                    explosion_group.add(expl)

    # Kolize nepřátelské střely s hráčem
    if pygame.sprite.spritecollide(player, enemy_bullets, True):
        print("Zásah hráče!")

    # --- UPDATE ---
    player_group.update()
    enemy_group.update()
    enemy_bullets.update()
    explosion_group.update()

    # --- VYKRESLOVÁNÍ ---
    screen.fill(settings.BG_COLOR)
    player_group.draw(screen)
    enemy_group.draw(screen)
    enemy_bullets.draw(screen)
    explosion_group.draw(screen)
    
    pygame.display.flip()

pygame.quit()