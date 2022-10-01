import pygame
import constants
from game.paddle import Paddle
from game.ball import Ball
from game.physics_object import PhysicsObject


class Game:
    def __init__(self, window):
        self.window = window
        self.left_paddle = Paddle(20, 0)
        self.right_paddle = Paddle(constants.SCREEN_WIDTH-20-constants.PADDLE_WIDTH, 0)
        self.ball = Ball(300, 300)

        self.balls = [self.ball]
        self.paddles = [self.left_paddle, self.right_paddle]
        self.walls = [
            PhysicsObject(0, -20, constants.SCREEN_WIDTH, 20),
            PhysicsObject(0, constants.SCREEN_HEIGHT, constants.SCREEN_WIDTH, 20)
        ]

        self.physics_objects = self.balls + self.paddles + self.walls
    
    def eventloop(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ball = Ball(300, 300)
                self.balls.append(ball)
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.right_paddle.vel[1] = -constants.PADDLE_SPEED
        elif keys[pygame.K_DOWN]:
            self.right_paddle.vel[1] = constants.PADDLE_SPEED
        if keys[pygame.K_w]:
            self.left_paddle.vel[1] = -constants.PADDLE_SPEED
        elif keys[pygame.K_s]:
            self.left_paddle.vel[1] = constants.PADDLE_SPEED
        
        for physics_object in self.physics_objects:
            other_physics_objects = self.physics_objects.copy()
            other_physics_objects.remove(physics_object)
            physics_object.move(other_physics_objects)
 
        for ball in self.balls:
            ball.render(self.window.screen)
           
        for paddle in self.paddles:
            paddle.render(self.window.screen)
