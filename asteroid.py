import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        
        if self.position.x > SCREEN_WIDTH + 100:
            self.position.x = -50
        if self.position.x < -50:
            self.position.x = SCREEN_WIDTH + 100
        if self.position.y > SCREEN_HEIGHT + 100:
            self.position.y = -50
        if self.position.y < -50:
            self.position.y = SCREEN_HEIGHT - 100

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)

            a = self.velocity.rotate(random_angle)
            b = self.velocity.rotate(-random_angle)
            
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = a * 1.2
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = b * 1.2

    def kill_all(self):
        self.asteroid.kill()