import sys
from os import kill

import pygame

from logger import log_event
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    # creating groups
    # this will hold all the objects that can be updated
    updatable = pygame.sprite.Group()



    # this will hold all the objects that can be drawn
    drawable = pygame.sprite.Group()

    # group for the asteroids
    asteroids = pygame.sprite.Group()

    # group for the asteroid
    shots = pygame.sprite.Group()

    # static container Field
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable,drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    # static container Field Objects
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                #log event
                log_event("player_hit")
                #print a message
                print("Game over!")
                # quit gamee
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    print("HIT")
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.kill()



        screen.fill("black")
        updatable.update(dt)

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
