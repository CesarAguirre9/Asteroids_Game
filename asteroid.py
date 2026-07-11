import pygame
import random

from constants import LINE_WIDTH
from Circleshape import CircleShape
from logger import log_event
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        else: 
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            a = self.velocity.rotate(angle)
            b = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            Asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            Asteroid1.velocity = a * 1.2
            Asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            Asteroid2.velocity = b* 1.2 
