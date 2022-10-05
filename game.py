import pygame, random
import constants, windowgui

class Game:
    def __init__(self, window):
        self.window = window
        self.left_paddle = self.create_paddle("left")
        self.right_paddle = self.create_paddle("right")
        self.paddles = [self.left_paddle, self.right_paddle]
        self.balls = [self.create_ball()]
        self.items = self.paddles + self.balls

        self.left_score = 0
        self.right_score = 0

        self.paddle_slow_timer = windowgui.Timer()
        self.paddle_slow_timer.start()
    
    def create_ball(self):
        return {
            "type": "ball",
            "rect": pygame.Rect(
                constants.SCREEN_WIDTH//2-constants.BALL_RADIUS,
                constants.SCREEN_HEIGHT//2-constants.BALL_RADIUS,
                constants.BALL_RADIUS*2, constants.BALL_RADIUS*2
            ),  
            "vel": random.choice([[constants.BALL_X_VEL, 0], [-constants.BALL_X_VEL, 0]]),
        }
    
    def create_paddle(self, side):
        x = constants.SCREEN_WIDTH-constants.PADDLE_WIDTH*2
        if side == "left":
            x = constants.PADDLE_WIDTH 

        return {
            "type": "paddle",
            "rect": pygame.Rect(x, constants.SCREEN_HEIGHT//2-constants.PADDLE_HEIGHT//2,
            constants.PADDLE_WIDTH, constants.PADDLE_HEIGHT),
            "vel": [0, 0]
        }

    def eventloop(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pass
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.right_paddle["vel"][1] = -constants.PADDLE_SPEED
        elif keys[pygame.K_DOWN]:
            self.right_paddle["vel"][1] = constants.PADDLE_SPEED
        if keys[pygame.K_w]:
            self.left_paddle["vel"][1] = -constants.PADDLE_SPEED
        elif keys[pygame.K_s]:
            self.left_paddle["vel"][1] = constants.PADDLE_SPEED
        
        if self.paddle_slow_timer.passed(.1):
            self.paddle_slow_timer.start()
            for paddle in self.paddles:
                if paddle["vel"][1] < 0:
                    paddle["vel"][1] += constants.PADDLE_SLOW
                elif paddle["vel"][1] > 0:
                    paddle["vel"][1] -= constants.PADDLE_SLOW  

        
        for item in self.items:
            item["rect"].x += item["vel"][0]
            item["rect"].y += item["vel"][1]
        
        for item in self.items:
            if item["type"] == "ball":
                pygame.draw.circle(self.window.screen, windowgui.Colors.ORANGE, 
                item["rect"].center, constants.BALL_RADIUS)
            else:
                pygame.draw.rect(self.window.screen, windowgui.Colors.BLACK, item["rect"])


        
        
        
        

        


        

        
