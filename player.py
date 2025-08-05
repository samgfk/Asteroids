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


