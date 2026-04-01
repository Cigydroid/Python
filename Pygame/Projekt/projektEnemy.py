import pygame
import random
from projektSettings import *

class FallingBlock:
    def __init__(self, y_start=0):
        self.rect = pygame.Rect(
            random.randint(0, WIDTH - BLOCK_SIZE),
            y_start,
            BLOCK_SIZE,
            BLOCK_SIZE
        )

    def reset(self, y_start=0):
        self.rect.y = y_start
        self.rect.x = random.randint(0, WIDTH - BLOCK_SIZE)

    def update(self, speed):
        self.rect.y += speed

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)