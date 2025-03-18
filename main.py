import pygame, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def setup_game():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

def main():
    setup_game()
    dt = 0
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    #asteroidfield = pygame.sprite.Group()  
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))

        #updatable.update(dt)
        for sprite in updatable:
            sprite.update(dt)

        for sprite in asteroids:
            if sprite.collisions_check(player):
                print("GAME OVER")
                sys.exit()
        
        for sprite in drawable:
            sprite.draw(screen)

        #player.draw(screen)
        #player.update(dt)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
    
if __name__ == "__main__":
    main()

