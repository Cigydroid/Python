import pygame
from projektSettings import *

class Player:
    def __init__(self):
        self.rect = pygame.Rect(180, 350, PLAYER_SIZE, PLAYER_SIZE)

        self.dashing = False
        self.dash_distance = 0
        self.last_dash_time = -DASH_COOLDOWN

    def move(self, keys, current_time, power_active):
        move_speed = 5
        if power_active == "speed":
            move_speed = 8

        moving_left = keys[pygame.K_a]
        moving_right = keys[pygame.K_d]

        # DASH START
        if keys[pygame.K_SPACE] and not self.dashing:
            if current_time - self.last_dash_time >= DASH_COOLDOWN:
                if moving_left or moving_right:
                    self.dashing = True
                    self.dash_distance = 0
                    self.last_dash_time = current_time

        # DASH
        if self.dashing:
            if keys[pygame.K_SPACE]:
                move = 0
                if moving_left:
                    move = -DASH_SPEED
                elif moving_right:
                    move = DASH_SPEED

                self.rect.x += move
                self.dash_distance += abs(move)

                if self.dash_distance >= WIDTH // 2:
                    self.dashing = False
            else:
                self.dashing = False
        else:
            if moving_left and self.rect.left > 0:
                self.rect.x -= move_speed
            if moving_right and self.rect.right < WIDTH:
                self.rect.x += move_speed

        # okraje
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def draw(self, screen):
        pygame.draw.rect(screen, (0,255,0), self.rect)