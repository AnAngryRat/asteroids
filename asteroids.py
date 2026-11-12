import random
import math
import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroids(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.verts = self.gen_verts()

    def gen_verts(self, num_points=12):
        verts = []
        for i in range(num_points):
            angle = (2 * math.pi / num_points) * i
            radius = self.radius * random.uniform(0.75,1.25)
            x = math.cos(angle) * radius
            y = math.sin(angle) * radius
            verts.append((x,y))

        return verts


    def draw(self, screen: pygame.Surface):
        points = [
                (self.position.x + x, self.position.y + y)
                for x, y in self.verts
            ]
        pygame.draw.polygon(screen, "white", points, 4)

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
