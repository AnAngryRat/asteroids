import pygame

class Score(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.points = 0
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        self.x = x
        self.y = y

    def inc(self):
        self.points += 1

    def draw(self, screen):
        text = self.font.render(f"Score: {self.points}", True, "white")
        screen.blit(text, (self.x, self.y))
