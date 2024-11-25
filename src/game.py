import pygame
from src.bird import Bird
from src.pipe import Pipe
from src.constants import BACKGROUND_IMG, FPS


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.bird = Bird()
        self.pipes = [Pipe(x=400)]
        self.background = pygame.image.load(BACKGROUND_IMG)
        self.score = 0

    def update(self):
        self.bird.update()
        for pipe in self.pipes:
            pipe.update()
            if pipe.is_off_screen():
                self.pipes.remove(pipe)
                self.pipes.append(Pipe(x=400))
                self.score += 1

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.bird.render(self.screen)
        for pipe in self.pipes:
            pipe.render(self.screen)

        # Hiển thị điểm
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        pygame.display.flip()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.bird.jump()

            self.update()
            self.render()
            self.clock.tick(FPS)
