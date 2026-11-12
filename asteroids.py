import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroids(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt: float):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_angle = random.uniform(20,50)
        a1 = self.velocity.rotate(new_angle)
        a2 = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new1 = Asteroids(self.position[0], self.position[1],new_radius)
        new1.velocity = a1
        new2 = Asteroids(self.position[0], self.position[1],new_radius)
        new2.velocity = a2
