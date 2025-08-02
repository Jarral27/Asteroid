import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)  # Set the container for Player class

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        

        #always update before rendering
        
        screen.fill("black")  # Fill the screen with black

        for sprite in drawable:
            sprite.draw(screen)

        dt = clock.tick(60) / 1000.0  # Limit to 60 FPS
        
        



        pygame.display.flip()  # Update the display !alwways last!

if __name__ == "__main__":
    main()
