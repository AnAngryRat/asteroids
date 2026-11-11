import pygame

from circleshape import CircleShape


class Asteroids(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt: float):
        self.position += self.velocity * dt
