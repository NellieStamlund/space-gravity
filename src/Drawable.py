import pygame

## Drawable class
# This class is the parent class of all drawable objects in the game.
class Drawable:
    def __init__(self, shape, color, position):
        self.color = color
        self.position = position # Vector2
        self.velocity = pygame.Vector2(0,0)

        # shape0 represents the original shape with angle and without position
        self.shape0 = shape # Vector2[]

        # shape represents the current shape at position
        self.shape = [] # Vector2[]
        for point in self.shape0:
            self.shape.append(point+position)

    def draw(self, screen, dt):
        # Calculate new player position s = v * t
        # new position = old position + velocity * time
        self.position += self.velocity * dt

        # Update the shape with the new position
        self.shape = []
        for point in self.shape0:
            self.shape.append(point+self.position)

        if len(self.shape0) > 1:
            pygame.draw.polygon(screen, self.color, self.shape, 0)
        else:
            pygame.draw.circle(screen, self.color, self.position, 1)
