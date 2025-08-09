import random
import pygame
from constants import * 
from player import Player
from circleshape import CircleShape
from random import uniform
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", tuple(self.position), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        self.random_angle = random.uniform(20, 50)
        self.split1_vector = self.velocity.rotate(self.random_angle)
        self.split2_vector = self.velocity.rotate(-self.random_angle)
        self.split2_radius = self.radius-ASTEROID_MIN_RADIUS
        self.split1_radius = self.radius-ASTEROID_MIN_RADIUS

        self.split_asteroid1 = Asteroid(self.position.x,self.position.y,self.split1_radius)
        self.split_asteroid2 = Asteroid(self.position.x,self.position.y,self.split2_radius)
        self.split_asteroid1.velocity = self.split1_vector * 1.2
        self.split_asteroid2.velocity = self.split2_vector * 1.2



        
        
      

       

