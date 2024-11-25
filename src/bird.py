import pygame
from constants import BIRD_IMGS, BIRD_SCALE, BIRD_GRAVITY, BIRD_JUMP_STRENGTH, BIRD_MAX_FALL_SPEED


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y, scale=BIRD_SCALE):
        super().__init__()
        self.images = []
        self.index = 0
        self.counter = 0

        # Tải và thay đổi kích thước hình ảnh chim
        for img_path in BIRD_IMGS:
            img = pygame.image.load(img_path).convert_alpha()
            new_width = int(img.get_width() * scale)
            new_height = int(img.get_height() * scale)
            img = pygame.transform.scale(img, (new_width, new_height))
            self.images.append(img)

        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.velocity = 0
        self.clicked = False

    def update(self):
        self.animation()

        # Thêm trọng lực vào vận tốc
        self.velocity += BIRD_GRAVITY
        if self.velocity > BIRD_MAX_FALL_SPEED:
            self.velocity = BIRD_MAX_FALL_SPEED

        # Cập nhật vị trí của chim
        self.rect.y += int(self.velocity)

        # Đảm bảo chim không rơi khỏi màn hình
        if self.rect.bottom > 450:
            self.rect.bottom = 450
            self.velocity = 0

        # Xử lý nhảy
        if self.clicked:
            self.velocity = BIRD_JUMP_STRENGTH
            self.clicked = False

        # Xoay chim theo vận tốc
        self.image = self.rotate()

    def jump(self):
        self.clicked = True

    def rotate(self):
        # Xoay chim dựa trên vận tốc rơi
        return pygame.transform.rotozoom(self.image, self.velocity * -2, 1)

    def animation(self):
        # Đổi hình ảnh để tạo hiệu ứng flap
        self.counter += 1
        if self.counter > 5:  # Flap cooldown
            self.counter = 0
            self.index = (self.index + 1) % len(self.images)
        self.image = self.images[self.index]
