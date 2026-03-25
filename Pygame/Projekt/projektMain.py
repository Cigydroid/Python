import pygame, sys, random

from projektSettings import *
from projektPlayer import Player
from projektEnemy import FallingBlock

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)

player = Player()

block = FallingBlock(0)
life_block = FallingBlock(-200)
power_block = FallingBlock(-300)

score, speed = 0, 5
lives = MAX_LIVES

power_active = None
power_timer = 0

state = "menu"

start_btn = pygame.Rect(100,150,200,50)
quit_btn  = pygame.Rect(100,220,200,50)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if state == "menu":
                if start_btn.collidepoint(event.pos):
                    state = "game"
                    score = 0
                    speed = 5
                    lives = MAX_LIVES

                    player = Player()

                    block.reset(0)
                    life_block.reset(-200)
                    power_block.reset(-300)

                    power_active = None

                if quit_btn.collidepoint(event.pos):
                    sys.exit()

    if state == "menu":
        screen.fill((0,0,0))

        pygame.draw.rect(screen,(0,150,0),start_btn)
        pygame.draw.rect(screen,(150,0,0),quit_btn)

        screen.blit(font.render("START", True,(255,255,255)), (150,160))
        screen.blit(font.render("QUIT", True,(255,255,255)), (165,230))

        pygame.display.flip()
        clock.tick(FPS)

    else:
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()

        player.move(keys, current_time, power_active)

        current_speed = speed
        if power_active == "slow":
            current_speed *= 0.5

        block.update(current_speed)

        # spawn life
        if random.randint(1,100) == 1 and life_block.rect.y < 0:
            life_block.reset(0)

        if life_block.rect.y >= 0:
            life_block.update(current_speed)

        # spawn power
        if random.randint(1,150) == 1 and power_block.rect.y < 0:
            power_block.reset(0)

        if power_block.rect.y >= 0:
            power_block.update(current_speed)

        # kolize
        if player.rect.colliderect(block.rect):
            score += 1
            speed += 0.2
            block.reset(0)

        if player.rect.colliderect(life_block.rect):
            if lives < MAX_LIVES:
                lives += 1
            else:
                score += 1
            life_block.reset(-200)

        if player.rect.colliderect(power_block.rect):
            power_active = random.choice(["slow", "shield", "speed"])
            power_timer = current_time
            power_block.reset(-300)

        # pád
        if block.rect.y > HEIGHT:
            if power_active == "shield":
                power_active = None
            else:
                lives -= 1

            block.reset(0)

            if lives <= 0:
                state = "menu"

        if life_block.rect.y > HEIGHT:
            life_block.reset(-200)

        if power_block.rect.y > HEIGHT:
            power_block.reset(-300)

        # power timer
        if power_active and current_time - power_timer > 5000:
            power_active = None

        # draw
        screen.fill((0,0,0))

        player.draw(screen)
        block.draw(screen,(255,0,0))

        if life_block.rect.y >= 0:
            life_block.draw(screen,(0,0,255))

        if power_block.rect.y >= 0:
            power_block.draw(screen,(255,255,0))

        screen.blit(font.render(f"Score: {score}", True,(255,255,255)), (10,10))
        screen.blit(font.render(f"Lives: {lives}", True,(255,255,255)), (WIDTH-140,10))

        # cooldown bar
        cd_ratio = min((current_time - player.last_dash_time)/DASH_COOLDOWN,1)
        pygame.draw.rect(screen,(100,100,100),(100,50,200,10))
        pygame.draw.rect(screen,(0,255,255),(100,50,int(200*cd_ratio),10))

        pygame.display.flip()
        clock.tick(FPS)