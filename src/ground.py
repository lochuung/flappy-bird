import pygame
from constants import GROUND_IMG, SCREEN_HEIGHT


class Ground:
    def __init__(self, screen_width, scroll_speed):
        self.image = pygame.image.load(GROUND_IMG).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 2, self.image.get_height() // 2))
        self.scroll_speed = scroll_speed
        self.scroll = 0
        self.ground_width = self.image.get_width()
        self.ground_y = SCREEN_HEIGHT - self.image.get_height()

    def update(self):
        self.scroll -= self.scroll_speed
        if self.scroll <= -self.ground_width:
            self.scroll = 0

    def render(self, screen):
        screen.blit(self.image, (self.scroll, self.ground_y))
        screen.blit(self.image, (self.scroll + self.ground_width, self.ground_y))
