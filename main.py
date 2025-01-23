import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def check_exit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return pygame.key.get_pressed()[pygame.K_ESCAPE]

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # init sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    
    # init game env
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()
    
    # init sprite objects
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroids_field = AsteroidField()
    while True:
        if check_exit():
            return
        screen.fill('black')
        for sprite in updatable:
            sprite.update(dt)
        
        for sprite in asteroids:
            if sprite.colision_detected(player):
                print("GAME OVER!")
                return
            for shot in shots:
                if sprite.colision_detected(shot):
                    sprite.split()
                    shot.kill()
        
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()