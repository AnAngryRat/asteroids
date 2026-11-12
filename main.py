import pygame
import asyncio
from pygame.time import Clock
from asteroidfield import AsteroidField
from asteroids import Asteroids
import constants
from logger import log_state, log_event
from player import Player
import sys
from shot import Shot

SCREEN_WIDTH = constants.SCREEN_WIDTH
SCREEN_HEIGHT = constants.SCREEN_HEIGHT
PLAYER_RADIUS = constants.PLAYER_RADIUS

def initializeGame():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroids.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable,drawable, shots)
    AsteroidField()
    player = Player(SCREEN_WIDTH / 2 ,SCREEN_HEIGHT /2, PLAYER_RADIUS)
    return player, updatable, drawable, shots, asteroids

async def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    player, updatable, drawable, shots, asteroids = initializeGame()
    game_over = False


    while True:
        #log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                player, updatable, drawable, shots, asteroids = initializeGame()
                game_over = False
        screen.fill("black")
        if not game_over:
            updatable.update(dt)
            for i in asteroids:
                if i.collides_with(player) == True:
                    #log_event("player_hit")
                    print("Game Over!")
                    game_over = True
                    break
                for s in shots:
                    if s.collides_with(i) == True:
                        #log_event("asteroid_shot")
                        s.kill()
                        i.split()

        for i in drawable:
            i.draw(screen)
        if game_over:
            font = pygame.font.Font(None, 48)
            text = font.render("GAME OVER - PRESS ENTER", True, "white")

            text_rect = text.get_rect(
                center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            )

            screen.blit(text, text_rect)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        await asyncio.sleep(0.001)
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")


if __name__ == "__main__":
    asyncio.run(main())
