import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *

def main():
    pygame.init()
    c = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    AsteroidField.containers = updatable
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    afield = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        x = c.tick(60)
        dt = x / 1000
        screen.fill((1, 1, 1))
        for item in drawable:
            item.draw(screen)
        for item in updatable:
            item.update(dt)
        pygame.display.flip()

if __name__ == "__main__":
    main()
