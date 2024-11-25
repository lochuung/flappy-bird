import pygame
import random
from bird import Bird
from ground import Ground
from pipe import Pipe
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BACKGROUND_IMG, PIPE_GAP


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Flappy Bird")

    # Background
    bg = pygame.image.load(BACKGROUND_IMG).convert_alpha()
    bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Font for score and game over message
    font = pygame.font.SysFont("Arial", 40)
    large_font = pygame.font.SysFont("Arial", 60)

    running = True
    while running:
        start_game = False
        game_over = False
        score = 0

        # Initialize Bird, Ground, and Pipes
        bird_group = pygame.sprite.Group()
        flappy = Bird(100, 200, scale=2)
        bird_group.add(flappy)
        ground = Ground(SCREEN_WIDTH, scroll_speed=4)

        pipe_group = pygame.sprite.Group()
        pipe_frequency = 1500
        last_pipe_time = pygame.time.get_ticks()

        while not start_game:
            screen.blit(bg, (0, 0))
            ground.render(screen)

            title_text = large_font.render("Press SPACE to Start", True, (255, 255, 255))
            screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    start_game = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    start_game = True

        while not game_over:
            screen.blit(bg, (0, 0))

            # Add new pipes
            current_time = pygame.time.get_ticks()
            if current_time - last_pipe_time > pipe_frequency:
                pipe_height = random.randint(100, SCREEN_HEIGHT - 250)
                pipe_top = Pipe(SCREEN_WIDTH, pipe_height, is_top=True, gap=PIPE_GAP)
                pipe_bottom = Pipe(SCREEN_WIDTH, pipe_height, is_top=False, gap=PIPE_GAP)
                pipe_group.add(pipe_top)
                pipe_group.add(pipe_bottom)
                last_pipe_time = current_time

            # Update and draw pipes
            pipe_group.update()
            pipe_group.draw(screen)

            # Remove off-screen pipes
            for pipe in pipe_group:
                if pipe.is_off_screen():
                    pipe_group.remove(pipe)

            # Update score
            for pipe in pipe_group:
                if not pipe.scored and pipe.rect.right < flappy.rect.left:
                    score += 0.5
                    pipe.scored = True

            # Display score
            score_text = font.render(f"Score: {int(score)}", True, (255, 255, 255))
            screen.blit(score_text, (20, 20))

            # Check for collisions
            if pygame.sprite.spritecollide(flappy, pipe_group, False) or flappy.rect.bottom >= 450:
                game_over = True

            # Update ground and bird
            ground.update()
            ground.render(screen)
            bird_group.update()
            bird_group.draw(screen)

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_over = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    flappy.jump()

            pygame.display.update()
            clock.tick(FPS)

        while game_over:
            screen.blit(bg, (0, 0))
            ground.render(screen)

            game_over_text = large_font.render("GAME OVER", True, (255, 0, 0))
            score_text = font.render(f"Score: {int(score)}", True, (255, 255, 255))
            restart_text = font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))

            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
            screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))
            screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game_over = False
                    if event.key == pygame.K_q:
                        running = False
                        game_over = False

    pygame.quit()


if __name__ == "__main__":
    main()
