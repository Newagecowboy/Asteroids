import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED, PLAYER_SHOOT_SPEED
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, shots_group):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # Player's facing angle (degrees)
        self.speed = 200  # Pixels per second
        self.thrust = False 
        self.shots_group = shots_group

    
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
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shots_group.add(shot)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt



    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt    