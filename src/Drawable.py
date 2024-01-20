import pygame

## Drawable class
# This class is the parent class of all drawable objects in the game.
class Drawable:
    def __init__(self, color, position):
        self.color = color
        self.position = position # Vector2
        self.angle = 0
        self.velocity = pygame.Vector2(0,0)

    def getPolygon():
        # TODO: Calculate the polygon from the position and angle
        return []

    def draw(self, screen, dt):
        # Calculate new player position s = v * t
        # new position = old position + velocity * time
        self.position += self.velocity * dt
        # TODO: Calculate new player angle

        pygame.draw.polygon(screen, self.color, self.getPolygon(), 0)
