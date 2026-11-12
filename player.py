from circleshape import CircleShape
from constants import LINE_WIDTH, PLAYER_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_COOLDOWN, SHOT_RADIUS
import pygame

from shot import Shot

class Player(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0
        self.invulTimer = 0
        self.invulDur = 3.0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt: float):
        self.rotation += dt * PLAYER_TURN_SPEED

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        self.cooldown -= dt
        if self.invulTimer > 0:
            self.invulTimer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt: float):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def hit(self):
        self.invulTimer = self.invulDur

    def shoot(self):
        if self.cooldown > 0:
            return
        bullet = Shot(self.position[0],self.position[1],SHOT_RADIUS)
        bullet.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.cooldown = SHOT_COOLDOWN
