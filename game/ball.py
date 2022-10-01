import pygame
import random, math
import constants, windowgui
from game.physics_object import PhysicsObject

class Ball(PhysicsObject):
    def __init__(self, x, y):
        super().__init__(x, y, constants.BALL_SIZE, constants.BALL_SIZE)
        self.angle = random.randint(0, 360)
    
    def move(self, physics_objects):
        
        super().move(physics_objects)

    def render(self, screen):
        pygame.draw.rect(screen, windowgui.Colors.YELLOW, self.rect)