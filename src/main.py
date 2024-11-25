import pygame
from bird import Bird
from ground import Ground
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BACKGROUND_IMG


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Flappy Bird")

    # Background
    bg = pygame.image.load(BACKGROUND_IMG).convert_alpha()
    bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Khởi tạo Bird và Ground
    bird_group = pygame.sprite.Group()
    flappy = Bird(100, 200, scale=2.0)  # Scale 2 lần kích thước ban đầu
    bird_group.add(flappy)
    ground = Ground(SCREEN_WIDTH, scroll_speed=4)

    # Game variables
    game_over = False
    running = True

    while running:
        screen.blit(bg, (0, 0))

        # Ground update
        ground.update()
        ground.render(screen)

        # Bird update
        bird_group.update()
        bird_group.draw(screen)

        # Game over check
        if flappy.rect.bottom >= 450:
            game_over = True

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                flappy.jump()

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
