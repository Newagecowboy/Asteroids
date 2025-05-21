import pygame
import sys
from constants import*
from player import Player
from asteroid import Asteroid 
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot 

def main():
        pygame.init()
        clock = pygame.time.Clock()
        dt = 0
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        Player.containers = (updatable, drawable)
        asteroids = pygame.sprite.Group()
        shots = pygame.sprite.Group()
        Asteroid.containers = (asteroids, updatable, drawable)
        Shot.containers = (shots, updatable, drawable)
        AsteroidField.containers = updatable
        asteroid_field = AsteroidField()
        

        print("Starting Asteroids!") 
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            
            dt = clock.tick(60) / 1000.0
            
            updatable.update(dt)
            
            for asteroid in asteroids:
                if asteroid.collision(player):
                    print("Game over!") 
                    sys.exit()

            screen.fill("black")
            for sprite in drawable:
                sprite.draw(screen)
            
            pygame.display.flip()


if __name__ == "__main__":
     main()
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")