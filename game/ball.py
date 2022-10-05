import pygame
import random, math
import constants, windowgui
from game.physics_object import PhysicsObject
from game.paddle import Paddle

class Ball(PhysicsObject):
    def __init__(self, x, y):
        super().__init__(x, y, constants.BALL_SIZE, constants.BALL_SIZE)
        self.angle = random.randint(0, 360)
        self.x_speed = 5
        self.y_speed = 5
    
    def is_scored(self):
        if self.rect.x < 0 or self.rect.y > constants.SCREEN_WIDTH:
            return True
        return False
    
    def draw_angle(self, screen):
        start_pos = self.rect.center
        end_pos = self.rect.x + math.cos(self.angle) * 100, self.rect.y + math.sin(self.angle) * 100
        pygame.draw.line(screen, windowgui.Colors.GOLD, start_pos, end_pos, 5)
    
    def move(self, physics_objects):
        self.vel[0] = round(self.x_speed * math.cos(self.angle))
        self.vel[1] = round(self.y_speed * math.sin(self.angle))
        collision = super().move(physics_objects)
        if collision:
            print("collision")
            if isinstance(collision["physics_object"], Paddle):
                self.angle += 360
                    
                # self.x_speed = -self.x_speed
            else:
                self.y_speed = -self.y_speed


    def render(self, screen):
        pygame.draw.rect(screen, windowgui.Colors.YELLOW, self.rect)
        self.draw_angle(screen)