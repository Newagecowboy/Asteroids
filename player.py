import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS
from constants import PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # Player's facing angle (degrees)
        self.speed = 200  # Pixels per second
        self.thrust = False  # For

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        color = (255, 255, 255)
        points = self.triangle()
        line_width = 2 
        pygame.draw.polygon(screen, color, points, line_width)
        
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # ?
        if keys[pygame.K_d]:
            # ?
    
    
    def rotate(dt):
        PLAYER_TURN_SPEED * dt 

    
    def move(dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt    