import pygame
from settings import *
from Block import *
from Player import *
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jump Game")
clock =  pygame.time.Clock()


hrac = Player(250,800)
hrac_group = pygame.sprite.Group()
hrac_group.add(hrac)
block = Block(250, 400)
block_group = pygame.sprite.Group()
block_group.add(block)

running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False

    hrac_group.draw(screen)
    hrac_group.update()
    clock.tick(FPS)
    pygame.display.update() 
pygame.quit()