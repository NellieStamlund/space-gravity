import math
import pygame
from Drawable import Drawable

toRad = math.pi/180
class Player(Drawable):
    def __init__(self, name, color, position):
        # Create a space craft as a polygon with (0,0) at center
        super().__init__([pygame.Vector2(0,-13),
                          pygame.Vector2(-10,12),
                          pygame.Vector2(0,7),
                          pygame.Vector2(10,12)], color, position)
        self.name = name

        # Use angle to know which way the player is facing
        self.angle = 180

    def rotate(self, angle):

        # Recreate shape0 with new angle
        shape0 = []
        for point in self.shape0:
            shape0.append(point.rotate(angle))
        self.shape0 = shape0

        # Store new angle of player
        self.angle -= angle
        if (self.angle < 0):
            self.angle += 360
        if (self.angle > 360):
            self.angle -= 360
        print(self.angle)
        
    def thrust(self, force):
        x = math.sin(self.angle*toRad) * force
        y = math.cos(self.angle*toRad) * force
        velocity = pygame.Vector2(x,y)
        self.velocity += velocity

    def draw(self, screen, dt):
        super().draw(screen, dt)
        # TODO: Draw thrust if player is accelerating

    def fire(self):
        x = math.sin(self.angle*toRad) * 300
        y = math.cos(self.angle*toRad) * 300
        bullet = Drawable([pygame.Vector2(0,0)], "White", pygame.Vector2(self.position + self.shape0[0]))
        bullet.velocity = pygame.Vector2(x,y) + self.velocity
        return bullet