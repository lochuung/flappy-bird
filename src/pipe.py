import pygame
import random
from src.constants import PIPE_IMG


class Pipe:
    def __init__(self, x):
        self.image = pygame.image.load(PIPE_IMG)
        self.x = x
        self.height = random.randint(150, 450)
        self.speed = 5

    def update(self):
        self.x -= self.speed

    def render(self, screen):
        screen.blit(self.image, (self.x, self.height))
        screen.blit(pygame.transform.flip(self.image, False, True), (self.x, self.height - 600))  # Ống lật ngược

    def is_off_screen(self):
        return self.x + self.image.get_width() < 0
