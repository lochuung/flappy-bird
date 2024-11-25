import pygame
from constants import BIRD_IMGS


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y, scale=1.5):
        super().__init__()
        self.images = []
        self.index = 0
        self.counter = 0

        # Tải và thay đổi kích thước hình ảnh chim
        for img_path in BIRD_IMGS:
            img = pygame.image.load(img_path).convert_alpha()
            # Scale hình ảnh theo tỷ lệ
            width = int(img.get_width() * scale)
            height = int(img.get_height() * scale)
            img = pygame.transform.scale(img, (width, height))
            self.images.append(img)

        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.velocity = 0
        self.clicked = False

    def update(self):
        self.animation()
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
        # Xoay chim dựa trên tốc độ rơi
        return pygame.transform.rotozoom(self.image, self.velocity * -2, 1)

    def animation(self):
        # Đổi hình ảnh để tạo hiệu ứng flap
        self.counter += 1
        if self.counter > 5:  # Flap cooldown
            self.counter = 0
            self.index = (self.index + 1) % len(self.images)
        self.image = self.images[self.index]
