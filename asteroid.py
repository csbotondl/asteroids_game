import random

from circleshape import *
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    def update(self, dt: float) -> None:
        self.position += self.velocity*dt
    def split(self) -> None:
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            pass
        else:
            log_event("asteroid_split")
            theta = random.uniform(20,50)
            rad = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x,self.position.y, rad)
            asteroid1.velocity = self.velocity.rotate(theta) * 1.2
            asteroid2 = Asteroid(self.position.x,self.position.y, rad)
            asteroid2.velocity = self.velocity.rotate(-theta) * 1.2
