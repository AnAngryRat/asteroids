from circleshape import CircleShape
import pygame
from constants import LIVES, HEART_POINTS


class Lives(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()
        self.lives = LIVES
        self.x = x
        self.y = y

    def draw(self, screen, scale = 1):
        for i in range(self.lives):
            offset = i * 50
            points = [
                    (self.x + px + offset * scale, self.y + py * scale)
                    for px, py in HEART_POINTS
                ]

            pygame.draw.polygon(screen, "red", points)

    def hit(self):
        self.lives -= 1

    def dead(self):
        return self.lives == 0
