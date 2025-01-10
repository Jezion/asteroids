import pygame
from constants import *
from player import Player

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
    Player.containers = (updatable, drawable)
    
    # init game env
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()
    
    # init sprite objects
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        if check_exit():
            return
        screen.fill('black')
        for sprite in updatable:
            sprite.update(dt)
        
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()