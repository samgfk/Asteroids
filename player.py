import pygame
from circleshape import CircleShape 
import constants
class Player(CircleShape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = constants.PLAYER_RADIUS
        super().__init__(x, y, self.radius)  # Pass radius here
        self.rotation = 0 
   
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def __draw__(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle())
    
    def rotate(self, dt):
        self.rotation += dt*constants.PLAYER_TURN_SPEED
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt     


