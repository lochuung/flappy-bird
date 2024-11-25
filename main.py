import pygame
from pygame.locals import *
import random

# Initialize the game
pygame.init()
clock = pygame.time.Clock()

# Game Settings Variable
FPS = 60
screen_width = 1028
screen_height = 512
# Game Variables
ground_scroll = 0
scroll_speed = 4
game_over = False
flying = False

# Display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")
font = pygame.font.SysFont('Bauhaus 93', 60)
# Background
bg = pygame.image.load('assets/images/background.png')
bg = pygame.transform.scale(bg, (screen_width, screen_height))

# Ground
ground = pygame.image.load('assets/images/lq-base.png')
# down revolution
ground = pygame.transform.scale(ground, (ground.get_width() // 2, ground.get_height() // 2))
ground_width = ground.get_width()

# Pipe
pipe = pygame.image.load('assets/images/pipe-red.png')


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        image_paths = [
            'assets/images/redbird-downflap.png',
            'assets/images/redbird-midflap.png',
            'assets/images/redbird-upflap.png',
        ]
        for path in image_paths:
            image = pygame.image.load(path)
            image = pygame.transform.scale(image, (50, 50))
            self.images.append(image)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.velocity = 0
        self.clicked = False

    def update(self):
        self.animation()
        if not self.clicked:
            self.velocity += 0.5
            if self.velocity > 8:
                self.velocity = 8
            if self.rect.bottom < 450:
                self.rect.y += int(self.velocity)
        if self.clicked:
            self.velocity = -10
            self.clicked = False
        self.rect.y += int(self.velocity)
        if self.rect.bottom > 450:
            self.rect.bottom = 450

        self.image = self.rotate()

    def jump(self):
        self.clicked = True

    def rotate(self):
        new_image = pygame.transform.rotozoom(self.images[self.index], self.velocity * -2, 1)
        return new_image

    def animation(self):
        self.counter += 1
        flap_cooldown = 5
        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]


bird_group = pygame.sprite.Group()
flappy = Bird(100, 200)
bird_group.add(flappy)

# Running
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    # Ground
    ground_y = screen_height - ground.get_height()
    screen.blit(ground, (ground_scroll, ground_y))
    screen.blit(ground, (ground_scroll + ground_width, ground_y))
    if ground_scroll > -1 * ground_width:
        ground_scroll -= scroll_speed
    else:
        ground_scroll = 0
    # Bird
    bird_group.draw(screen)
    bird_group.update()

    if flappy.rect.bottom >= 450:
        game_over = True

    # Event
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_SPACE or event.type == MOUSEBUTTONDOWN:
            flappy.jump()
        if event.type == QUIT:
            running = False

    # Update
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
