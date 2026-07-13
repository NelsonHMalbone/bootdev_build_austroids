import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # logs the event, only reached if we didn't return early
        log_event("asteroid_split")

        #  random angle between 20-50 degrees.
        angle = random.uniform(20, 50)

        # Two rotated vectors, one positive angle, one negative.
        forward_vector1 = self.velocity.rotate(angle)
        backward_vector1 = self.velocity.rotate(-angle)


        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Two new Asteroid objects created at the same position with the new radius
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Velocities set using the rotated vectors, scaled by 1.2
        new_asteroid1.velocity = forward_vector1 * 1.2
        new_asteroid2.velocity = backward_vector1 * 1.2