import sys
import pygame

from player import *
from constants import *
from asteroidfield import *
from asteroidfield import *
from shot import Shot
from asteroid import Asteroid
from logger import log_state, log_event

def main():
    print(f"Starting Asteroids with pygame version {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0.0
    clock = pygame.time.Clock()
    # Object Groups 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    shot = Shot(0, 0)
    while True:
        log_state()
        clock.tick(60)
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        for ob in updatable:
            ob.update(dt)
        for ast in asteroids:
            if ast.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for ast in asteroids:
            for bullet in shots:
                if ast.collides_with(bullet):
                    log_event("asteroid_shot")
                    ast.split()
                    bullet.kill()
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()