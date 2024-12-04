import pygame

from constants import PIPE_SCALE, PIPE_IMG


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, is_top, gap, speed):
        super().__init__()
        self.image = pygame.image.load(PIPE_IMG).convert_alpha()

        # Reduce pipe size
        new_width = int(self.image.get_width() * PIPE_SCALE)
        new_height = int(self.image.get_height() * PIPE_SCALE)
        self.image = pygame.transform.scale(self.image, (new_width, new_height))

        # Set pipe position
        if is_top:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect = self.image.get_rect(bottom=y - gap // 2)
        else:
            self.rect = self.image.get_rect(top=y + gap // 2)

        self.rect.x = x
        self.speed = speed
        self.scored = False  # Track if the pipe has been scored

    def update(self):
        self.rect.x -= self.speed

    def is_off_screen(self):
        return self.rect.right < 0
