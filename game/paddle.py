import pygame
import constants, windowgui
from game.physics_object import PhysicsObject

class Paddle(PhysicsObject):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PADDLE_WIDTH, constants.PADDLE_HEIGHT)
        self.timer = windowgui.Timer()
        self.timer.start()
    
    def move(self, physics_objects):
        super().move(physics_objects)
        if self.timer.passed(.1):
            self.timer.start()
            if self.vel[1] < 0:
                self.vel[1] += 1
            elif self.vel[1] > 0:
                self.vel[1] -= 1
    
    def render(self, screen):
        pygame.draw.rect(screen, windowgui.Colors.BLACK, self.rect)