import pygame
from Drawable import Drawable


class Player(Drawable):
    def __init__(self, name, color, position):
        super().__init__(color, position)
        self.name = name

    def getPolygon(self):
        # TODO: Calculate the polygon from the position and angle
        return [(self.position.x+10,self.position.y),
                (self.position.x,self.position.y+25),
                (self.position.x+10,self.position.y+20),
                (self.position.x+20,self.position.y+25)]

    def rotate(self, angle):
        pass
        
    def thrust(self, force):
        pass

    def draw(self, screen, dt):
        super().draw(screen, dt)
        print("Drawing player")
        # TODO: Draw thrust if player is accelerating