import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS
from asteroid import LINE_WIDTH



class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y, SHOT_RADIUS)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        pass

    def update(self, dt: float) -> None:

        self.position += self.velocity
        print("position:", self.position.x, self.position.y)

