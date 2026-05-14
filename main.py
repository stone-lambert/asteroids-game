from player import Player
import pygame
from asteroidfield import AsteroidField 
from asteroid import Asteroid
from constants import PLAYER_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event 
import sys
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids with pygame version", pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    updatable= pygame.sprite.Group()
    drawable= pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    while True:
        
        dt = clock.tick(60) / 1000.0
        
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  

        screen.fill("black")

        updatable.update(dt)
        for drawable_sprite in drawable:
            drawable_sprite.draw(screen)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
               log_event("player_hit")
               print("Game Over!")
               sys.exit()
        
        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    asteroid.split()
                    shot.kill()
        pygame.display.flip()

if __name__ == "__main__":
    main()
